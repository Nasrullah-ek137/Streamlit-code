import streamlit as st
import numpy as np
import pandas as pd

# download_button
file=open("selfi.jpeg","rb")
btn=st.download_button(
    label="Download here",
    data=file,
    file_name="selfi.jpeg",
    mime="image/jpg"
)
st.write(btn)

# Checkbox
check=st.checkbox("Do you Agree this term and condition")
if check=="True":
    st.write("You are Agree")
else:
    st.write("Tu ja re..")

# Radio
option=st.radio(
    label="Please Order your food.",
    options=("Pizza","rice","Biryani","Kabab")
)
if option=="Pizza":
    st.write("you choosed Pizza")
elif option=="rice":
    st.write("you choosed Rice")
elif option=="Biryani":
    st.write("you choosed Biryani")
elif option=="Kabab":
    st.write('you choosed Kebab')

# Selectbox
location=st.selectbox(
    label="Where do you live ?",
    options=("Palestine","Iran","India")
)
if location=="Palestine":
    st.write("you live in Palestine")
elif location=="Iran":
    st.write("you live in Iran")
elif location=="India":
    st.write("MERAH BHARAT MAHAN..")