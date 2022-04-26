import streamlit as st
from scripts.utilities import *
from scripts.plots import *

df, cost_burd_results = load_data()

def explorer():
    #new row    
    row0_spacer1, row0_1, row0_spacer2 = st.columns(
        (.1, 3.2, .1)
    )
    with row0_1:
        st.title('Data Explorer')
        #st.markdown('***')
        st.markdown('Use this tool to gain an initial understanding of the data')
    see_data = st.expander('You can click here to see the raw data first 👉')
    with see_data:
        st.dataframe(data=df)

    #new row
    row1_spacer1, row1_1, row1_spacer2, row1_2, row1_spacer3 = st.columns(
        (.1, 1, .2, 1, .1)
    )

    with row1_1:
        st.subheader('View a Feature')
        st.write('Select a feature to explore its distribution and a feature to color encode.')
        st.write(" ")

        #allow user to select a feature
        featureH = st.selectbox('Select Feature', df.columns)
        colorH = st.selectbox('Select Color Encoding', df.columns)
    with row1_2:
        st.write('')
        st.write(histogram(featureH, colorH, False).properties(
        width=480,
        height=360
    ))

    #new row
    row2_spacer1, row2_1, row2_spacer2, row2_2, row2_spacer3 = st.columns(
        (.1, 1, .2, 1, .1)
    )
    with row2_1:
        st.subheader('Compare Features')
        st.write('Select two features to visualize correlations and a third to color encode.')
        st.write(" ")

        x_selectS = st.selectbox('X Axis', df.columns)
        y_selectS = st.selectbox('Y Axis', df.columns)
        colorS = st.selectbox('Color', df.columns)


    with row2_2:
        st.write(scatter(x_selectS, y_selectS, colorS).properties(
        width=480,
        height=360
    ))