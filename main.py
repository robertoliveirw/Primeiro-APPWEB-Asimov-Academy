import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(layout='wide')

df_reviews = pd.read_csv("datasets/customer reviews.csv")
df_to100_books = pd.read_csv("datasets/Top-100 Trending Books.csv")
# Filtrando o valor
price_max = df_to100_books['book price'].max()
price_min = df_to100_books['book price'].min() 
#Side bar do valor
max_price = st.sidebar.slider('Price Range', price_min, price_max, price_max)
df_books = df_to100_books[df_to100_books['book price'] <= max_price]
df_books
#Histograma
fig = px.bar(df_books['year of publication'].value_counts())
st.plotly_chart(fig)