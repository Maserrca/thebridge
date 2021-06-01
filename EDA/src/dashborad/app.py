import re
import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
from PIL import Image
import requests
import os

header = st.beta_container()
dataset = st.beta_container()


path = os.path.dirname(__file__)
df = None
    
menu = st.sidebar.selectbox('Menu:',
            options=["Welcome","Dataset", "Visualization", "Flask"])

with header:
    st.title('US Homicides EDA')

if menu == 'Welcome':
    st.title('Welcome!')
    st.write('This proyect will look into the cases of homicide in the US from 1980 to 2019')

if menu == 'Dataset':
    st.write('The original dataset is from the Murder Accountability Proyect by Thomas K. Hargrove')

if menu == "Visualización":
    pass

if menu == "":
    r = requests.get("http://localhost:8080/give_me_id?token_id=R70423563").json()
    df = pd.DataFrame(r)
    st.write(df)

if menu == "Países":
    r = requests.get("http://localhost:8080/give_me_id?token_id=R70423563").json()
    df = pd.DataFrame(r)
    st.write(df)