import altair as alt
import matplotlib.pyplot as plt
import copy
from scripts.utilities import *
from scripts.constants import *

#load data
df, cost_burd_results = load_data()

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
    temp_df = copy.deepcopy(df)
    temp_df[PUMA].replace(PUMA_CODES, inplace=True)
    
    base = alt.Chart(temp_df).encode(
        theta=alt.Theta(PUMA+":N", stack=True),
        radius=alt.Radius('mean('+column+')', type='quantitative'),
        color= PUMA+":N",
    ).properties(title = column + ' vs PUMA Area Code')
    
    c1 = base.mark_arc(innerRadius=10, stroke="#fff")

    return c1