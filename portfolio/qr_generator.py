import streamlit as st
import qrcode

def generate_qr(data, filename):
    img = qrcode.make(data)
    img.save(filename)
    with open(filename, "rb") as f:
        st.download_button("Download Portfolio QR Code", f, file_name=filename)