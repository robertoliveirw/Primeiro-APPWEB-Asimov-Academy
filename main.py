import streamlit as st
import pandas as pd
import plotly as pt

st.set_page_config(layout='wide')


df_reviews = pd.read_csv("datasets/customer reviews.csv")
df_to100_books = pd.read_csv("datasets/Top-100 Trending Books.csv")

df_reviews
df_to100_books