import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import streamlit as st
import seaborn as sns

#INPUT DATA
day_df = pd.read_csv('https://raw.githubusercontent.com/theresiaa13/tugasdicoding/main/dashboard/daysepeda.csv')
hour_df = pd.read_csv('https://raw.githubusercontent.com/theresiaa13/tugasdicoding/main/dashboard/hoursepeda.csv')

#EDA
#EXPLORE DATA DAY_DF
#MENGHITUNG JUMLAH PENYEWA SEPEDA BERDASARKAN KATEGORI WEATHERSIT (CUACA) DARI DATASET DAY_DF
day_df.groupby(by="weathersit").agg({
    'dteday':'nunique',
    'cnt':'sum'
})
#MENGHITUNG MEAN DAN STANDAR DEVIASI JUMLAH PENYEWA SEPEDA BERDASARKAN KATEGORI WEATHERSIT (CUACA) DARI DATASET DAY_DF
day_df.groupby(by="weathersit").agg({
    "cnt": ["mean","std"]
})

#EXPLORE DATA HOUR_DF
#MENGHITUNG DAN MENGURUTKAN JUMLAH PENYEWA SEPEDA BERDASARKAN JAM PADA DATASET HOUR_DF
hour_group = hour_df.groupby(by='hr').agg({
    'dteday':'nunique',
    'cnt':'sum'
})
sorting_hour_group = hour_group.sort_values(by='cnt', ascending=False)
print(sorting_hour_group)


st.header('Proyek Analisis Data Dashboard :smile:')

with st.sidebar:
    # Menambahkan gambar
    st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR3MtOqYzI07wRaLmXQ6hTWGmZKZto9lOtCzA&usqp=CAU")
    st.subheader("Theresia as student at Bangkit Academy")
    st.write("Hasil Analisis data menggunakan Bike Sharing Dataset")
tab1, tab2 = st.tabs(["Tab 1","Tab 2"])

with tab1 :
    st.title("Jumlah Penyewa Sepeda Berdasarkan Cuaca")
    #Gambar
    pict_bar_one, ax = plt.subplots(figsize=(21, 7))
    sns.barplot(x="weathersit", y="cnt", data=day_df)
    ax.set_xlabel("Cuaca")
    ax.set_ylabel("Jumlah penyewa")
    ax.set_title("Jumlah Penyewa Sepeda Berdasarkan Cuaca", loc="center", fontsize=15)
    plt.show()

    #Penjelasan
    st.pyplot(pict_bar_one)
    with st.expander("Hasil Analisa"):
        st.write("Berdasarkan hasil analisa diagram diatas, didapatkan hasil bahwa sepeda digunakan oleh penyewa paling banyak adalah saat cuaca nomor 1 (Clear, Few clouds, Partly cloudy, Partly cloudy) dengan 2257952 penyewa dan paling sedikit saat cuaca nomor 3 (Light Snow, Light Rain + Thunderstorm + Scattered clouds, Light Rain + Scattered clouds) dengan 37869 penyewa. Dari analisa data ini, perusahaan penyedia layanan dapat menyediakan jumlah sepeda lebih banyak ketika sedang cuaca nomor 1 dan dapat melakukan perbaikan saat cuaca nomor 3.")

with tab2:
    st.title("Jumlah Penyewa Sepeda Berdasarkan Jam")
   #Gambar
    pict_bar_two, ax = plt.subplots(figsize=(21, 7))
    sns.barplot(x="hr", y="cnt", data=sorting_hour_group)
    ax.set_xlabel("Jam")
    ax.set_ylabel("Jumlah Pengguna")
    ax.set_title("Jumlah Penyewa Sepeda Berdasarkan Jam", loc="center", fontsize=15)
    plt.show()

    #Penjelasan
    st.pyplot(pict_bar_two)
    with st.expander("Hasil Analisa Penjelasan"):
        st.write("Berdasarkan hasil analisa diagram diatas, didapatkan hasil bahwa sepeda digunakan oleh penyewa paling banyak di jam 17.00 (336860 penyewa) dan paling sedikit di jam 04.00 (4428 penyewa). Dari analisa data ini, perusahaan penyedia layanan dapat menyediakan jumlah sepeda lebih dari biasanya ketika jam 17.00 dan dapat menguranginya saat jam 04.00.")