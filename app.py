import joblib
import streamlit as st
import pandas as pd

model = joblib.load('Daegu_Apartment_XGB')

st.image("WLA25-Daegu-LB-01-565x403.jpg", use_container_width=True)

st.title("🧮Prediksi Harga Apartemen Daegu")

st.subheader('Masukkan Detail Data Properti :')

hallway = st.selectbox("Tipe Hallway", ['terraced', 'mixed', 'corridor'])
time_to_subway = st.selectbox("Waktu ke Subway", ['0-5min', '5min-10min', '10min-15min', '15min-20min'])
station = st.selectbox("Stasiun Subway", [
    'Kyungbuk_uni_hospital', 'Chil_sung_market', 'Bangoge', 'Sin_nam','Banwoldang', 'no_subway_nearby', 'Myung_duk', 'Daegu'
]) 

facilities_etc = st.number_input("Jumlah Fasilitas Sekitar (ETC)", 0, 10, 1)
public_office = st.number_input("Jumlah Kantor Pemerintah Sekitar", 0, 10, 3)
university = st.number_input("Jumlah Universitas Sekitar", 0, 10, 1)
parking = st.number_input("Jumlah Parkir Basement", 0, 5000, 100)
year = st.number_input("Tahun Dibangun", 1960, 2025, 2000)
in_apt = st.number_input("Jumlah Fasilitas Dalam Apartemen", 0, 20, 5)
size = st.number_input("Ukuran Apartemen (sqf)", 100, 3000, 1000)

input_df = pd.DataFrame({
    'HallwayType': [hallway],
    'TimeToSubway': [time_to_subway],
    'SubwayStation': [station],
    'N_FacilitiesNearBy(ETC)': [facilities_etc],
    'N_FacilitiesNearBy(PublicOffice)': [public_office],
    'N_SchoolNearBy(University)': [university],
    'N_Parkinglot(Basement)': [parking],
    'YearBuilt': [year],
    'N_FacilitiesInApt': [in_apt],
    'Size(sqf)': [size]
})

# Prediksi
if st.button("Prediksi Harga"):
    price = model.predict(input_df)[0]
    st.success(f"💰 Prediksi Harga Apartemen: ₩ {price:,.0f}")

