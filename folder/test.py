import streamlit as st
from pathlib import Path
import pandas as pd
import numpy as np
# df = pd.read_csv('pytube_eg.csv')
# st.write(df)

st.write('Test successful!!')
path_df = Path(__file__).parents[0]/ 'pytube_eg.csv'
st.write(path_df)
# 'GarretBurhennData/Garret_Burhenn_Pitches.csv'
df = pd.read_csv(path_df)
st.write(df)

path_np_1 = Path(__file__).parents[0]/ 'reverse_target_word_index.npy'
path_np_2 = Path(__file__).parents[0]/ 'target_word_index.npy'
path_np_3 = Path(__file__).parents[0]/ 'reverse_source_word_index.npy'
reverse_target_word_index = np.load(path_np_1,allow_pickle='TRUE').item()
target_word_index = np.load(path_np_2,allow_pickle='TRUE').item()
reverse_source_word_index = np.load(path_np_3,allow_pickle='TRUE').item()

st.write(reverse_target_word_index[1])
st.write(target_word_index['के'])
st.write('Lol',reverse_source_word_index[1])
