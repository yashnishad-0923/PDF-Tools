import streamlit as st
from utils.merger import merge_pdfs
from utils.compresser import compress_pdf
from utils.encrypt import encrypt_pdf
from utils.page_extractor import extract_pages
from utils.img_to_pdf import images_to_pdf
from utils.docx_to_pdf import convert_docx_to_pdf

st.set_page_config(page_title="PDF Tools", layout="centered")
st.title("📚 PDF Tools")
st.markdown("Choose a tool from the sidebar to get started.")

tool = st.sidebar.radio("🧰 Select Tool", [
    "📎 Merge PDFs",
    "🔽 Compress PDF",
    "🔒 Encrypt PDF",
    "🧩 Extract Pages",
    "🖼️ Images to PDF",
    "🔁 DOCX to PDF"
])

if tool == "📎 Merge PDFs":
    merge_pdfs()

elif tool == "🔽 Compress PDF":
    compress_pdf()

elif tool == "🔒 Encrypt PDF":
    encrypt_pdf()

elif tool == "🧩 Extract Pages":
    extract_pages()

elif tool == "🖼️ Images to PDF":
    images_to_pdf()

elif tool == "🔁 DOCX to PDF":
    convert_docx_to_pdf()
