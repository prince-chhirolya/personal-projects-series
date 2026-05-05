# Write Task 1 code here
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import pydeck as pdk

# Add Task 5,6,7,9 and 11 import here
import preprocess
from mystlib import explore
from mystlib import viewOnMap
from mystlib import plot2D
from mystlib import plot3D

# Write Task 2 code here
df = pd.read_csv('/usercode/dataset.csv')


# Write Task 3 and 4 code here
st.header("My First Streamlit Application")

# Set page configuration
st.set_page_config(layout = "wide", page_title = "Streamlit Data-centric App", page_icon = ":taxi:")


# Provide a list of functionalities to select from
message = """
        __Select a functionality from the list below__
        """
with st.sidebar:
    st.markdown(message)
    page = st.selectbox('Select:',
        ['View Data Using Dropdowns',
        'Visualize Data on a Map',
        '2D Charts and Histograms', 
        '3D Charts and Histograms']) 


# Write Task 5 code here
# Preprocess the dataset
preprocess.run(df)

# Do some more processing.
df = preprocess.lat_lon_conversion("mydataset.csv")

# Display interactive dataframe
st.dataframe(df)

# Write Task 6, 7, 9 and 11 code here
if page == 'View Data Using Dropdowns':
    explore.run(df)
elif page == 'Visualize Data on a Map':
    viewOnMap.run(df)

elif page == '3D Charts and Histograms':
    plot3D.run(df)
