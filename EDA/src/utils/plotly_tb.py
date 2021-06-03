#--------------Gráficos de plotly---------------
import sys, os
import numpy as np
import pandas as pd
import plotly.express as px

dirr = os.path.dirname
path = dirr(dirr(dirr(__file__)))
sys.path.append(path)

print('prueba')

df_1 = pd.read_csv(path + os.sep + 'data' + os.sep  +'finaldf.csv')
df_US = pd.read_csv(path +  os.sep + 'data' + os.sep  + 'dfUS.csv')
df_curioso = pd.read_csv(path + os.sep + 'data' + os.sep  + 'curioso.csv')
df_matriz = pd.read_csv(path +  os.sep + 'data' + os.sep + 'paramatriz.csv')

def barras(df_1):
    state1 = px.bar(df_1, x="State", y="Porcentaje Resueltos", color="Decade", title="Casos resueltos por Estado y década")
    state1.write_html(path + os.sep + 'img' + os.sep + "midibuji.html")
    state1.write_image(path + os.sep + 'img' + os.sep + "midibuji.png")
    state1.show()
    return state1

def weapons(df_curioso):
    fig1 = px.pie(df_curioso, names='Weapon', title='Murder weapons in the US')
    fig1.write_html(path + os.sep + 'img' + os.sep + "weapons.html")
    fig1.write_image(path + os.sep + 'img' + os.sep + "weapons.png")
    fig1.show(fig1)
    return fig1
def circunstancia(df_curioso):
    fig2 = px.pie(df_curioso, names='Circumstance', title='How people is killed in the US')
    fig2.write_html(path + os.sep + 'img' + os.sep + "circunstancia.html")
    fig2.write_image(path + os.sep + 'img' + os.sep + "circunstancia.png")
    fig2.show(fig2)
    return fig2

#Añadidos en img 