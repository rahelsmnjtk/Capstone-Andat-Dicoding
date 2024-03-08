# Import Library
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import seaborn as sns
import matplotlib.pyplot as plt

# LOAD DATA
data = pd.read_csv("https://raw.githubusercontent.com/rahelsmnjtk/Capstone-Analitika-Data-Dicoding/main/hour.csv")
day_df = day_df = pd.read_csv("https://raw.githubusercontent.com/rahelsmnjtk/Capstone-Analitika-Data-Dicoding/main/day.csv")
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

#Pengaruh cuaca terhadap jumlah sewa
st.subheader("Pengaruh cuaca terhadap jumlah sewa")
# Filter data for year 0
weather_cnt = day_df[day_df['yr'] == 0]
fig_temp_chart = px.bar(weather_cnt, x="weathersit", y="cnt",
                            title="Jumlah Sewa Sepeda berdasarkan Cuaca", color="weathersit")
st.plotly_chart(fig_temp_chart, use_container_width=True,
                height=500, width=1000)
st.markdown('**Weather Situation:**')
st.markdown('1: Clear, Few clouds, Partly cloudy, Partly cloudy')
st.markdown('2: Mist + Cloudy, Mist + Broken clouds, Mist + Few clouds, Mist')
st.markdown('3: Light Snow, Light Rain + Thunderstorm + Scattered clouds, Light Rain + Scattered clouds')
st.markdown('4: Heavy Rain + Ice Pallets + Thunderstorm + Mist, Snow + Fog')
with st.expander("See explanation"):
    st.write(
    """
    Dari grafik yang ditampilkan, dapat dilihat bahwa 
    cuaca memberikan pengaruh yang signifikan terhadap jumlah sewa sepeda 
    pada tahun 2011. Terlihat bahwa cuaca yang baik seperti cerah, 
    agak berawan (weathersit = 1) akan membuat orang lebih tertarik 
    untuk melakukan sewa sepeda.

    Analisis ini menunjukkan bahwa kondisi cuaca dapat menjadi faktor 
    yang harus diperhatikan para penyedia layanan sewa sepeda karena 
    dapat memengaruhi jumlah permintaan sewa. Hal-hal seperti stok 
    sepeda yang harus disediakan, biaya sewa, atau teknik pemasaran 
    harus diperhatikan dan disesuaikan dengan kondisi cuaca.
    """
    )

#Orang yang menggunakan sewa sepeda pada hari kerja selama musim gugur
st.subheader("Jumlah pengguna sewa sepeda pada hari kerja selama musim gugur")

# Filter DataFrame for workdays during the fall season
workday = day_df[(day_df["workingday"] == 1)]
fig_temp_chart = px.bar(workday, x="season", y="cnt",
                            title="Jumlah Sewa Sepeda berdasarkan Musim pada Hari Kerja", color="season")
st.plotly_chart(fig_temp_chart, use_container_width=True,
                height=500, width=1000)

workday_fall = day_df[(day_df["workingday"] == 1) & (day_df["season"] == 3)]
# Calculate the total number of bike rentals
count_total = workday_fall["cnt"].sum()
    
# Display the result
st.write("Total number of bike rentals on workdays during the fall season:", count_total)

with st.expander("See explanation"):
    st.write(
    """Sewa sepeda pada hari kerja selama musim gugur mencapai 749.073. 
    Hal ini menunjukkan bahwa bisnis sewa sepeda pada musim gugur 
    merupakan potensi bisnis yang kuat. Sehingga, penyedia layanan sewa sepeda
    harus tanggap dan dapat memanfaatkan informasi ini untuk
    melakukan persiapan seperti jumlah sepeda yang harus disiapkan, dan lainnya pada hari kerja
    saat musim gugur."""
    )

#Distribusi per jam untuk sewa sepeda bagi orang casual pada hari libur tahun 2012.
st.subheader("Distribusi per jam untuk sewa sepeda bagi pengguna casual pada hari libur tahun 2012.")

# Filter DataFrame for workdays during the fall season
holiday_2012 = data[(data["yr"] == 1)]
fig_temp_chart = px.bar(holiday_2012, x="holiday", y="cnt",
                            title="Jumlah Sewa Sepeda tahun 2012", color="holiday")
st.plotly_chart(fig_temp_chart, use_container_width=True,
                height=500, width=1000)

holiday_2012 = data[(data["yr"] == 1) & (data["holiday"] == 1)]
# Calculate the total number of bike rentals
dist_per_hour = holiday_2012.groupby("hr")["casual"].sum()
    
# Display the result
st.write("Distribution of bike rentals for casual per hour on holidays in 2012:")
st.write(dist_per_hour)

with st.expander("See explanation"):
    st.write(
    """Dari hasil yang ditampilkan, terlihat bahwa pada hari libur  
    tahun 2012, pengguna casual banyak menggunakan sewa sepeda di 
    siang sampai ke sore hari, yaitu dimulai dari sekitar jam 11 siang 
    sampai jam 4 sore, dimana puncaknya berada di jam 1 siang yang 
    mencapai 1245 sewa. Hal ini dapat menjadi pertimbangan para penyedia 
    layanan sewa sepeda pada tahun-tahun berikutnya, dimana mungkin 
    mereka dapat menentukan berapa jumlah sepeda yang harus disediakan 
    pada jam-jam ramai tersebut."""
    )

#Cara meningkatkan sewa sepeda bagi pengguna terdaftar pada hari kerja
st.subheader('Jumlah Sewa Sepeda Pengguna Terdaftar Pada Hari Kerja')
    
# Filter data for workdays
workday = day_df[(day_df["workingday"] == 1) & (day_df['registered']>0)]
    
# Group by weekday and sum the number of registered rentals
data = workday.groupby('weekday')['registered'].sum().reset_index()
    
# Create a bar plot
fig, ax = plt.subplots()
sns.barplot(x='weekday', y='registered', data=data, ax=ax)
ax.set_xlabel('Weekday')
ax.set_ylabel('Registered Bike Rentals')
ax.set_title('Jumlah Sewa Sepeda Pengguna Terdaftar Pada Hari Kerja')
    
# Display the plot in Streamlit
st.pyplot(fig)


with st.expander("See explanation"):
    st.write(
    """
    Beberapa cara yang dapat dilakukan untuk meningkatkan sewa sepeda bagi pengguna terdaftar :\n
    1. Memberikan promosi bagi pengguna terdaftar pada hari-hari yang jumlah sewanya sedikit, seperti hari senin.\n
    2. Memberikan poin atau penghargaan setiap kali menggunakan layanan sewa pada hari kerja, dimana poin tersebut dapat ditukar menjadi diskon pada penggunaan selanjutnya.\n
    3. Melakukan komunikasi langsung dengan pengguna terdaftar seperti melakukan penawaran melalui emai, pesan teks, atau yang lainnya.\n
    4. Menyediakan stasiun penyewaan sepeda yang mudah diakses di lokasi strategis dan memastikan kondisi sepeda ada dalam keadaan baik pada hari kerja.
    """
    )

# Show data source and description
st.sidebar.title("About")
st.sidebar.info("Dashboard ini menampilkan visualisasi dari dataset Bike Share. Dataset Bike Share memuat beberapa variabel seperti season, weather situation, humidity, windspeed, dan lainnya. ")