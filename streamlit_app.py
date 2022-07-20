import streamlit as st
from st_functions import st_button, load_css
from PIL import Image

load_css()

col1, col2, col3 = st.columns(3)
col2.image(Image.open('dp.png'))

st.header('Sachin Mishra, BE.')

st.info('Data Scientist at Data Society, Content Creator and ex-TCSer')

icon_size = 20

st_button('youtube', 'https://www.youtube.com/c/TKWTK/', 'Sachin Mishra YouTube channel', icon_size)
st_button('twitter', 'https://twitter.com/sachin19566/', 'Follow me on Twitter', icon_size)
st_button('linkedin', 'https://www.linkedin.com/in/sachin-mishra19566/', 'Follow me on LinkedIn', icon_size)

