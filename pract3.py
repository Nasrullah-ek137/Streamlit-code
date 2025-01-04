import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import streamlit as st

# Area_chart
df=pd.DataFrame(np.random.randn(10,2),columns=['prices','etc'])
st.area_chart(df)
st.area_chart(df,y=["etc"])

# line_chart
st.line_chart(df)

# Bar_chart
st.bar_chart(df)

# matplotlib Scatter
fig,ax=plt.subplots()
ax.scatter(np.arange(10),np.arange(10)**2)
st.pyplot(fig)

# Map_chart
places=pd.DataFrame({
    "lat":[19.07,28.64],
    "lon":[72.87,77.21]
})
st.map(places)