# app.py
import streamlit as st
from PIL import Image
import numpy as np
from inference import predict

# Set page title and icon
st.set_page_config(page_title="Deepfake GAN Detector", page_icon="🔍")

# Define custom CSS styles for the app
st.markdown(
    """
    <style>
    body {
        background-color: #141414;
        color: #ffffff;
        font-family: Arial, sans-serif;
    }
    .container {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        height: 100vh;
    }
    .header {
        font-size: 48px;
        margin-bottom: 30px;
        text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.5);
    }
    .upload-btn {
        background-color: #5cb85c;
        color: #ffffff;
        padding: 15px 30px;
        border: none;
        border-radius: 50px;
        font-size: 24px;
        cursor: pointer;
        transition: background-color 0.3s;
    }
    .upload-btn:hover {
        background-color: #4cae4c;
    }
    .prediction {
        font-size: 36px;
        padding: 30px;
        border-radius: 10px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        background-color: #ffffff;
        color: #000000;
        text-align: center;
        animation: pulse 1s infinite alternate;
    }
    @keyframes pulse {
        0% {
            transform: scale(1);
        }
        100% {
            transform: scale(1.1);
        }
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Background image
st.markdown(
    """
    <style>
    .stApp {
        background-image: url('https://images.unsplash.com/photo-1542281286-9e0a16bb7366');
        background-size: cover;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Container for content
with st.container():
    # Header
    st.markdown("<h1 class='header'>Deepfake GAN Detector</h1>", unsafe_allow_html=True)

    # Description
    st.markdown(
        """
        <div style='margin-bottom: 30px;'>
        🔍 Detect deepfake images using GAN identification model. 
        Upload an image and click 'Detect' to see the result.
        </div>
        """,
        unsafe_allow_html=True,
    )

    # Upload image
    uploaded_file = st.file_uploader("Upload an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)
    st.write("")
    st.write("Classifying...")

    prediction = predict(image)
    if prediction[0][0] > 0.5:
        st.write(f"Prediction: Real")
    else:
        st.write(f"Prediction: Fake")
