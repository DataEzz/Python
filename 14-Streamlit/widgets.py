import streamlit as st
import pandas as pd

st.title("Streamlit Text Input")
name = st.text_input("Enter your name:")

## SLIDER
age = st.slider("Select your age:",0,100,25)
st.write(f"Your age is {age}.")

## SELECTBOX
options = ["Python","Java","C++","JavaScript"]
choice = st.selectbox("Choose your favourite language:",options)
st.write(f"You select {choice}.")

if name:
    st.write(f"Hello, {name}")
    

data = {
    "Name":['Ajit','Akhilesh','Aman','Kanchan'],
    "Age":[20,25,20,18],
    "City":["Mumbai",'Bangalore','Delhi','Hyderabad']
}

df = pd.DataFrame(data)
df.to_csv('sampledata.csv')
st.write(df)

uploaded_file = st.file_uploader("Choose a CSV file",type = 'csv')
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write(df)