import altair as alt
import matplotlib.pyplot as plt
import copy
from scripts.utilities import *
from scripts.constants import *

#load data
df, cost_burd_results, df_concat = load_data()

#Basic histogram for exploration
def histogram(column, target, bin_feat):
    types = [DATA_TYPES_ALTAIR[get_datatype(x)] for x in [column, target]]
    hist = alt.Chart(df).mark_bar().encode(
        alt.X(column, type = types[0], bin=bin_feat),
        alt.Y('count()'),
        alt.Color(target, type = types[1])
    ).properties(title = column+" Distribution").interactive()
    return hist

#Basic scatter plot for exploration
def scatter(col1, col2, target):
    types = [DATA_TYPES_ALTAIR[get_datatype(x)] for x in [col1, col2, target]]
    scat = alt.Chart(df).mark_circle().encode(
        alt.X(col1, type = types[0]),
        alt.Y(col2, type = types[1]),
        alt.Color(target, type = types[2])
    ).properties(title = col1 + ' vs ' + col2).interactive()
    return scat

#Polar histogram for PUMA section
def puma_polar(column):
    PUMA = 'PUMA'
    dtype = 'N'
    temp_df = copy.deepcopy(df)
    temp_df[PUMA].replace(PUMA_CODES, inplace=True)
    
    base = alt.Chart(temp_df).encode(
        theta=alt.Theta(PUMA+dtype, stack=True),
        radius=alt.Radius('mean('+column+')', type='quantitative'),
        color= PUMA+dtype,
    ).properties(title = column + ' vs PUMA Area Code')
    
    c1 = base.mark_arc(innerRadius=10, stroke="#fff")

    return c1

def cost_burd_plot():
    source = pd.read_csv(PATH_DF_CLEAN_CLUSTERS)
    c1 = alt.Chart(source).mark_bar().encode(
        alt.X("AMI:O", bin=False, axis=alt.Axis(title='Area Median Income')),
        y='count()',
        color = 'COST_BURDALL:N'
    ).properties(height = 200, width = 250)

    c2 = alt.Chart(source).mark_bar().encode(
        alt.X("AFF_OCC:O", bin=False, axis=alt.Axis(title='Affordability')),
        y='count()',
        color = 'COST_BURDALL:N'
    ).properties(height = 200, width = 250)

    c3 = alt.Chart(source).mark_circle().encode(
        alt.X('AMI:O', axis=alt.Axis(title='Area Median Income')),
        alt.Y('AFF_OCC:O', axis=alt.Axis(title='Affordability')),
        color = 'COST_BURDALL:N'
    ).properties(height = 200, width = 250)

        
    return (c1|c2|c3)

def parallel_coord():
    fold = list(df_concat.columns[0:5])
    ttip = list(df_concat.columns[6:])
    c1 = alt.Chart(df_concat).transform_window(
        index='count()'
    ).transform_fold(
        fold
    ).mark_line().encode(
        x= alt.X('key:N', title = 'Features'),
        y='value:Q',
        color=alt.Color('COST_BURDALL', scale = alt.Scale(scheme = 'cividis')),
        detail='index:N',
        opacity=alt.value(0.5),
        tooltip = ['key:N', 'value:Q'] + ttip
    ).properties(width=600).interactive()

    c2 = alt.Chart(df_concat).transform_window(
        index='count()'
    ).transform_fold(
        fold
    ).mark_circle().encode(
        x= alt.X('key:N', title = 'Features'),
        y = alt.Y('value:Q'),
        color=alt.Color('COST_BURDALL', scale = alt.Scale(scheme = 'cividis')),
        tooltip = ['key:N', 'value:Q'] + ttip
    ).properties(width = 200).interactive()

    return c1|c2