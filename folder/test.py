import streamlit as st
from pathlib import Path
import pandas as pd
# df = pd.read_csv('pytube_eg.csv')
# st.write(df)

st.write('Test successful!!')
df = Path(__file__).parents[0]/ 'folder/pytube_eg.csv'
# 'GarretBurhennData/Garret_Burhenn_Pitches.csv'
st.write(df)
