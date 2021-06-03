import os
import sys
dirr = os.path.dirname
path = dirr(dirr(dirr(__file__)))
print(path)
sys.path.append(path)
import re
import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
import requests

import plotly.express as px
from src.utils.plotly_tb import *
from src.utils.visualization_tb import *
from src.utils.plotly_tb import *

header = st.beta_container()
dataset = st.beta_container()
df = None




    
menu = st.sidebar.selectbox('Menu:', options=["Welcome","Dataset", "Visualization", "Flask"])
submenu = st.sidebar.selectbox('Submenu:', options=["Matriz de Correlación", "Distribución por estado", "Tendencia Total"])

with header:
    st.title('US Homicides EDA')

if menu == 'Welcome':
    st.title('Welcome!')
    st.write('This proyect will look into the cases of homicide in the US from 1980 to 2019')

if menu == 'Dataset':
    st.write('The original dataset is from the Murder Accountability Proyect by Thomas K. Hargrove')
    r = requests.get("http://localhost:6060/give_me_id?token_id=M53994161").json()
    df = pd.DataFrame(r)
    st.write(df)

if menu == "Visualization":
    if submenu == "Matriz de Correlación":
        matriz =Image.open(path + os.sep + 'img' + os.sep + 'matriz.png')
        st.image(matriz,use_column_width=True)
    if submenu == "Distribución por estado":
        st.plotly_chart(barras(df_1), use_column_width=False)
    if submenu == "Tendencia Total":
        image1 =Image.open(path + os.sep + 'img' + os.sep + 'graf1.png')
        st.image(image1,use_column_width=True)
    pass
