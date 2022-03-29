#Data Dictionary Lookup Functions

data_dict = pd.read_csv('data_sets/data_dictionary.csv')
#sort to optimize lookup performance
data_dict = data_dict.sort_index() 
cols = data_dict.columns
#NOTE: the following features are not in the Dictionary since they were added by the city of Charlotte.
others =  ['WGTP_CLT', 'AMI', 'AFF_OCC', 'AFF_VACS', 'COST_BURDALL', 'YEAR']

CLT_FEAT = {'WGTP_CLT' : 'Housing Unit Weight for City of Charlotte', 
            'AMI' : 'Area Median Income for the household',
            'AFF_OCC' : 'The affordability level of the rental housing unit',
            'AFF_VACS' : 'The affordability level of the vacant housing unit',
            'COST_BURDALL' : 'Cost-burdened status of household',
            'YEAR' : 'Year of the ACS PUMS data'}

CLT_VALUES = {
            'WGTP_CLT' : 'Integer weight of housing unit', 
            'AMI' : {
                1: '30% and Below',
                2: '31 to 50%',
                3: '51 to 60%',
                4: '61 to 80%',
                5: '81 to 100%',
                6: '101 to 120%',
                7: 'Greater than 120%'
                    },
            'AFF_OCC' : {
                1: '30% and Below',
                2: '31 to 50%',
                3: '51 to 60%',
                4: '61 to 80%',
                5: '81 to 100%',
                6: '101 to 120%',
                7: 'Greater than 120%'
                        },
            'AFF_VACS' : {
                1: '30% and Below',
                2: '31 to 50%',
                3: '51 to 60%',
                4: '61 to 80%',
                5: '81 to 100%',
                6: '101 to 120%',
                7: 'Greater than 120%'
            },
            'COST_BURDALL' : {
                0: 'No',
                1: 'Yes'
            },
            'YEAR' : 'Year of the ACS PUMS data'
           }

'''
Look up the semantics of a feature name

    Parameters:
        feat (str): name of column/feature
    Returns:
        data description (str)
'''
def lookup_feat(feat):
    try:
        if feat not in others:
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
def lookup_value(feat, value):
    try:
        if feat not in others:
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
def lookup_values(feat):
    try:
        if feat not in others:
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