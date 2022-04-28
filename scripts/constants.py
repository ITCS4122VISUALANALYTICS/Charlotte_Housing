#features not includes in PUMS ACS Data Dictionary
CLT =  ['WGTP_CLT', 'AMI', 'AFF_OCC', 'AFF_VACS', 'COST_BURDALL', 'YEAR']

#Meanings of features added by Charlotte
CLT_FEAT = {
	'WGTP_CLT' : 'Housing Unit Weight for City of Charlotte', 
    'AMI' : 'Area Median Income for the household',
    'AFF_OCC' : 'The affordability level of the rental housing unit',
    'AFF_VACS' : 'The affordability level of the vacant housing unit',
    'COST_BURDALL' : 'Cost-burdened status of household',
    'YEAR' : 'Year of the ACS PUMS data'
}

# Meanings of the values of features added by Charlotte
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

CLT_TYPES = {
    'WGTP_CLT' : 'quantitative', 
    'AMI' : 'ordinal',
    'AFF_OCC' : 'ordinal',
    'AFF_VACS' : 'ordinal',
    'COST_BURDALL' : 'nominal',
    'YEAR' : 'ordinal'
}

# For (data dictionary -> altair) type conversion
DATA_TYPES_ALTAIR = {
    'C' : 'nominal',
    'N' : 'quantitative',
    'ordinal':'ordinal',
    'quantitative': 'quantitative',
    'nominal':'nominal'
}

# PUMA Area Codes corresponding region
PUMA_CODES = {
    3101 : "Charlotte City (Central)", 
    3102 : "Charlotte City (Northwest)", 
    3103 : "Charlotte City (Northeast)",
    3104 : "Charlotte City (South)",
    3105 : "Charlotte City (Southwest)", 
    3106 : "Mecklenburg County (North)--Huntersville, Cornelius & Davidson Towns",
    3107 : "Mecklenburg County (East)--Mint Hill & Matthews (North) Towns",
    3108 : "Mecklenburg County (South)--Matthews Town (South)"
}


#generated from generate_dictionary() function
PAIRS = {'PUMA': 'Public use microdata area code (PUMA) based on 2010 Census definition (areas with population of 100,000 or more, use with ST for unique code)', 'NP': 'Number of Persons', 'ACCESS': 'Access to the Internet', 'BATH': 'Bathtub or shower', 'BDSP': 'Number of bedrooms', 'BLD': 'Units in structure', 'BROADBND': 'Cellular data plan for a smartphone or other mobile device', 'COMPOTHX': 'Other computer equipment', 'DIALUP': 'Dial-up service', 'ELEFP': 'Electricity cost flag variable', 'ELEP': 'Electricity cost', 'FS': 'Yearly food stamp/Supplemental Nutrition Assistance Program (SNAP) recipiency', 'FULFP': 'Fuel cost flag variable', 'GASFP': 'Gas cost flag variable', 'HFL': 'House heating fuel', 'HISPEED': 'Broadband (high speed) Internet service such as cable, fiber optic, or DSL service', 'LAPTOP': 'Laptop or desktop', 'OTHSVCEX': 'Other Internet service', 'REFR': 'Refrigerator', 'RMSP': 'Number of rooms', 'RNTM': 'Meals included in rent', 'RNTP': 'Monthly rent (use ADJHSG to adjust RNTP to constant dollars)', 'SATELLITE': 'Satellite Internet service', 'SMARTPHONE': 'Smartphone', 'TABLET': 'Tablet or other portable wireless computer', 'TEL': 'Telephone service', 'TEN': 'Tenure', 'VEH': 'Vehicles (1 ton or less) available', 'WATFP': 'Water cost flag variable', 'YBL': 'When structure first built', 'GRPIP': 'Gross rent as a percentage of household income past 12 months', 'HHL': 'Household language', 'HHLANP': 'Household language', 'HHT': 'Household/family type', 'HINCP': 'Household income (past 12 months, use ADJINC to adjust HINCP to constant dollars)', 'HUPAC': 'HH presence and age of children', 'KIT': 'Complete kitchen facilities', 'LNGI': 'Limited English speaking household', 'MULTG': 'Multigenerational household', 'MV': 'When moved into this house or apartment', 'NOC': 'Number of own children in household (unweighted)', 'NPP': 'Grandparent headed household with no parent present', 'NR': 'Presence of nonrelative in household', 'PARTNER': 'Unmarried partner household', 'PSF': 'Presence of subfamilies in household', 'R18': 'Presence of persons under 18 years in household (unweighted)', 'R65': 'Presence of persons 65 years and over in household (unweighted)', 'RESMODE': 'Response mode', 'SRNT': 'Specified rental unit', 'SSMC': 'Same-sex married couple households', 'WGTP_CLT': 'Housing Unit Weight for City of Charlotte', 'AMI': 'Area Median Income for the household', 'AFF_OCC': 'The affordability level of the rental housing unit', 'COST_BURDALL': 'Cost-burdened status of household', 'Cluster': 'Cluster'}

