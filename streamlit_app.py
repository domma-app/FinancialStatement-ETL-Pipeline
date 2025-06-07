import streamlit as st
import os
import shutil

from utils.pdf_extractor.extract import extract_pdfs_from_folder
from utils.pdf_extractor.transform import transform_extracted_texts
from utils.pdf_extractor.load import load_texts

from utils.financial_statements.extract import get_financial_data
from utils.financial_statements.transform import prepare_data_for_saving
from utils.financial_statements.load import save_data_to_csv

from utils.predict.predictor import stock_purchase_recommendation

# Set Streamlit to use wide layout
st.set_page_config(layout="wide")

# === Header / Introduction ===
st.markdown(
    """
    ## 💼 Capstone Project - Dicoding x DBS Foundation 2025

    Halo, perkenalkan saya **Falah Mandira Irawan**, seorang Machine Learning Engineer Cohort dalam program **Coding Camp 2025**. Fitur ini adalah fitur yang saya kembangkan dalam **Capstone Project Coding Camp 2025** yang diselenggarakan oleh [Dicoding](https://www.dicoding.com/) dan didukung oleh **DBS Foundation**.

    🎯 **Tujuan dari aplikasi ini** adalah untuk membantu **investor pemula** dalam melakukan analisis sederhana terhadap laporan keuangan perusahaan, dan memberikan **rekomendasi kelayakan saham** secara otomatis berdasarkan data tersebut.

    Dengan hanya mengunggah file PDF laporan keuangan dari situs resmi seperti [IDX (Indonesia Stock Exchange)](https://www.idx.co.id/id/perusahaan-tercatat/laporan-keuangan-dan-tahunan/), aplikasi ini akan:
    
    - 📄 Mengekstraksi dan membersihkan teks dari laporan keuangan
    - 📊 Menyusun metrik keuangan utama
    - 🧠 Melakukan analisis berbasis machine learning
    - ✅ Memberikan rekomendasi sederhana berupa persentase kelayakan pembelian saham

    ---
    """,
    unsafe_allow_html=True
)

st.title("📥 Analisis Laporan Keuangan (PDF) + Rekomendasi Saham")

# === File uploader ===
st.markdown(
    """
    ### Unggah Laporan Keuangan
    Unggah satu atau lebih file PDF laporan keuangan tahunan atau per triwulan dari satu perusahaan.
    <br>
    Format file dapat dilihat sebagai referensi di [website resmi IDX](https://www.idx.co.id/id/perusahaan-tercatat/laporan-keuangan-dan-tahunan/) 🧾
    """,
    unsafe_allow_html=True
)

uploaded_files = st.file_uploader(
    "Upload file PDF yang ingin dianalisis:",
    type=["pdf"],
    accept_multiple_files=True
)

# === Run pipeline ===
if uploaded_files:
    if st.button("🚀 Jalankan Analisis"):
        def clean_up_folders(folders):
            try:
                for folder in folders:
                    if os.path.exists(folder):
                        for filename in os.listdir(folder):
                            file_path = os.path.join(folder, filename)
                            if os.path.isfile(file_path):
                                os.remove(file_path)
                            elif os.path.isdir(file_path):
                                shutil.rmtree(file_path)
                        print(f"Cleaned up: {folder}")
            except Exception as e:
                print(f"Error during cleanup: {e}")

        def run_pipeline_with_uploaded_files(uploaded_files):
            input_folder = "input"
            os.makedirs(input_folder, exist_ok=True)

            for uploaded_file in uploaded_files:
                file_path = os.path.join(input_folder, uploaded_file.name)
                with open(file_path, "wb") as f:
                    f.write(uploaded_file.read())

            st.info("📄 File PDF berhasil diupload dan disimpan!")

            st.write("🔍 Menjalankan ekstraksi teks dari PDF...")
            pdf_texts = extract_pdfs_from_folder(input_folder)

            st.write("🧹 Membersihkan teks hasil ekstraksi...")
            clean_texts = transform_extracted_texts(pdf_texts)

            st.write("💾 Menyimpan teks hasil transformasi...")
            saved_files = load_texts(clean_texts)

            st.write("📊 Mengekstraksi data keuangan dari teks...")
            all_financial_data = []
            for text in clean_texts.values():
                financial_data = get_financial_data(text)
                if financial_data:
                    all_financial_data.extend(financial_data)

            st.write("📈 Mempersiapkan data keuangan untuk disimpan...")
            prepared_data = prepare_data_for_saving(all_financial_data)

            st.write("🧾 Menyimpan data keuangan ke CSV...")
            saved_data = save_data_to_csv(prepared_data)

            if saved_data.empty:
                st.warning("⚠️ Tidak ada data keuangan yang tersedia untuk rekomendasi.")
                return

            st.write("💡 Menghasilkan persentase rekomendasi pembelian saham...")
            recommendation = stock_purchase_recommendation(saved_data)

            st.success("✅ Proses selesai!")
            st.subheader("Rekomendasi Pembelian Saham:")
            st.json(recommendation)

            st.write("🧹 Membersihkan folder output...")
            clean_up_folders(['input', 'output', 'datasets'])

        run_pipeline_with_uploaded_files(uploaded_files)

# === Footer ===
st.caption("Copyright \u00A9 2025 Falah Mandira Irawan. All rights reserved.")