# utils/page_extractor.py
import streamlit as st
from PyPDF2 import PdfReader, PdfWriter
from io import BytesIO

def extract_pages():
    st.header("🧩 Extract Pages from PDF")

    uploaded_file = st.file_uploader("Upload PDF to extract pages from", type="pdf")
    page_range = st.text_input("Enter page range (e.g., 2-5)")

    if uploaded_file and page_range and st.button("Extract Pages"):
        try:
            reader = PdfReader(uploaded_file)
            total_pages = len(reader.pages)

           
            if "-" not in page_range:
                st.error("❌ Use the format start-end (e.g., 2-5).")
                return

            start, end = map(int, page_range.strip().split("-"))
            start -= 1
            end -= 1

            if start < 0 or end >= total_pages or start > end:
                st.error(f"❌ Invalid page range. PDF has {total_pages} pages.")
                return

            writer = PdfWriter()
            for i in range(start, end + 1):
                writer.add_page(reader.pages[i])

            output = BytesIO()
            writer.write(output)
            output.seek(0)

            st.success(f"✅ Pages {start+1} to {end+1} extracted!")

            st.download_button(
                label="Download Extracted PDF",
                data=output,
                file_name="extracted_pages.pdf",
                mime="application/pdf"
            )

        except Exception as e:
            st.error(f"❌ Error while extracting pages:\n{e}")
    elif uploaded_file and not page_range:
        st.warning("⚠️ Enter a valid page range like 1-3.")