INVERSE_PAIRS = {'Public use microdata area code (PUMA) based on 2010 Census definition (areas with population of 100,000 or more, use with ST for unique code)': 'PUMA', 'Number of Persons': 'NP', 'Access to the Internet': 'ACCESS', 'Bathtub or shower': 'BATH', 'Number of bedrooms': 'BDSP', 'Units in structure': 'BLD', 'Cellular data plan for a smartphone or other mobile device': 'BROADBND', 'Other computer equipment': 'COMPOTHX', 'Dial-up service': 'DIALUP', 'Electricity cost flag variable': 'ELEFP', 'Electricity cost': 'ELEP', 'Yearly food stamp/Supplemental Nutrition Assistance Program (SNAP) recipiency': 'FS', 'Fuel cost flag variable': 'FULFP', 'Gas cost flag variable': 'GASFP', 'House heating fuel': 'HFL', 'Broadband (high speed) Internet service such as cable, fiber optic, or DSL service': 'HISPEED', 'Laptop or desktop': 'LAPTOP', 'Other Internet service': 'OTHSVCEX', 'Refrigerator': 'REFR', 'Number of rooms': 'RMSP', 'Meals included in rent': 'RNTM', 'Monthly rent (use ADJHSG to adjust RNTP to constant dollars)': 'RNTP', 'Satellite Internet service': 'SATELLITE', 'Smartphone': 'SMARTPHONE', 'Tablet or other portable wireless computer': 'TABLET', 'Telephone service': 'TEL', 'Tenure': 'TEN', 'Vehicles (1 ton or less) available': 'VEH', 'Water cost flag variable': 'WATFP', 'When structure first built': 'YBL', 'Gross rent as a percentage of household income past 12 months': 'GRPIP', 'Household language': 'HHLANP', 'Household/family type': 'HHT', 'Household income (past 12 months, use ADJINC to adjust HINCP to constant dollars)': 'HINCP', 'HH presence and age of children': 'HUPAC', 'Complete kitchen facilities': 'KIT', 'Limited English speaking household': 'LNGI', 'Multigenerational household': 'MULTG', 'When moved into this house or apartment': 'MV', 'Number of own children in household (unweighted)': 'NOC', 'Grandparent headed household with no parent present': 'NPP', 'Presence of nonrelative in household': 'NR', 'Unmarried partner household': 'PARTNER', 'Presence of subfamilies in household': 'PSF', 'Presence of persons under 18 years in household (unweighted)': 'R18', 'Presence of persons 65 years and over in household (unweighted)': 'R65', 'Response mode': 'RESMODE', 'Specified rental unit': 'SRNT', 'Same-sex married couple households': 'SSMC', 'Housing Unit Weight for City of Charlotte': 'WGTP_CLT', 'Area Median Income for the household': 'AMI', 'The affordability level of the rental housing unit': 'AFF_OCC', 'Cost-burdened status of household': 'COST_BURDALL', 'Cluster': 'Cluster'}

PATH_DF_CLEAN_CLUSTERS = 'data_sets/df_cleaned_clusters.csv'

PATH_COST_BURD_RESULTS = 'data_sets/cost_burd_results.csv'

PATH_DATA_DICTIONARY = 'data_sets/data_dictionary.csv'

PATH_DF_CLEAN_STRINGS = 'data_sets/df_cleaned_STRINGS.csv'

LIGHTGBM_SHAP_CB_PATH = 'data_sets/GBM_SHAP_COSTBURD.png'

HEATMAP_FEAT_SELECT = 'data_sets/feat_select_HEATMAP.png'

PATH_DF_CONCAT = 'data_sets/df_concat.csv'

