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

# For (data dictionary -> altair) type conversion
DATA_TYPES_ALTAIR = {
    'C' : 'nominal',
    'N' : 'quantitative'
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

PATH_DF_CLEAN_CLUSTERS = 'data_sets/df_cleaned_clusters.csv'

PATH_COST_BURD_RESULTS = 'data_sets/cost_burd_results.csv'