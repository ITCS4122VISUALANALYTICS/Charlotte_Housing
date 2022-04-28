import streamlit as st
from scripts.utilities import *
from scripts.constants import *
from scripts.plots import *
from PIL import Image 


df, cost_burd_results, df_concat = load_data()

def explorer():
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
        (.1, 0.6, .2, 1.4, .1)
    )

    with row1_1:
        st.subheader('View a Feature')
        st.write('Select a feature to explore its distribution and a feature to color encode.')
        st.write(" ")

        #allow user to select a feature
        featureH = st.selectbox('Select Feature', [PAIRS[x] for x in df.columns])
        #featureH = st.selectbox('Select Feature', df.columns)
        colorH = st.selectbox('Select Color Encoding', [PAIRS[x] for x in df.columns])
        #colorH = st.selectbox('Select Color Encoding', df.columns)
    with row1_2:
        st.write('')
        st.write(histogram(INVERSE_PAIRS[featureH], INVERSE_PAIRS[colorH], False).properties(
        width=480,
        height=360
    ))

    #new row
    row2_spacer1, row2_1, row2_spacer2, row2_2, row2_spacer3 = st.columns(
        (.1, 0.6, .2, 1.4, .1)
    )
    with row2_1:
        st.subheader('Compare Features')
        st.write('Select two features to visualize correlations and a third to color encode.')
        st.write(" ")

        x_selectS = st.selectbox('X Axis', [PAIRS[x] for x in df.columns])
        y_selectS = st.selectbox('Y Axis', [PAIRS[x] for x in df.columns])
        colorS = st.selectbox('Color', [PAIRS[x] for x in df.columns])


    with row2_2:
        st.write(scatter(INVERSE_PAIRS[x_selectS], INVERSE_PAIRS[y_selectS], INVERSE_PAIRS[colorS]).properties(
        width=480,
        height=360
    ))