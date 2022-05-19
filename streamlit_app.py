import streamlit as st
import pandas as pd
import requests
import snowflake.connector
from urllib.error import ERLError

my_fruit_list = pd.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

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

# Display fruityvice api response
st.header('Fruityvice Fruit Advice!')
try:
  fruit_choice = st.text_input('What fruit would you like to learn about?')
  if not fruit_choice:
    st.error("Please select a fruit to get information.")
  else:
    fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)
    fruityvice_normalized = pd.json_normalize(fruityvice_response.json())
    st.dataframe(fruityvice_normalized)
    
except URLError as e:
  st.error()

st.stop()
#snowflake
my_cnx = snowflake.connector.connect(**st.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("select * from fruit_load_list")
my_data_rows = my_cur.fetchall()

st.header("The fruit load list contains:")
st.dataframe(my_data_rows)

# Allow end user to add a fruit to the list
add_my_fruit = st.text_input('What fruit would you like to add?')
st.write('Thanks for adding ' + add_my_fruit)

#Add fruit to snowflake
my_cur.execute("insert into fruit_load_list values ('from streamlit')")
