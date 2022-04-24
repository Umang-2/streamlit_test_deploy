import streamlit as st
from pathlib import Path
import pandas as pd
# df = pd.read_csv('pytube_eg.csv')
# st.write(df)

st.write('Test successful!!')
path_df = Path(__file__).parents[0]/ 'folder/pytube_eg.csv'
st.write(path_df)
# 'GarretBurhennData/Garret_Burhenn_Pitches.csv'
df = pd.read_csv(path_df)
st.write(df)
