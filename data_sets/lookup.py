#Data Dictionary Lookup Functions

data_dict = pd.read_csv('data_sets/data_dictionary.csv')
#sort to optimize lookup performance
data_dict = data_dict.sort_index() 
#NOTE: the following features are not in the Dictionary since they were added by the city of Charlotte.
#      ['WGTP_CLT', 'AMI', 'AFF_OCC', 'AFF_VACS', 'COST_BURDALL', 'YEAR']

'''
Look up the semantics of a feature name

    Parameters:
        feat (str): name of column/feature
    Returns:
        data description (str)
'''
def lookup_feat(feat):
    try:
        desc = data_dict.loc['NAME', feat]['C'][0]
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
def lookup_value(feat, value):
    try:
        subset = data_dict.loc['VAL', feat]
        desc = subset[subset['C'] == value]['Record Type'][0]
    except:
        return '***LOOK UP FAILED***'
    else:
        return desc
    
'''
Look up all values and their semantics of a feature

    Parameters:
        feat (str): name of column/feature
    Returns:
        data description (pandas.DataFrame)
'''
def lookup_values(feat):
    try:
        subset = data_dict.loc['VAL', feat]
        desc = subset[['C', 'Record Type']]
        desc = desc.reset_index().drop(columns = ['level_0', 'level_1']).rename(columns = {'C':'Value'})
    except:
        return '***LOOK UP FAILED***'
    else:
        return desc