import streamlit as st
import qrcode
from PIL import Image

def generate_qr(data):
    qr = qrcode.make(data)
    qr.save("qrcode.png")
    return "qrcode.png"

st.title("QR Code Generator")
user_input = st.text_input("Enter text or URL:")
if user_input:
    img_path = generate_qr(user_input)
    st.image(Image.open(img_path), caption="Your QR Code")
