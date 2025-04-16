import streamlit as st
from PyPDF2 import PdfReader, PdfWriter
import tempfile
import os

def compress_pdf(input_file, output_path):
    reader = PdfReader(input_file)
    writer = PdfWriter()

    for page in reader.pages:
        writer.add_page(page)

    writer.add_metadata(reader.metadata)

    with open(output_path, "wb") as f:
        writer.write(f)

    return output_path

st.set_page_config(page_title="PDF Compressor", layout="centered")

st.title("📄 PDF Compressor mas ferdian")
st.write("Upload PDF untuk diperkecil ukurannya, ukuran PDF lo bukan yang lain")

uploaded_file = st.file_uploader("Pilih PDF", type=["pdf"])

if uploaded_file is not None:
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as temp_input:
        temp_input.write(uploaded_file.read())
        temp_input_path = temp_input.name

    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as temp_output:
        compressed_path = compress_pdf(temp_input_path, temp_output.name)

    with open(compressed_path, "rb") as f:
        st.download_button(
            label="⬇️ Download PDF Terkompres",
            data=f,
            file_name="compressed.pdf",
            mime="application/pdf"
        )

    # Info ukuran
    original_size = os.path.getsize(temp_input_path) / 1024
    compressed_size = os.path.getsize(compressed_path) / 1024
    st.info(f"Ukuran awal: {original_size:.2f} KB | Setelah dikompres: {compressed_size:.2f} KB")
