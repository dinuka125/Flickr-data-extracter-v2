import streamlit as st
import datetime
from scrap import scrapy


st.set_page_config(page_title="Flickr Data Extractor", page_icon=":smiley:", layout="wide")
with st.container():
    st.header("Flickr Data Extractor")
    st.subheader("Search..." + ":smiley:")
    search_keyword = st.text_input('Search term to extract data')

with st.sidebar:
    st.subheader('Select Date Range')
    max_date = st.date_input(
        "Max Date",max_value=datetime.datetime.today()
        )
    min_date = st.date_input(
        "Min Date",max_value=datetime.datetime.today()
        )

clicked = st.button("Search...", on_click=scrapy, args=(search_keyword,max_date,min_date))
