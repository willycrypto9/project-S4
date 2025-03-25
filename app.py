import streamlit as st 
import pandas as pd
import numpy as np
import plotly.express as px

df = pd.read_csv("vehicles_us.csv") 

st.header('Market of Sales Vehicles ')
st.write("Here is the Analysis of Vehicle Sales ")

#histogram
fig = px.histogram(df, x="model")
st.plotly_chart(fig)

#scatter plot
fig = px.scatter(df, x="fuel", y="type")git status
st.plotly_chart(fig)

if st.checkbox("Show data"):
    st.write(df.head())