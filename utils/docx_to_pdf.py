# utils/docx_to_pdf.py
import streamlit as st
from docx2pdf import convert
import os
import tempfile
from pathlib import Path

def convert_docx_to_pdf():
    st.header("🔁 Convert DOCX to PDF")

    uploaded_files = st.file_uploader(
        "Upload DOCX file(s)", 
        type="docx", 
        accept_multiple_files=True
    )

    if uploaded_files and st.button("Convert to PDF"):
        try:
            with tempfile.TemporaryDirectory() as temp_dir:
                temp_dir = Path(temp_dir)
                output_files = []

                for file in uploaded_files:
                    input_path = temp_dir / file.name
                    output_path = temp_dir / (file.name.replace(".docx", ".pdf"))

                   
                    with open(input_path, "wb") as f:
                        f.write(file.getbuffer())

                    
                    convert(str(input_path), str(output_path))

                   
                    with open(output_path, "rb") as f:
                        output_files.append((file.name.replace(".docx", ".pdf"), f.read()))

                st.success(f"✅ {len(output_files)} file(s) converted successfully!")

                for filename, data in output_files:
                    st.download_button(
                        label=f"Download {filename}",
                        data=data,
                        file_name=filename,
                        mime="application/pdf"
                    )

        except Exception as e:
            st.error(f"❌ Conversion failed:\n{e}")
