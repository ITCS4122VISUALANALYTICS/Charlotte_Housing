import streamlit as st
import altair as alt
import pandas as pd
import matplotlib.pyplot as plt
from vega_datasets import data
from pycaret.regression import *
from pycaret.classification import *
from scripts.utilities import *

load_config('notebooks/rf_config')

# load model
@st.cache 
def predict_cache(test_data):
    rf_saved = load_model('notebooks/rf_model')
    predictions = predict_model(rf_saved, data = test_data)
    return predictions['Label']

df = pd.read_csv("data_sets/df_cleaned.csv")

# Introduction Section
	# - Motivation
	# - Goal
	# - Soft Data Introduction
st.title('Charlotte Housing')
st.write(" ")
st.header('Introduction')
st.markdown('***')
st.subheader('Motivation')
st.write('Our motivation for this project is to predict the price of a house in Charlotte, North Carolina. The data we are using is from the [Charlotte Housing Data Project](https://data.charlottenc.gov/datasets/housing-demand-and-availability-by-income/explore).')
st.write(" ")
st.subheader('Goal')
st.write('The goal of this project is to predict the price of a house in Charlotte, NC. The data is from the [Charlotte Housing Data Project](https://data.charlottenc.gov/datasets/housing-demand-and-availability-by-income/explore).')
st.write(" ")
st.subheader('Soft Data Introduction')
st.write('The data we are using is from the [Charlotte Housing Data Project](https://data.charlottenc.gov/datasets/housing-demand-and-availability-by-income/explore).')
st.write(" ")
st.write(" ")

# Exploration Section
	# - Interactive plots
		# Histogram of single feature
			# Allow color to be changed to various targets
st.header('Exploration')
st.markdown('***')
st.subheader('Interactive Histogram')
st.write('This section will allow you to explore the data interactively. You can select a feature and a target to see a histogram of the feature.')
st.write(" ")

#allow user to select a feature
featureH = st.selectbox('Select Feature', df.columns)

def histogram(column):
    hist = alt.Chart(df).mark_bar().encode(
        alt.X(column, bin=False),
        y='count()',
    ).properties(title = column+" Distribution").interactive()
    return hist

st.write(histogram(featureH))

		# Scatter of two features
			# Allow color to be changed based on targets
			# Simple regression on given features too???
st.subheader('Interactive Scatter')
st.write('This section will allow you to explore the data interactively. You can select a feature and a target to see a scatter plot of the feature.')
st.write(" ")

#allow user to select features and target
featureS = st.selectbox('Feature', df.columns)
targetS = st.selectbox('Target', df.columns)

def scatter(col1, col2):
    types = [DATA_TYPES_ALTAIR[get_datatype(x)] for x in [col1, col2]]
    scat = alt.Chart(df).mark_circle().encode(
        alt.X(col1, type = types[0]),
        alt.Y(col2, type = types[1]),
    ).properties(title = col1 + ' vs ' + col2).interactive()
    return scat

st.write(scatter(featureS, targetS))

		# Heatmap
			# select subset of features to compare
            # allow color to be changed based on targets
st.subheader('Interactive Heatmap')
st.write('This section will allow you to explore the data interactively. You can select a feature and a target to see a heatmap of the feature.')
st.write(" ")




		# Other simple plots??
            # Correlation matrix
            # Boxplot
            # Violin plot
            # Bar plot


	# - Include notes on how to interpret each?
	# - Use cleaned or uncleaned data?
	# - Need to allow value acronyms to be converted on the spot OR convert them already

# Model Analysis
	# - Allow for users to predict rent based on subset of features
		# - paired with plots?



	# - Allow users to predict if cost burdened based on features	
		# - paired with plots?



	# - Allow users to determine if a house is considered affordable based on features
	    # - paired with plots?



	# - Analysis of Classification on COSTBURD_ALL



	# - Analysis of Regression on rent



	# - Analysis of Regression on affordability




# Conclusion Section




# Data Dictionary
	# - Hard data introduction



	# - Pre-processing Methods