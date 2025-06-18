import streamlit as st
import eda,prediction,home

st.set_page_config(page_title = "E-Commerce Transaction Data Center",
                   layout='centered',
                   initial_sidebar_state='expanded')

with st.sidebar:
    st.write('# Navigation')
    navigation = st.radio('Page', ['Home', 'Exploratory Data Analysis', 'Profit Prediction'])

if navigation == 'Exploratory Data Analysis':
    eda.eda()
elif navigation == 'Home':
    home.home()
else:
    prediction.run()