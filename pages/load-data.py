
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


DATE_COLUMN = 'date/time'
DATA_URL = (
    'https://raw.githubusercontent.com/JoaquinAmatRodrigo/skforecast/master/'
    'data/h2o.csv'
)


st.title('Load data')

@st.cache_data
def load_data():
    data = data = pd.read_csv(DATA_URL, sep=',', header=0)
    return data

data = load_data()

st.write(data)