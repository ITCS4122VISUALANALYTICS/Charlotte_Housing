import streamlit as st
from streamlit_option_menu import option_menu
from scripts.utilities import *
from scripts.home import *
from scripts.explorer import * 
from scripts.cost_burdened import * 
    
with st.sidebar:
    selected = option_menu(
        menu_title = None,
        options = ['Home', 'Data Explorer', 'Cost Burdened Analysis', 'Affordability Analysis', 'Rent Analysis', 'About the Data']
    )

if selected == 'Home':
    home()
if selected == 'Data Explorer':
    explorer()
if selected == 'Cost Burdened Analysis':
    cost_burdened()
if selected ==  'Affordability Analysis':
    pass #in progress
if selected ==  'Rent Analysis':
    pass #in progress 
if selected ==  'About the Data':
    pass #in progress
