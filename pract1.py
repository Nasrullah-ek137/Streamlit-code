import streamlit as st
import numpy as np
import pandas as pd

st.title("Hello this is shanu page..")
st.header("This line is heading line")
st.subheader("This line is subheader")
st.text("this is text line")

st.write("Hello **How** are you 'fine'")

# dict practice
dic={'name':'shanu','age':20,'married':'Randwa'}
st.write(dic)

# code fxn
code="""def hello():
           print(np.array[1,2,3][4,5,6])"""
st.code(code,language="python")

# pandas
df=pd.read_csv(r"payment.csv")
st.write(df)
