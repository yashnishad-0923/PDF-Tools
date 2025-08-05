# utils/encrypt.py
import streamlit as st
from PyPDF2 import PdfReader, PdfWriter
from io import BytesIO

def encrypt_pdf():
    st.header("🔒 Encrypt PDF")

    uploaded_file = st.file_uploader("Upload PDF to encrypt", type="pdf")
    password = st.text_input("Set a password for the PDF", type="password")

    if uploaded_file and password and st.button("Encrypt PDF"):
        try:
            reader = PdfReader(uploaded_file)
            writer = PdfWriter()

            for page in reader.pages:
                writer.add_page(page)

            writer.encrypt(password)

            output = BytesIO()
            writer.write(output)
            output.seek(0)

            st.success("✅ PDF Encrypted Successfully!")

            st.download_button(
                label="Download Encrypted PDF",
                data=output,
                file_name="encrypted.pdf",
                mime="application/pdf"
            )

        except Exception as e:
            st.error(f"❌ Failed to encrypt PDF:\n{e}")
    elif uploaded_file and not password:
        st.warning("⚠️ Please enter a password to encrypt the PDF.")
