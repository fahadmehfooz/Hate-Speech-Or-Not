#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
import base64

# Function to set the background image
def set_bg_image(bg_image):
    with open(bg_image, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode()
    bg_image_css = f"""
    <style>
    .stApp {{
        background-image: url("data:image/jpeg;base64,{encoded_string}");
        background-size: cover;
    }}
    </style>
    """
    st.markdown(bg_image_css, unsafe_allow_html=True)

# Function to set custom styles
def set_custom_styles():
    custom_css = """
    <style>
    h1 {
        color: black !important;
    }
    </style>
    """
    st.markdown(custom_css, unsafe_allow_html=True)

# Set custom styles
set_custom_styles()

# Set the background image
set_bg_image('hate_speech.webp')

# Load the model and vectorizer
model = pickle.load(open('GBM_tuned.pkl', 'rb'))
vectorizer = pickle.load(open('tfidf_vectorizer.pkl', 'rb'))

# Title of the webpage
st.title("Hate Speech or Not?")
message = st.text_area("Enter Text", "Enter your text ...")
# Predict button
# Predict button
if st.button('Predict'):
    data = [message]
    vectorized_data = vectorizer.transform(data)
    prediction = model.predict(vectorized_data)

    # Display a user-friendly prediction with custom style
    if prediction[0] == 0:
       st.markdown("<p style='color: black; font-size: 20px;'>The given text is not a hate speech.</p>", unsafe_allow_html=True)
    else:
        st.markdown("<p style='color: black; font-size: 20px;'>The given text is a hate speech.</p>", unsafe_allow_html=True)
