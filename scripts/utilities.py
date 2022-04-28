import pandas as pd
import streamlit as st
from scripts.constants import *

#read data dictionary
try:
    data_dict = pd.read_csv(PATH_DATA_DICTIONARY)
except:
    data_dict = pd.read_csv('../' + PATH_DATA_DICTIONARY)
    
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
            if feat == 'Cluster':
                desc = 'Cluster'
            elif feat == 'HHLANP':
                desc = 'Household language'
            else:
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
        if feat == 'Cluster':
            name = 'Cluster',
            desc = 'Cluster'
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
    try:
        if feat == 'HFL': # accounting for an error in the data dictionary
            return 'C'
        if feat == 'Cluster':
            return 'C'
        if feat not in CLT:
            return data_dict.loc['NAME', feat]['NAME'][0]
        else:
            return CLT_TYPES[feat]
    except: 
        return '***LOOK UP FAILED***'

'''
Load needed datasets for streamlit app

    Returns:
        df: raw dataframe
        cost_burd_results: metrics from classification models
'''
@st.cache
def load_data():
    df = pd.read_csv(PATH_DF_CLEAN_STRINGS).drop(columns = 'Unnamed: 0')
    cost_burd_results = pd.read_csv(PATH_COST_BURD_RESULTS).drop(columns = 'Unnamed: 0')
    return df, cost_burd_results

#so st.cache doesnt break when being called outside of streamlit app
def load_data_nb():
    df = pd.read_csv(PATH_DF_CLEAN_STRINGS).drop(columns = 'Unnamed: 0')
    cost_burd_results = pd.read_csv(PATH_COST_BURD_RESULTS).drop(columns = 'Unnamed: 0')
    return df, cost_burd_results

'''
Generate dictionary containing Column Acronym: Definition Pairs.

    Params:
        invert: boolean value to determine where to invert pairs or not

    Returns:
        dictionary
'''
def generate_dictionary(invert):
    df = pd.read_csv(PATH_DF_CLEAN_CLUSTERS)
    pairs = {}
    if invert:  
        for i in range(len(df.columns)):
            pairs[get_feat(df.columns[i])] = df.columns[i]
    else:
        for i in range(len(df.columns)):
            pairs[df.columns[i]] = get_feat(df.columns[i])
    return pairs

