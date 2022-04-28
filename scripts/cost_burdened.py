import streamlit as st
from scripts.utilities import *
from scripts.plots import *
from PIL import Image 

def cost_burdened():
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
        st.title('Cost-Burdened Analysis')
        st.subheader('What features contribute to a household being cost-burdened?')
        
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
        (.1, 3.2, .1)
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
        st.markdown('I selected the top features across all the models implemented. They were as follows:')
        st.markdown('- Tenure Type **(TEN)**\n- Number of People in the Household **(NP)**\n - Household/Family Type **(HHT)**\n - Limited English Speaking Household **(LNGI)**\n - Electricity Cost **(ELEP)**\n - Number of Vehicles **(VEH)**\n - Sample Weight **(CLT_WGTP)**')
    with row3_2:
        st.markdown('***')
        st.write('LightGBM SHAP Values')
        st.image(LIGHTGBM_SHAP_CB_PATH, width = 350)
        st.markdown('***')

     
     #new row
    row8_spacer1, row8_1, row8_spacer2, row8_2, row8_spacer3 = st.columns(
        (.1, 1, .2, 1, .1)
    )

    with row8_1:
        st.markdown('**Correlation Heatmap of Selected Features**')
        st.image(HEATMAP_FEAT_SELECT)
    with row8_2:
        cols_of_interest = ['TEN', 'NP', 'HHT', 'LNGI', 'ELEP', 'VEH', 'WGTP_CLT']
        featureH = st.selectbox('Select Feature', cols_of_interest)
        st.write(histogram(featureH, 'COST_BURDALL', False).properties(
            height=380,
            width=430,
            title = PAIRS[featureH] + ' Distribution' ))

       #new row
    row7_spacer1, row7_1, row7_spacer2 = st.columns(
        (.1, 2.2, .1)
    )

    with row7_1:
        st.markdown('When exploring these features **individually** or by **pairs**, it is hard to see any clear correlation with cost-burdened status or with each other.')



    row9_spacer1, row9_1, row9_spacer2 = st.columns(
        (.1, 2.2, .1)
    )
    with row9_1:
        st.markdown('***')
        st.markdown('In order to better visualize the relationship between these features, we created a **Parallel Coordinate Plot**. Due to the nature of the plot, we needed to drop the continuous values as they were to noisy to interpret.')
        st.markdown('')
        st.markdown('We adjusted the colormap of Cost-Burden so that we can perceive blending a bit easier. Yellow refers to cost-burdened, Purple refers to **not** cost-burdened. This plot allows us to see the how different combinations of the categorical features contribute to cost-burdened status. The more purple or yellow a line is, the more frequent the corresponding cost-burdened status is.')
        st.markdown('This plot can be a bit hard to interpret if you have not come across one before. Basically:\n - The **X-Axis** contains our features we selected based off the models, each of which is categorical.\n - The **Y-Axis** correponds to the possible values each category could be. Note that these values are encoded as numbers and then standardized so that its distribution is centered around zero. So the further away a datapoint is from 0, the less often it occurs. This also allows us to identify outliers.\n - The **lines** as all the possible paths that a datapoint could take across all the given features. The color corresponds to cost-burdened status. The more yellow is Yes, Purple is No. So when a line is very Yellow or very Purple, it means that most of the datapoints that have that specific combination of values tend to be Cost-Burdened or Not respectively. The grayish lines are more noisy and do not clearly lean one way or the other.\n - The plot on the right has the lines removed and can be used to better see the spread of the data.')

        st.write(parallel_coord().properties(title = 'Parallel Coordinate Plot of Selected Features'))
        st.markdown('As a recap, for this analysis, we created a handful of classification models to predict whether or not a household is cost-burdened. We analyzed the feature importance of all of these models and selected the features that had the highest importance across all models. We then analyzed these features through visualizations. Based on these visualizations, we can identify what combination of factors tend contribute to cost-burdened status. It is important to note that these features do not obviously contribute on their own. It is only when certain combinations of values occur that we are able to identify cost-burdened status. While this does not generalize the whole data set, it is valuable since at the end of the day this data is about real people.')