# ------ Gráficos no plotly -------
import sys, os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

dirr = os.path.dirname
path = dirr(dirr(dirr(__file__)))
print(path)
sys.path.append(path)

print('prueba')


df_1 = pd.read_csv(path + os.sep + 'data' + os.sep  +'finaldf.csv')
df_US = pd.read_csv(path +  os.sep + 'data' + os.sep  + 'dfUS.csv')
df_curioso = pd.read_csv(path + os.sep + 'data' + os.sep  + 'curioso.csv')
df_matriz = pd.read_csv(path +  os.sep + 'data' + os.sep + 'paramatriz.csv')

def matriz(df_matriz):
    plt.subplots(figsize=(13, 10))
    matriz = sns.heatmap(df_matriz.corr(), vmin = -1, vmax = 1, annot = True, linewidths = .5)
    return matriz

def tendencia_total(df_1):
    return sns.lineplot(data=df_1, x="Decade", y="Casos Totales",label='Casos Totales').set_title('Asesinatos en EEUU')

def tendecia_casos(df_1):
    sns.lineplot(data=df_1, x="Decade", y="Enc_Solved", label='Casos Resueltos')
    sns.lineplot(data=df_1, x="Decade", y="Enc_NoSolved", label='Casos No Resueltos')
    plt.title('Asesinatos en EEUU')
    return plt.show()
