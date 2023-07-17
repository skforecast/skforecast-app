import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from skforecast import __version__ as skforecast_version
from skforecast.ForecasterAutoreg import ForecasterAutoreg
from sklearn.ensemble import RandomForestRegressor

st.title('Forecasting with skforecast')
st.write(f"This is a demo of the [skforecast {skforecast_version}]()")


st.sidebar.markdown("## Controls")
st.sidebar.markdown("You can **change** the values to change the *chart*.")
x = st.sidebar.slider('Slope', min_value=0.01, max_value=0.10, step=0.01)
y = st.sidebar.slider('Noise', min_value=0.01, max_value=0.10, step=0.01)

n_est = st.sidebar.slider("n_est", min_value=1, max_value=5_000, step=1)

data = st.sidebar.file_uploader("Upload a Dataset", type=["csv", "txt"])
demo = st.sidebar.checkbox("Use Demo Dataset")

if demo:
    url = (
    'https://raw.githubusercontent.com/JoaquinAmatRodrigo/skforecast/master/'
    'data/h2o.csv'
    )
    data = pd.read_csv(url, sep=',', header=0, names=['y', 'datetime'])
    data['datetime'] = pd.to_datetime(data['datetime'], format='%Y-%m-%d')
    data = data.set_index('datetime')
    data = data.asfreq('MS')
    data = data['y']
    data = data.sort_index()

# Data partition train-test
# ==============================================================================
end_train = '2005-06-01 23:59:00'
print(
    f"Train dates : {data.index.min()} --- {data.loc[:end_train].index.max()}  " 
    f"(n={len(data.loc[:end_train])})")
print(
    f"Test dates  : {data.loc[end_train:].index.min()} --- {data.index.max()}  "
    f"(n={len(data.loc[end_train:])})")

# Plot
# ==============================================================================
fig, ax = plt.subplots(figsize=(7, 3))
data.loc[:end_train].plot(ax=ax, label='train')
data.loc[end_train:].plot(ax=ax, label='test')
ax.legend()
st.pyplot(fig)