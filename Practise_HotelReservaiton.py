import streamlit as st
import pandas as pd
from matplotlib import image
import plotly.express as px

st.title(":red[Hotel Reservation Dataset.]")

img = image.imread(r"C:\Users\user\internship\resources\images\hotel_reservation_img.jpg")
st.image(img)

df = pd.read_csv(r"C:\Users\user\internship\resources\data\Hotel Reservations.csv")
st.dataframe(df)

status = st.selectbox("Select the Species:", df['booking_status'].unique())

fig_1 = px.histogram(df[df['booking_status'] == status], x="avg_price_per_room")
st.plotly_chart(fig_1, use_container_width=True)

fig_2 = px.box(df[df['booking_status'] == status], x="market_segment_type")
st.plotly_chart(fig_2, use_container_width=True)

fig_3 = px.line(df[df['booking_status'] == status] , y="no_of_week_nights")
st.plotly_chart(fig_3, use_container_width=True)

fig_3 = px.bar(df[df['booking_status'] == status] , x="type_of_meal_plan")
st.plotly_chart(fig_3, use_container_width=True)

