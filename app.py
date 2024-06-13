import streamlit as st
import pandas as pd

@st.cache_data
def load_data():
    train = pd.read_csv('BBDDs/diamonds_train.csv')
    test = pd.read_csv('BBDDs/diamonds_test.csv')
    return train, test

st.title('Diamond Price Predictor')

train, test = load_data()

st.subheader('Diamonds Train Data')
st.write(train.head())

st.subheader('Diamonds Test Data')
st.write(test.head())
