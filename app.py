import pandas as pd
import numpy as np
import streamlit as st
import plotly.express as px
import plotly.io as pio

df = pd.read_csv("vehicles_us.csv") 

st.header('Market of Sales Vehicles ')
st.write("Here is the Analysis of Vehicle Sales ")

# Handling missing values
df['paint_color']= df['paint_color'].fillna('unknown') # Replacing missing paint
df['is_4wd'] = df['is_4wd'].fillna(0) # Replacing 2wd by 0
#Replacing missing model year values grouped with model
df['model_year'] = df['model_year']. fillna(df.groupby(['model'])['model_year'].transform('median'))
# Réplacing missing odometer values grouped with model
df['odometer'] = df['odometer'].fillna(df.groupby(['model'])['odometer'].transform('median'))
# Replacing missing cylinders values grouped with model
df['cylinders'] = df['cylinders'].fillna(df.groupby(['model'])['cylinders'].transform( 'median' ))

if st.checkbox("Show data"):
    st.write(df.head())



#histogram
fig = px.histogram(df, x="model")
st.plotly_chart(fig)

#scatter plot
fig = px.scatter(df, x="fuel", y="type")
st.plotly_chart(fig)

# Visualizing the values
fig_price = px.histogram(df, x="price", title="price Distribution")
fig_price.update_layout(yaxis_title = "Number of Cars")
st.plotly_chart(fig_price)
fig_odometer = px.scatter(df, x="odometer", y="price",title= "Price vs Odometer- Reading")
st.plotly_chart(fig_odometer)