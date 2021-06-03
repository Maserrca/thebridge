import sys, os
import numpy as np
import pandas as pd

pud = os.path.dirname
din=pud(pud(pud(__file__)))
sys.path.append(pud) 

def clean_1(csv):
    df = pd.read_csv(din + os.sep + 'data' + os.sep + csv)
    df = df.drop(['StateName', 'Subcircum', 'FileDate'], axis =1)
    df = df.drop_duplicates()
    df = df[df.ActionType != "Adjustment"]
    df.drop("ActionType", axis=1, inplace = True)
    df.reset_index(inplace = True)
    df_clean = df[['State','Solved', 'Year']]
    df_clean['Decade'] = df_clean['Year']
    df_clean['Decade'] = df_clean['Decade'].apply(lambda x: str(x))
    df_clean['Decade'] = df_clean['Decade'].str[:3]
    df_clean['Zeros'] = '0'
    df_clean['Decade'] = df_clean['Decade'] + df_clean['Zeros']
    df_clean.drop('Zeros', axis= 1, inplace=True)
    df_clean.drop('Year', axis= 1, inplace=True)
    df_clean['Enc_Solved'] = df_clean['Solved']
    coding = df_clean['Enc_Solved']
    df_clean[['Enc_NoSolved', 'Enc_Solved']] = pd.get_dummies(coding)
    return df_clean

def sum_solved(df_clean):
    agrupado = df_clean.groupby(['Decade', 'State']).sum()
    return agrupado



def clean_population(csv):
    population = pd.read_csv(din + os.sep + 'data' + os.sep + csv, sep=";")
    population.rename(columns={'Unnamed: 0':'Area'},inplace=True)
    population.set_index('Area', inplace = True)
    population.drop(population.filter(regex='Rank').columns, axis=1, inplace = True)
    population.drop(population.filter(regex='2020').columns, axis=1, inplace = True)
    population = population.T
    population = population.iloc[::-1]
    population['Decade'] = [1970,1970,1980,1980,1990,1990,2000,2000,2010,2010]
    col_name="Decade"
    first_col = population.pop("Decade")
    population.insert(0, col_name, first_col)
    population.reset_index(level= None, inplace=True)
    population.set_index('Decade', inplace = True)
    population.rename(columns = {'index': 'Medidas'}, inplace=True)
    population['Medidas'] = population['Medidas'].str[:-12]
    population.reset_index(level='Decade', inplace=True)
    population2 = population.groupby(['Decade', 'Medidas']).sum()
    population3 = population2.stack().unstack("Medidas").reset_index().rename(columns={'Area':'State'})
    return population3


def converger(agrupado,population3):
    df = agrupado.reset_index()
    df['Decade']=df['Decade'].astype('int64')
    completo = df.merge(population3, on = ['Decade', 'State'])
    return completo 


def operables(completo):
    completo['Population Density']=completo['Population Density'].apply(lambda x: x.replace('.',"").replace(',',"."))
    completo['Resident Population']=completo['Resident Population'].apply(lambda x: x.replace('.',""))
    completo['Population Density']=completo['Population Density'].astype('float')
    completo['Resident Population']=completo['Resident Population'].astype('int64')
    completo['Enc_NoSolved'] = completo['Enc_NoSolved'].astype('int64')
    completo['Enc_Solved'] = completo['Enc_Solved'].astype('int64')
    completo = completo[completo['Decade'] != 1970]
    completo.reset_index(inplace = True, drop=True)
    return completo #Para la matriz de correlación
    
def sumatorios(completo):
    completo['Casos Totales'] = completo['Enc_Solved'] + completo['Enc_NoSolved']
    completo['Porcentaje Resueltos'] = (completo['Enc_Solved'] / completo['Casos Totales']) * 100
    completo['Porcentaje No Resueltos'] = (completo['Enc_NoSolved'] / completo['Casos Totales']) * 100
    df_1 = completo
    return df_1 #Para los gráficos de porcentaje



#Hasta aqui limpiar data sobre el dataframe 1

#----- Ahora dataframe 2 -------
def para_us(df_1):
    df_US = df_1.groupby(['Decade', 'State']).sum()
    return df_US #Para los graficos agrupados


#-------Datos curiosos ------------
def clean_curious(csv):
    df = pd.read_csv(din + os.sep + 'data' + os.sep + csv)
    df = df.drop(['StateName', 'Subcircum', 'FileDate'], axis =1)
    df = df.drop_duplicates()
    df = df[df.ActionType != "Adjustment"]
    df.drop("ActionType", axis=1, inplace = True)
    df.reset_index(inplace = True)
    df_curious = df[['State','OffSex','Weapon', 'Circumstance']]
    return df_curious #Para los datos curiosos
