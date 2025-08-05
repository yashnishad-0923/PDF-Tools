# utils/merger.py
import streamlit as st
from PyPDF2 import PdfMerger
from io import BytesIO

def merge_pdfs():
    st.header("📎 Merge PDFs")
    uploaded_files = st.file_uploader("Upload PDF files to merge", type="pdf", accept_multiple_files=True)

    if uploaded_files:
        if st.button("Merge PDFs"):
            merger = PdfMerger()
            for file in uploaded_files:
                try:
                    merger.append(file)
                except Exception as e:
                    st.error(f"Error merging {file.name}: {e}")
                    return

            output_pdf = BytesIO()
            merger.write(output_pdf)
            merger.close()
            output_pdf.seek(0)

            st.success("✅ PDFs Merged Successfully!")
            st.download_button("Download Merged PDF", output_pdf, "merged_output.pdf", mime="application/pdf")
