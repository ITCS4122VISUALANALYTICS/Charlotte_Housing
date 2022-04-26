import streamlit as st
import altair as alt
import pandas as pd
import matplotlib.pyplot as plt
from pycaret.regression import *
from pycaret.classification import *
from scripts.utilities import *
from PIL import Image


###################################################
# Helper functions and initial assignments
###################################################
@st.cache
def load_data():
    df = pd.read_csv("data_sets/df_cleaned_clusters.csv")
    df = df.drop(columns = 'Unnamed: 0')
    return df

def histogram(column, target):
    types = [DATA_TYPES_ALTAIR[get_datatype(x)] for x in [column, target]]
    hist = alt.Chart(df).mark_bar().encode(
        alt.X(column, type = types[0], bin=False),
        alt.Y('count()'),
        alt.Color(target, type = types[1])
    ).properties(title = column+" Distribution").interactive()
    return hist

def scatter(col1, col2, target):
    types = [DATA_TYPES_ALTAIR[get_datatype(x)] for x in [col1, col2, target]]
    scat = alt.Chart(df).mark_circle().encode(
        alt.X(col1, type = types[0]),
        alt.Y(col2, type = types[1]),
        alt.Color(target, type = types[2])
    ).properties(title = col1 + ' vs ' + col2).interactive()
    return scat

image = Image.open('data_sets/flag.png')
df = load_data()

###################################################
# Image
###################################################
row0_spacer1, row0_1, row0_spacer2= st.columns(
    (.1, 3.2, .1)
)
with row0_spacer1:
    st.write("")
with row0_1:
    st.image(image, width = 200)
with row0_spacer2:
    st.write("")
    
###################################################
# INTRO
###################################################
row1_spacer1, row1_1, row1_spacer2, row1_2, row1_spacer3 = st.columns(
    (.1, 2, .2, 1, .1)
)
row1_1.title('Charlotte Housing Exploration')
with row1_2:
    row1_2.subheader('Calvin Hathcock, Divyaja Reddy, Phillip Hersch')
    
row2_spacer1, row2_1, row2_spacer2 = st.columns(
    (.1, 3.2, .1)
)
with row2_1:
    st.markdown('An interactive dashboard exploring the state of housing in Charlotte with regards to socio-economic status.')
    st.markdown('')
    st.markdown('Our goal is to discover what factors contribute to affordability and cost-burdened status of Charlotte households, as well as uncovering insights about general distributions of household properties.')    
    st.markdown('')
    st.markdown('Our data comes from the [2018 American Community Survey](https://www.census.gov/programs-surveys/acs), a yearly survey of American households. The City of Charlotte created a subset for the Charlotte-Mecklenburg area and uploaded it to the [Charlotte Data Portal](https://data.charlottenc.gov/datasets/housing-demand-and-availability-by-income/explore).')
    st.markdown('')
    st.markdown("The data is in a tabular format with each record corresponding to a single household. There are over 1700 rows and 200 columns. The raw CSV is not very interpretable, however a data dictionary is provided by the Census Bureau so that we can look up semantics of values. You can find this app's source code, our notebooks for cleaning/modeling, and other utility scripts in our [project's repository](https://github.com/ITCS4122VISUALANALYTICS/Charlotte_Housing).")
    st.markdown("")
    see_data = st.expander('You can click here to see the raw data first 👉')
    with see_data:
        st.dataframe(data=df)


###################################################
# Raw exploration
###################################################

row3_spacer1, row3_1, row3_spacer2 = st.columns(
    (.1, 3.2, .1)
)
with row3_1:
    st.header('Visualization Sandbox')
    #st.markdown('***')
    st.markdown('Use this section to gain an initial understanding of the data')

row4_spacer1, row4_1, row4_spacer2, row4_2, row4_spacer3 = st.columns(
    (.1, 1, .2, 1, .1)
)



with row4_1:
    st.subheader('Interactive Histogram')
    st.write('Select a feature to explore its distribution and a feature to color encode.')
    st.write(" ")

    #allow user to select a feature
    featureH = st.selectbox('Select Feature', df.columns)
    colorH = st.selectbox('Select Color Encoding', df.columns)
with row4_2:
    st.write('')
    st.write(histogram(featureH, colorH).properties(
    width=480,
    height=360
))

row5_spacer1, row5_1, row5_spacer2, row5_2, row5_spacer3 = st.columns(
    (.1, 1, .2, 1, .1)
)
with row5_1:
    st.subheader('Interactive Scatter')
    st.write('Select two features to visualize correlations and a third to color encode.')
    st.write(" ")

    x_selectS = st.selectbox('X Axis', df.columns)
    y_selectS = st.selectbox('Y Axis', df.columns)
    colorS = st.selectbox('Color', df.columns)


with row5_2:
    st.write(scatter(x_selectS, y_selectS, colorS).properties(
    width=480,
    height=360
))


st.subheader('Interactive Heatmap')
st.write('This section will allow you to explore the data interactively. You can select a feature and a target to see a heatmap of the feature.')
st.write(" ")

