import pandas as pd
import streamlit as st
from scripts.constants import *

#read data dictionary
try:
    data_dict = pd.read_csv('data_sets/data_dictionary.csv')
except:
    data_dict = pd.read_csv('../data_sets/data_dictionary.csv')
    
#sort to optimize lookup performance
data_dict = data_dict.sort_index() 
cols = data_dict.columns

'''
Look up the semantics of a feature name

    Parameters:
        feat (str): name of column/feature
    Returns:
        data description (str)
'''
def get_feat(feat):
    try:
        if feat not in CLT:
            desc = data_dict.loc['NAME', feat]['C'][0]
        else:
            desc = CLT_FEAT[feat]
    except: 
        return '***LOOK UP FAILED***'
    else:
        return desc

'''
Look up the semantics of a specified value of a feature

    Parameters:
        feat (str): name of column/feature
        value (str): particular value within column
    Returns:
        data description (str)
'''
def get_value(feat, value):
    try:
        if feat not in CLT:
            subset = data_dict.loc['VAL', feat]
            desc = subset[subset['C'] == value]['Record Type'][0]
        else: 
            desc = CLT_VALUES[feat][value]
    except:
        return '***LOOK UP FAILED***'
    else:
        return desc
    
'''
Look up all values and their semantics of a feature

    Parameters:
        feat (str): name of column/feature
    Returns:
        feature desc
        values desc data description (pandas.DataFrame)
'''
def get_values(feat):
    try:
        if feat not in CLT:
            name = data_dict.loc['NAME', feat]['C'][0]
            subset = data_dict.loc['VAL', feat]
            desc = subset[['C', 'Record Type']]
            desc = desc.reset_index().drop(columns = ['level_0', 'level_1']).rename(columns = {'C':'Value'})
        else: 
            name = CLT_FEAT[feat]
            desc = CLT_VALUES[feat]
    except:
        return '***LOOK UP FAILED***'
    else:
        return name, desc
    
'''
Lookup the data type of a given feature

    Parameters:
        feat (str): name of column/feature
    Returns:
        str: 'C' or 'N' (Character or Numeric)
''' 
def get_datatype(feat):
    t = ''
    try:
        if feat == 'HFL': # accounting for an error in the data dictionary
            return 'C'
        if feat == 'Cluster':
            return 'C'
        if feat not in CLT:
            t = data_dict.loc['NAME', feat]['NAME'][0]
        else:
            return 'C'
    except: 
        return '***LOOK UP FAILED***'
    else:
        return t

'''
Load needed datasets for streamlit app

    Returns:
        df: raw dataframe
        cost_burd_results: metrics from classification models
'''
@st.cache
def load_data():
    df = pd.read_csv(PATH_DF_CLEAN_CLUSTERS).drop(columns = 'Unnamed: 0')
    cost_burd_results = pd.read_csv(PATH_COST_BURD_RESULTS).drop(columns = 'Unnamed: 0')
    return df, cost_burd_results