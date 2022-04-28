import streamlit as st
st.set_page_config(layout='wide')

from streamlit_option_menu import option_menu
from scripts.utilities import *
from scripts.home import *
from scripts.explorer import * 
from scripts.cost_burdened import * 
from scripts.about_data import *
    

with st.sidebar:
    selected = option_menu(
        menu_title = None,
        options = ['Home', 'Data Explorer', 'Cost Burdened Analysis', 'About the Data']
    )

if selected == 'Home':
    home()
if selected == 'Data Explorer':
    explorer()
if selected == 'Cost Burdened Analysis':
    cost_burdened() #in progress
if selected ==  'About the Data':
    about_data()
