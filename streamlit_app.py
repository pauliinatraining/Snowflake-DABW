import streamlit as st
import pandas as pd
import requests

my_fruit_list = pd.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")

# Display:

st.title('Mom and Pop\'s New Healthy Diner')
st.header('Breakfast Favorites')
st.text('🥣 Omega 3 & Blueberry Oatmeal')
st.text('🥗 Kale, Spinach & Rocket Smoothie')
st.text('🐔 Hard-Boiled Free-Range Egg')
st.text('🥑🍞 Avocado Toast')

st.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

# Picklist to choose fruit
fruits_selected = st.multiselect("Pick your fruits:", list(my_fruit_list.index),['Apple','Orange'])
fruits_to_show = my_fruit_list.loc[fruits_selected]

#Display the fruits table
st.dataframe(fruits_to_show)

st.text(fruityvice_respose)
