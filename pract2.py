import streamlit as st
import numpy as np
import pandas as pd


# Dataframe , Table, Matrices , Json

df=pd.DataFrame(np.random.randn(50,20))
st.dataframe(df)

de=pd.DataFrame(np.random.randn(50,20))
st.table(de)

st.metric("TCS Stock",value="237458.90",delta="20.60",delta_color="inverse")

st.json({'name':'don','age':20,'class':'cs'})

