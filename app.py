import streamlit as st

# working with title
st.title("Shanu tutorials..")

#display header and subheader
st.header("This is header")
st.subheader("This is subheader ")

# text
st.text("hello shanu")

# Display markdown
st.markdown("### this is markdown")

# display error
st.success("SUCCESSFUL")
st.info("INFORMATION")
st.warning("WARNING")
st.error("ERROR")
st.exception("NameError('name three not defined')")

# get helip information
st.help(range)

#  writing txt and super fxn
st.write("Text with write")
st.write(range(10))

# Displaying img
from PIL import Image
img=Image.open("selfi.jpeg")
st.image(img,width=300,caption="simple image")

# Working with video
vid_file=open("Khairiyat Song.mp4","rb").read()
st.video(vid_file)

# working with audio
aud_file=open("audio.opus","rb").read()
st.audio(aud_file,format='audio/mp3')

# checkbox
if st.checkbox("Show/Hide"):
    st.text("Showing or hiding widget")

# Radio
statue=st.radio("what is your status",("Active","InActive"))
if statue=="Active":
    st.success("You are Active")
else:
    st.warning("InActive,Activate")

# selectbox
occupation=st.selectbox("Your occupation",["programmer","developer","Doctor"
                                           ,"berosjir"])
st.write("you selected this option:-",occupation)

# multiselect
location=st.multiselect("Where do you work ?",("london","new york",
                                               "delhi","mumbai"))
st.write("you selected",len(location),"location")

# slider
level=st.slider("what is your level ?",1,5)

# button
st.button("simple button")

# text input
fn=st.text_input("Enter your name:","e.g: shanu")

# text area
msg=st.text_area("Enter your message:","type here..")
if st.button("Submit"):
    result=msg.title()
    st.success(result)

# date input
import datetime
today=st.date_input("today is:",datetime.datetime.now())
time=st.time_input("time is:",datetime.time())

# display json
st.write("Display JSON")
st.json({'name':"shanu",'gender':'male'})

# display row code
with st.echo():
    # This is comment line
    import pandas as pd
    df=pd.DataFrame()

# dataframe
st.dataframe(df)

# table
st.table(df)

# sidebar
st.sidebar.header("Home")
st.sidebar.title("This is home sidebar")

# spinner
import time
with st.spinner("waiting.."):
    time.sleep(4)
st.success("Finished")

# balloons
st.balloons()

# progress bar
my_bar=st.progress(2)