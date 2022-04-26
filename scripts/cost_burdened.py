import streamlit as st
from scripts.utilities import *
from scripts.plots import *

def cost_burdened():
    #new row
    row0_spacer1, row0_1, row0_spacer2 = st.columns(
        (.1, 3.2, .1)
    )
    with row0_1:
        st.title('Cost-Burdened Analysis')
        st.subheader('What features contribute to a household being cost-durdened?')
        
    #new row
    row1_spacer1, row1_1, row1_spacer2, row1_2, row1_spacer3 = st.columns(
        (.1, 1, .2, 1, .1)
    )
    with row1_1:
        st.markdown('Each household is marked with a binary value (0 or 1) to represent whether it is cost burdened or not. In this section we will apply classification models to this target to gain insights about what contributes to it.')
        st.markdown('')
        st.markdown('As we can see, the distribution of cost burdened status is slightly skewed.')
    with row1_2:
        st.write(histogram('COST_BURDALL', 'COST_BURDALL', False))

    #new row
    row2_spacer1, row2_1, row2_spacer2 = st.columns(
        (.1, 3.2, .1)
    )
    with row2_1:
        st.markdown('We created three models: Logistic Regression, Decision Tree, and LightGBM. All of which performed rather well with the classification metrics listed as follows:')
        st.write(cost_burd_results)
        
    #new row
    row3_spacer1, row3_1, row3_spacer2, row3_2, row3_spacer3 = st.columns(
        (.1, 1, .2, 1, .1)
    )
    with row3_1:
        st.markdown('Once satisfied with our models performance, we calculated the feature importance for each.')