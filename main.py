import streamlit as st
import numpy as np
import pandas as pd
import tensorflow as tf
from PIL import Image
from io import BytesIO

# Load the model
model = tf.keras.models.load_model('path_to_your_model.h5')

st.title('Handwritten Digit Recognition')

# Define a function for image preprocessing
def preprocess_image(image):
    image = image.convert('L')  # Convert to grayscale
    image = image.resize((28, 28))  # Resize to model input shape
    image = np.array(image) / 255.0  # Normalize to [0, 1]
    return image.reshape(1, 28, 28, 1)

# Create tabs for different functionalities
tab1, tab2 = st.tabs(['Upload Image', 'Draw Digit'])

with tab1:
    st.header('Upload Image')
    uploaded_file = st.file_uploader('Choose an image...', type=['png', 'jpg', 'jpeg'])
    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption='Uploaded Image', use_column_width=True)
        # Preprocess the image
        processed_image = preprocess_image(image)
        # Make a prediction
        prediction = model.predict(processed_image)
        predicted_class = np.argmax(prediction)
        confidence_score = np.max(prediction)
        st.write(f'Prediction: {predicted_class} with confidence: {confidence_score:.2f}')
        
with tab2:
    st.header('Draw Digit')
    from streamlit_canvas import st_canvas
    canvas_result = st_canvas(
        fill_color='rgba(255, 255, 255, 0)',
        background_color='rgba(255, 255, 255, 1)',
        stroke_color='rgba(0, 0, 0, 1)',
        stroke_width=10,
        display_toolbar=True,
        height=280,
        width=280,
        drawing_mode='freedraw',
        key='canvas'
    )
    if canvas_result.image_data is not None:
        # Convert to PIL image
        image = Image.fromarray(canvas_result.image_data.astype('uint8'), 'RGB')
        st.image(image, caption='Drawn Image', use_column_width=True)
        # Preprocess the image
        processed_image = preprocess_image(image)
        # Make a prediction
        prediction = model.predict(processed_image)
        predicted_class = np.argmax(prediction)
        confidence_score = np.max(prediction)
        st.write(f'Prediction: {predicted_class} with confidence: {confidence_score:.2f}')
        st.write('Prediction probabilities:')
        st.bar_chart(prediction[0])

# Error handling
st.warning('Ensure to upload a 28x28 image or draw a digit for accurate predictions.')