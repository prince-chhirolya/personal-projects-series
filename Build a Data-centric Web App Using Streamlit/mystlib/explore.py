# Write Task 6 code here
import streamlit as st
import pandas as pd

def run(df):
   st.title("Single-column Selection")
   # The following line allows single col selection
   col = st.selectbox('select one column:', df.columns)
   st.write('You selected:', col)
   # Show dataframe with the selected columns
   st.write(df[col].unique())

   st.title("Multi-column Selection")
   # The following line allows multiple col selection
   cols = st.multiselect('select column(s):', df.columns, default = [])
   st.write('You selected:', cols)
   # show dataframe with the selected columns
   st.write(df[cols])