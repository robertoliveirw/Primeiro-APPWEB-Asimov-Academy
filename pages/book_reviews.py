import streamlit as st
import pandas as pd

st.set_page_config(layout='wide')

df_reviews = pd.read_csv("datasets/customer reviews.csv")
df_to100_books = pd.read_csv("datasets/Top-100 Trending Books.csv")

books = df_to100_books['book title'].unique()
book = st.sidebar.selectbox('Books', books)

df_book = df_to100_books[df_to100_books['book title'] == book]
df_reviews_f = df_reviews[df_reviews['book name'] == book]

df_book
df_reviews_f