import streamlit as st
from scripts.utilities import *
from scripts.plots import *

def about_data():
    #new row
    row0_spacer1, row0_1, row0_spacer2 = st.columns(
        (.1, 3.2, .1)
    )
    with row0_1:
        st.title('About the Data')
        st.markdown('The following information is from the [DATA ANALYSIS METHODS DOCUMENT - HOUSING AFFORDABILITY & AVAILABILITY](https://tinyurl.com/2p9ftves) PDF file.')

    #new row
    row1_spacer1, row1_1, row1_spacer2 = st.columns(
        (.1, 3.2, .1)
    )
    with row1_1:
        st.subheader('Methods')
        st.markdown(''' 
            * Estimates for Mecklenburg County are apportioned to the City of Charlotte using the percentage of housing units by Public Use Microdata Area (PUMA) that are within the City of Charlotte. There are eight PUMAs that comprise Mecklenburg County. Apportionment factors retrieved from: http://mcdc.missouri.edu/websas/geocorr14.html.
                         
            * Each household is assigned to an AMI level based on household size (NP), total household income (HINCP), and the income limits for the corresponding year as established by the U.S. Department of Housing and Urban Development (HUD). Income limits retrieved from: https://www.huduser.gov/portal/datasets/il.html.
                        
            * Each rental unit is assigned as affordable to an AMI level based on gross rent (GRNTP), number of bedrooms (BDSP), and the household income adjustment factors by number of bedrooms as established by HUD. Adjustment factors retrieved from: https://www.huduser.gov/publications/pdf/CHAS_affordability_Analysis.pdf.
                * For units that are “Occupied without payment of rent” (TEN=4), gross rent is not available. Instead, the calculation uses the total monthly utility cost (WATP/12 + FULP/12 + ELEP + GASP).
                * For units that are “For rent” or “Rented, not occupied” (VACS=1, 2), gross rent is not available. Instead, the calculation uses Contract Rent (RNTP) plus an average utility adjustment factor calculated as the average total monthly utility cost for all rental units by year.
        ''')

        st.subheader('Limitations')
        st.markdown('''
            * This analysis relies on the definition of affordability from HUD, which defines an affordable dwelling as one that a household can obtain for 30 percent or less of its income. Affordability thresholds are tied to AMI. As Area Median Income rises across the region, a low-income household would be theoretically suited to a higher priced unit, even if their own household income did not change
            
            * Rent is only part of the affordability equation - e.g., transportation costs ($11,900 on average in Charlotte) are typically a household's second largest expense, and location within Charlotte is not reflected in this analysis
            
            * Due to lag in collection and release of PUMS data (PUMS estimates from the previous year are typically released in October), estimates may not reflect most current trends and market conditions
            
            * Data in the American Community Survey (ACS) products are estimates of the actual figures that would have been obtained by interviewing the entire population using the same methodology, and are subject to both sampling error (deviation of the of the selected sample from the true characteristics of the population) based on probability sampling and nonsampling error (occurs based on other factors such as coverage, non-response, data processing, estimation and analysis). Estimates made with PUMS data are subject to additional sampling error because the PUMS consists of a subset of the full ACS sample.
            
            * This analysis does not reflect: 
                * the use of Housing Choice Vouchers and other forms of tenant-based rental assistance
                * need for housing for the homeless population (not reflected in PUMS dataset)
                * the impacts of housing instability and the challenges that low-income households may have in accessing housing even when it is affordable and available
            
            * For a comprehensive assessment of housing instability and homelessness in Charlotte and Mecklenburg County, see local research on the Charlotte-Mecklenburg Housing & Homelessness Dashboard at: https://mecklenburghousingdata.org/research/local-reports/
        ''')