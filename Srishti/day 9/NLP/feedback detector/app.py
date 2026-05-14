# app.py

import streamlit as st
import nltk
import string
from textblob import TextBlob
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# Download NLTK resources (only first time)
nltk.download('punkt')
nltk.download('stopwords')

# Streamlit Page Config
st.set_page_config(page_title="Restaurant Review Sentiment Analyzer")

# Title
st.title("🍽️ Restaurant Review Sentiment Analysis")

st.write("Enter a restaurant review and check whether the sentiment is Positive, Negative, or Neutral.")

# Text Input
user_review = st.text_area("Enter your review here:")

# Preprocessing Function
def preprocess_text(text):
    # Lowercase
    text = text.lower()

    # Remove punctuation
    text = text.translate(str.maketrans('', '', string.punctuation))

    # Tokenization
    tokens = word_tokenize(text)

    # Remove stopwords
    filtered = [word for word in tokens if word not in stopwords.words('english')]

    return filtered

# Predict Button
if st.button("Analyze Sentiment"):

    if user_review.strip() == "":
        st.warning("Please enter a review.")
    
    else:
        # Preprocessing
        processed_words = preprocess_text(user_review)

        # Sentiment Analysis
        analysis = TextBlob(user_review)
        polarity = analysis.sentiment.polarity

        # Display Processed Words
        st.subheader("Processed Words")
        st.write(processed_words)

        # Display Sentiment Score
        st.subheader("Sentiment Score")
        st.write(round(polarity, 2))

        # Classification
        st.subheader("Prediction")

        if polarity > 0:
            st.success("Positive 😊")
        elif polarity < 0:
            st.error("Negative 😡")
        else:
            st.info("Neutral 😐")