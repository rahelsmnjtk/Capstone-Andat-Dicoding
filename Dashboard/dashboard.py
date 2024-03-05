# Import Library
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# LOAD DATA
data = pd.read_csv("https://raw.githubusercontent.com/rahelsmnjtk/Capstone-Analitika-Data-Dicoding/main/hour.csv")

# Set page title
st.title("Bike Share Dashboard")

#Sidebar
with st.sidebar:
    st.sidebar.title("Bike Sharing Dashboard")
    st.sidebar.markdown("**Nama: Rahel Sari Tua Simanjuntak**")
    st.sidebar.markdown("**Email: [rahelsmnjtk18@gmail.com](rahelsmnjtk18@gmail.com)**")
    st.sidebar.markdown("**id Dicoding : rahelsmnjtk**")
# Show dataset source
st.sidebar.markdown("[Download Dataset](https://raw.githubusercontent.com/rahelsmnjtk/Capstone-Analitika-Data-Dicoding/main/hour.csv)")

# Fix the data type
# df_day
data["dteday"] = pd.to_datetime(data["dteday"])
# df_hour
data["dteday"] = pd.to_datetime(data["dteday"])

# VISUALIZATION
st.header("Dataset Bike Sharing")
st.write(data)

# create a layout with two columns
col1, col2 = st.columns(2)

with col1:
    # Season-wise bike share count
    # st.subheader("Season-wise Bike Share Count")
    # Mapping dari angka ke label musim
    season_count = data.groupby("season")["cnt"].sum().reset_index()
    fig_season_count = px.bar(season_count, x="season",
                              y="cnt", title="Season-wise Bike Share Count", color="season")
    st.plotly_chart(fig_season_count, use_container_width=True,
                    height=500, width=800)
    st.markdown('**Season :**')
    st.markdown("1 : Spring")
    st.markdown("2 : Summer")
    st.markdown("3 : Fall")
    st.markdown("4 : Winter")
with col2:
    # Weather situation-wise bike share count
    # st.subheader("Weather Situation-wise Bike Share Count")

    weather_count = data.groupby("weathersit")["cnt"].sum().reset_index()
    fig_weather_count = px.bar(weather_count, x="weathersit",
                               y="cnt", title="Weather Situation-wise Bike Share Count", color="weathersit")
    # Mengatur tinggi dan lebar gambar
    st.plotly_chart(fig_weather_count, use_container_width=True,height=500, width=800)
    st.markdown('**Weather Situation:**')
    st.markdown('1: Clear, Few clouds, Partly cloudy, Partly cloudy')
    st.markdown('2: Mist + Cloudy, Mist + Broken clouds, Mist + Few clouds, Mist')
    st.markdown('3: Light Snow, Light Rain + Thunderstorm + Scattered clouds, Light Rain + Scattered clouds')
    st.markdown('4: Heavy Rain + Ice Pallets + Thunderstorm + Mist, Snow + Fog')


# Hourly bike share count
st.subheader("Hourly Bike Share Count")
hourly_count = data.groupby("hr")["cnt"].sum().reset_index()
fig_hourly_count = px.line(
    hourly_count, x="hr", y="cnt", title="Hourly Bike Share Count")
st.plotly_chart(fig_hourly_count, use_container_width=True,
                height=500, width=1000)

# Humidity vs. Bike Share Count
st.subheader("Humidity vs. Bike Share Count")
fig_humidity_chart = px.scatter(
    data, x="hum", y="cnt", title="Humidity vs. Bike Share Count", color="hum")
st.plotly_chart(fig_humidity_chart)

# Wind Speed vs. Bike Share Count
st.subheader("Wind Speed vs. Bike Share Count")
fig_wind_speed_chart = px.scatter(
    data, x="windspeed", y="cnt", title="Wind Speed vs. Bike Share Count", color="windspeed")
st.plotly_chart(fig_wind_speed_chart)

# Temperature vs. Bike Share Count
st.subheader("Temperature vs. Bike Share Count")
fig_temp_chart = px.scatter(data, x="temp", y="cnt",
                            title="Temperature vs. Bike Share Count",color= "temp")
st.plotly_chart(fig_temp_chart, use_container_width=True,
                height=500, width=1000)

# Feeling Temperature vs. Bike Share Count
st.subheader("Feeling Temperature vs. Bike Share Count")
fig_temp_chart = px.scatter(data, x="atemp", y="cnt",
                            title="Feeling Temperature vs. Bike Share Count", color="atemp")
st.plotly_chart(fig_temp_chart, use_container_width=True,
                height=500, width=1000)


# Show data source and description
st.sidebar.title("About")
st.sidebar.info("Dashboard ini menampilkan visualisasi dari dataset Bike Share. Dataset Bike Share memuat beberapa variabel seperti season, weather situation, humidity, windspeed, dan lainnya.")