import streamlit as st
import pandas as pd

st.title("Hi, I am K.T.Huda :wave:")
st.subheader("And I want to take your interview")


name = st.text_input("Enter your name: ")
adr = st.text_input("Enter your address: ")
classd=st.selectbox("Enter your class: ",(1,2,3,4,5,6,7,8,9,10,11,12,))
ac=st.text_input("Enter your fav anime/cartoon: ")

button = st.button("Done")
if button :
    st.markdown(f"""Name: {name},Address: {adr},class: {classd},Fav anime/cartoon: {ac}.""")
    