import streamlit as st
import cv2
import numpy as np
import os
import pandas as pd
from datetime import datetime

# ======================
# SETUP
# ======================

st.set_page_config(page_title="Face Attendance System", layout="centered")
st.title("Face Recognition Attendance System")

os.makedirs("registered_faces", exist_ok=True)

ATTENDANCE_FILE = "attendance.csv"
TRAINER_FILE = "trainer.yml"

face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)

if not os.path.exists(ATTENDANCE_FILE):
    pd.DataFrame(columns=["Name", "Date", "Time"]).to_csv(ATTENDANCE_FILE, index=False)

# ======================
# MENU
# ======================

menu = st.sidebar.selectbox(
    "Menu",
    ["Register Face", "Train Model", "Mark Attendance", "View Attendance"]
)

# ======================
# REGISTER FACE
# ======================
if menu == "Register Face":
    st.header("Face Registration")

    # The text input stays responsive now
    name = st.text_input("Enter Student Name (use underscores _ instead of spaces)")

    if st.button("Start Capture"):
        if name.strip() == "":
            st.warning("Please enter a name")
            st.stop()

        cap = cv2.VideoCapture(0)
        count = 0
        
        # Create a placeholder for the video feed inside the web page
        frame_placeholder = st.empty()
        
        # A stop button inside Streamlit
        stop_button = st.button("Stop & Save")

        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break

            # Convert to RGB for Streamlit display
            display_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            
            # Automatically save frames or wait for a condition
            # For automation, let's save 30 images quickly
            if count < 30:
                path = f"registered_faces/{name}_{count}.jpg"
                cv2.imwrite(path, frame)
                count += 1
                st.write(f"Captured {count}/30", end='\r')
            else:
                break

            # Show the frame in the browser
            frame_placeholder.image(display_frame, caption=f"Capturing for {name}...")

            if stop_button:
                break

        cap.release()
        st.success(f"Finished! {count} images saved for {name}")
# ======================
# TRAIN MODEL
# ======================

elif menu == "Train Model":

    st.header("Training Model")

    faces = []
    labels = []
    label_map = {}
    id_count = 0

    files = os.listdir("registered_faces")

    if len(files) == 0:
        st.error("No images found")
        st.stop()

    for file in files:

        if file.endswith((".jpg", ".jpeg", ".png")):

            path = os.path.join("registered_faces", file)
            img = cv2.imread(path)

            if img is None:
                continue

            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

            faces_detected = face_cascade.detectMultiScale(gray, 1.1, 5)

            if len(faces_detected) == 0:
                face = cv2.resize(gray, (200, 200))
            else:
                x, y, w, h = faces_detected[0]
                face = gray[y:y+h, x:x+w]
                face = cv2.resize(face, (200, 200))

            name = file.rsplit("_", 1)[0]

            if name not in label_map:
                label_map[name] = id_count
                id_count += 1

            faces.append(face)
            labels.append(label_map[name])

    if len(faces) == 0:
        st.error("Training failed: No faces found")
        st.stop()

    recognizer = cv2.face.LBPHFaceRecognizer_create()
    recognizer.train(faces, np.array(labels))
    recognizer.save(TRAINER_FILE)

    st.success("Model trained successfully")

# ======================
# MARK ATTENDANCE (WITH CHECKBOX CONTROL)
# ======================

elif menu == "Mark Attendance":

    st.header("Live Attendance System")

    if not os.path.exists(TRAINER_FILE):
        st.error("Train model first")
        st.stop()

    recognizer = cv2.face.LBPHFaceRecognizer_create()

    try:
        recognizer.read(TRAINER_FILE)
    except:
        st.error("Model corrupted. Retrain required.")
        st.stop()

    names = {}

    for file in os.listdir("registered_faces"):
        name = file.rsplit("_", 1)[0]
        if name not in names.values():
            names[len(names)] = name

    start_attendance = st.checkbox("Start Attendance Camera")

    if start_attendance:

        cap = cv2.VideoCapture(0)

        st.info("Camera ON - uncheck box to stop (rerun required)")

        frame_box = st.empty()
        marked = set()

        while True:

            ret, frame = cap.read()
            if not ret:
                break

            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            faces = face_cascade.detectMultiScale(gray, 1.1, 5)

            for (x, y, w, h) in faces:

                face = gray[y:y+h, x:x+w]
                face = cv2.resize(face, (200, 200))

                label, confidence = recognizer.predict(face)

                if confidence < 60:

                    name = names.get(label, "Unknown")

                    if name != "Unknown" and name not in marked:

                        now = datetime.now()

                        df = pd.read_csv(ATTENDANCE_FILE)

                        df = pd.concat([
                            df,
                            pd.DataFrame({
                                "Name": [name],
                                "Date": [now.strftime("%Y-%m-%d")],
                                "Time": [now.strftime("%H:%M:%S")]
                            })
                        ], ignore_index=True)

                        df.to_csv(ATTENDANCE_FILE, index=False)

                        marked.add(name)

                        st.success(f"Marked: {name}")

                else:
                    name = "Unknown"

                cv2.rectangle(frame, (x, y), (x+w, y+h), (0,255,0), 2)
                cv2.putText(frame, name, (x, y-10),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.8,
                            (0,255,0), 2)

            frame_box.image(frame, channels="BGR")

        cap.release()

# ======================
# VIEW ATTENDANCE
# ======================

elif menu == "View Attendance":

    st.header("Attendance Report")

    if os.path.exists(ATTENDANCE_FILE):
        df = pd.read_csv(ATTENDANCE_FILE)
        st.dataframe(df)
    else:
        st.warning("No records found")