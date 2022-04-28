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
        st.markdown('Each household is marked with a binary value (Yes or No) to represent whether it is cost burdened or not. In this section we will apply classification models to this target to gain insights about what contributes to it.')
        st.markdown('')
        st.markdown('On initial inspection, we can see, the distribution of cost burdened status is slightly skewed towards no. We fixed this imbalance before modeling by using [Synthetic Minority Oversampling Technique (SMOTE)](https://machinelearningmastery.com/smote-oversampling-for-imbalanced-classification/). Other pre-processing techniques include: Standardization, Outlier Removal, Multi-Collinearity Removal, and Null imputation.')

    with row1_2:
        st.write(histogram('COST_BURDALL', 'COST_BURDALL', False).properties(
        width=280,
        height=310,
        title = 'Cost-Burdened Distribution'
    ))

    #new row
    row4_spacer1, row4_1, row4_spacer2 = st.columns(
        (.1, 3.2, .1)
    )

    with row4_1:
        st.markdown('Our initial models clearly **overfitted** as all of them performed 100% accurately. After inspecting the feature importance, we could see that the **Cost-Burdened** variable can be derived directly from **Gross Rent as Perecentage of Income (GRPIP).** And also, **GRPIP** is directly derived from two other features, **Monthly Rent and Household Income**.')
        st.markdown('')
        st.markdown('We can verify this with the plots below. As you can see, there is a distinct cut off between Cost-Burdened status. We will drop these features since it is evidence of multi-collinearity and so that the model does not overfit again.')
    
    #new row
    row5_spacer1, row5_1, row5_spacer2, row5_2, row5_spacer3 = st.columns(
        (.1, 1, .2, 1, .1)
    )
    with row5_1:
        st.write(histogram('GRPIP', 'COST_BURDALL', False).properties(
        title = 'Rent as a Perecentage of Income Distribution'
    ))
    with row5_2:
        st.write(scatter('RNTP', 'HINCP', 'COST_BURDALL').properties(title = 'Monthly Rent vs. Household Income'))
    
    #new row
    row6_spacer1, row6_1, row6_spacer2 = st.columns(
        (.1, 3.2, .1)
    )
    with row6_1:
        st.markdown("Yet again, there seemed to be an overfit due to very high scores without much pre-processing. Looking at the feature importance plots, we can see that **Affordability** and **Area Median Income** were the top features. These features were also derived from economic factors. We can see with the following plots how these relate to cost-burdened status.")
    #new row
    row7_spacer1, row7_1, row7_spacer2 = st.columns(
        (.5, 2.8, .1)
    )
    with row7_1:
        st.write(cost_burd_plot().properties(title = 'Multi-Collinearity on Cost-Burdened Status'))

    #new row
    row2_spacer1, row2_1, row2_spacer2 = st.columns(
        (.1, 2.2, .1)
    )

    with row2_1:
        st.markdown("It's obvious that Cost-Burdened status can easily be derived from other economic factors. While this is valuable, we want to see what other properties of households contribute as well. So we went ahead and dropped all other economic features before modeling again.")
                
    #new row
    row3_spacer1, row3_1, row3_spacer2, row3_2, row3_spacer3 = st.columns(
        (.1, 1, .2, 1, .1)
    )
    with row3_1:
        st.markdown("We focused on a few models, namely: **Logistic Regression, Decision Trees, and LightGBM**. It's important to note that our performance was not great. The average accuracy score was about **0.66**. While better than randomly guessing, it's not great. However it is still worth looking at their feature importances of each. We used methods such as [SHAP Values](https://christophm.github.io/interpretable-ml-book/shap.html) to do this.")
        st.markdown('')
        st.markdown('I selected the top features across all the models implemented. They were as follows: **Tenure Type, Number of People in the Household, Family Type, Limited English Speaking Household, Electricity Cost, Number of Vehicles, and Sample Weight**')
    with row3_2:
        st.write('LightGBM SHAP Values')
        st.image(LIGHTGBM_SHAP_CB_PATH, width = 350)

        #new row
    row7_spacer1, row7_1, row7_spacer2 = st.columns(
        (.1, 2.2, .1)
    )

    with row7_1:
        st.markdown('When exploring these features **individually**, it is hard to see any clear correlation with cost-burdened status or with each other.')
