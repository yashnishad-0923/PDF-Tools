# utils/compresser.py
import streamlit as st
from PyPDF2 import PdfReader, PdfWriter
from io import BytesIO

def compress_pdf():
    st.header("🔽 Compress PDF")

    uploaded_file = st.file_uploader("Upload PDF to compress", type="pdf")

    if uploaded_file and st.button("Compress PDF"):
        try:
            reader = PdfReader(uploaded_file)
            writer = PdfWriter()

            for page in reader.pages:
                try:
                    page.compress_content_streams() 
                except:
                    pass
                writer.add_page(page)

            output = BytesIO()
            writer.write(output)
            output.seek(0)

            original_size = len(uploaded_file.getvalue()) / 1024  
            compressed_size = len(output.getvalue()) / 1024
            reduction = original_size - compressed_size

            st.success(f"✅ Compression Complete\n\nOriginal: {original_size:.2f} KB\nCompressed: {compressed_size:.2f} KB\nReduced By: {reduction:.2f} KB")

            st.download_button(
                label="Download Compressed PDF",
                data=output,
                file_name="compressed.pdf",
                mime="application/pdf"
            )
        except Exception as e:
            st.error(f"❌ Compression failed:\n{e}")
