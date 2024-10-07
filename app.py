import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Judul aplikasi
st.title('Streamlit Simple App')

# Menambahkan navigasi di sidebar
page = st.sidebar.radio("Pilih halaman", ["Dataset", "Visualisasi"])  # Tambahkan Dataset di sini

if page == "Dataset":
    st.header("Halaman Dataset")

    # Baca file CSV
    data = pd.read_csv("pddikti_example.csv.csv")  # Pastikan nama file benar

    # Tampilkan data di Streamlit
    st.write(data)

elif page == "Visualisasi":  
    st.header("Halaman Visualisasi")

    # Baca file CSV
    data = pd.read_csv("pddikti_example.csv.csv")  # Pastikan nama file benar

    # Filter berdasarkan universitas
    selected_university = st.selectbox('Pilih Universitas', data['universitas'].unique())
    filtered_data = data[data['universitas'] == selected_university]

    # Tampilkan filtered data untuk cek
    st.write(filtered_data)

    # Buat figure dan axis baru
    if not filtered_data.empty:
        plt.figure(figsize=(12, 6))

        for prog_studi in filtered_data['program_studi'].unique():
            subset = filtered_data[filtered_data['program_studi'] == prog_studi]
            subset = subset.sort_values(by='semester', ascending=True)  # Sortir berdasarkan semester

            plt.plot(subset['semester'], subset['jumlah'], label=prog_studi)

        plt.title(f"Visualisasi Data untuk {selected_university}")
        plt.xlabel('Semester')
        plt.xticks(rotation=90)
        plt.ylabel('Jumlah')
        plt.legend()

        # Tampilkan figure di Streamlit
        st.pyplot()  # Menampilkan visualisasi
