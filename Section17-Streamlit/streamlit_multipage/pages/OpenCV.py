import cv2
import streamlit as st
from streamlit_cropper import st_cropper
from PIL import Image
import numpy as np

st.title("OpenCV Image Processing")

# File uploader
uploaded_file = st.file_uploader("Choose an image...", type=['png', 'jpg', 'jpeg'])

if uploaded_file is not None:
    # Convert uploaded file to opencv format
    file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
    img = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)
    
    # Display original image
    st.subheader("Original Image")
    st.image(cv2.cvtColor(img, cv2.COLOR_BGR2RGB), use_container_width=True)
    
    # Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)    
    # Display grayscale image
    st.subheader("Grayscale Image")
    st.image(gray, use_container_width=True)

    img_brightness = cv2.convertScaleAbs(img, alpha=1, beta=50)
    # Display brightened image
    st.subheader("Brightened Image")
    st.image(cv2.cvtColor(img_brightness, cv2.COLOR_BGR2RGB), use_container_width=True)
    
else:
    st.info("Please upload an image file to get started")

st.title("Corta Imagem")

img_file = st.sidebar.file_uploader(label="Envie uma Imagem para cortar", type=['png', 'jpg'])
realtime_update = st.sidebar.checkbox("Atualização em Tempo Real", value=True)
box_color = st.sidebar.color_picker(label="Grupo de Cores", value="#0000FF")
aspect_choice = st.sidebar.radio(label="Proporção da Tela", options=["1:1", "16:9", "4:3"])

aspect_dict = {
    "1:1": (1, 1),
    "16:9": (16, 9),
    "4:3": (4, 3),
}

aspect_ratio = aspect_dict[aspect_choice]

if img_file:
    img = Image.open(img_file)
    cropped_img = st_cropper(
        img,
        realtime_update=realtime_update,
        box_color=box_color,
        aspect_ratio=aspect_ratio
    )
    st.subheader("Imagem Recortada")
    st.image(cropped_img, use_container_width=True)
