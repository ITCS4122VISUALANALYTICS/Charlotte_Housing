import streamlit as st
from scripts.utilities import *
from scripts.constants import *
from PIL import Image 

def home():
    image = Image.open('data_sets/flag.png')
    
    #new row
    rowi_spacer1, rowi_1, rowi_spacer2= st.columns(
        (.1, 3.2, .1)
    )
    with rowi_spacer1:
        st.write("")
    with rowi_1:
        st.image(image, width = 120)
    with rowi_spacer2:
        st.write("")

    #new row
    row1_spacer1, row1_1, row1_spacer2, row1_2, row1_spacer3 = st.columns(
        (.1, 2, .2, 1, .1)
    )
    row1_1.title('Charlotte Housing Exploration')
    with row1_2:
        row1_2.subheader('Calvin Hathcock, Divyaja Reddy, Phillip Hirsch')

    #new row
    row2_spacer1, row2_1, row2_spacer2 = st.columns(
        (.1, 3.2, .1)
    )
    with row2_1:
        st.markdown('An interactive dashboard exploring the state of households in Charlotte with regards to socio-economic status.')
        st.markdown('')
        st.markdown('Our goal is to discover what factors contribute to cost-burdened status of Charlotte households, as well as uncovering insights about general distributions of household properties.')    
        st.markdown('')
        st.markdown('Our data comes from the [2018 American Community Survey](https://www.census.gov/programs-surveys/acs), a yearly survey of American households. The City of Charlotte created a subset for the Charlotte-Mecklenburg area and uploaded it to the [Charlotte Data Portal](https://data.charlottenc.gov/datasets/housing-demand-and-availability-by-income/explore).')
        st.markdown('')
        st.markdown("The data is in a tabular format with each record corresponding to a single household. There are over 1700 rows and 200 columns. The raw CSV is not very interpretable, however a data dictionary is provided by the Census Bureau so that we can look up semantics of values. You can find this app's source code, our notebooks for cleaning/modeling, and other utility scripts in our [project's repository](https://github.com/ITCS4122VISUALANALYTICS/Charlotte_Housing).")
        st.markdown("")
