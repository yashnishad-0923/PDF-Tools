# utils/img_to_pdf.py
import streamlit as st
from PIL import Image
from io import BytesIO

def images_to_pdf():
    st.header("🖼️ Convert Images to PDF")

    uploaded_images = st.file_uploader(
        "Upload image files (.jpg, .jpeg, .png)", 
        type=["jpg", "jpeg", "png"], 
        accept_multiple_files=True
    )

    if uploaded_images and st.button("Convert to PDF"):
        try:
            image_objs = []

            for file in uploaded_images:
                img = Image.open(file).convert("RGB")
                image_objs.append(img)

            if not image_objs:
                st.error("❌ No valid images selected.")
                return

            output = BytesIO()
            image_objs[0].save(output, save_all=True, append_images=image_objs[1:], format="PDF")
            output.seek(0)

            st.success("✅ Images successfully converted to PDF!")

            st.download_button(
                label="Download PDF",
                data=output,
                file_name="images_to_pdf.pdf",
                mime="application/pdf"
            )

        except Exception as e:
            st.error(f"❌ Failed to convert images:\n{e}")
