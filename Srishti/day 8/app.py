import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image
import zipfile
import os

# ----------------------------
# Extract model from ZIP
# ----------------------------
if not os.path.exists("flower_model.h5"):

    with zipfile.ZipFile("flower_model.zip", "r") as zip_ref:
        zip_ref.extractall()

# ----------------------------
# Load model
# ----------------------------
model = tf.keras.models.load_model("flower_model.h5")

# Class labels
class_names = ['daisy', 'dandelion', 'rose', 'sunflower', 'tulip']

# Page config
st.set_page_config(
    page_title="Flower Classification",
    page_icon="🌸",
    layout="centered"
)

# Title
st.title("🌸 Flower Classification App")

st.write("Upload a flower image and the model will predict its class.")

# Upload image
uploaded_file = st.file_uploader(
    "Choose a flower image",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file is not None:

    # Open image
    image = Image.open(uploaded_file).convert("RGB")

    # Show image
    st.image(image, caption="Uploaded Image", use_container_width=True)

    # Resize
    image = image.resize((150, 150))

    # Convert to array
    img_array = np.array(image)

    # Normalize
    img_array = img_array / 255.0

    # Add batch dimension
    img_array = np.expand_dims(img_array, axis=0)

    # Predict
    prediction = model.predict(img_array)

    predicted_class = class_names[np.argmax(prediction)]
    confidence = np.max(prediction) * 100

    # Output
    st.subheader("Prediction Result")
    st.success(f"Predicted Flower: {predicted_class}")
    st.info(f"Confidence: {confidence:.2f}%")