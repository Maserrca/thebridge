import sys
import os
import numpy as np
import pandas as pd

def clean_1():
    df = pd.read_csv("homicides_data.csv")
    df = df.drop(['StateName', 'Subcircum', 'FileDate'], axis =1)
    df = df.drop_duplicates()
    df = df[df.ActionType != "Adjustment"]
    df.drop("ActionType", axis=1, inplace = True)
    df.reset_index(inplace = True)
    df_clean = df[['State','Solved', 'Year']]
    return df_clean
df_clean = clean_1()

def create_decade():
    df_clean['Decade'] = df_clean['Year']
    df_clean['Decade'] = df_clean['Decade'].apply(lambda x: str(x))
    df_clean['Decade'] = df_clean['Decade'].str[:3]
    df_clean['Zeros'] = '0'
    df_clean['Decade'] = df_clean['Decade'] + df_clean['Zeros']
    df_clean.drop('Zeros', axis= 1, inplace=True)
    df_clean.drop('Year', axis= 1, inplace=True)
    return df_clean
df_clean = create_decade()

def enc_solved():
    df_clean['Enc_Solved'] = df_clean['Solved']
    coding = df_clean['Enc_Solved']
    df_clean[['Enc_NoSolved', 'Enc_Solved']] = pd.get_dummies(coding)
    return df_clean
def sum_solved():
    agrupado = df_clean.groupby(['Decade', 'State']).sum()
    return agrupado
enc_solved()
agrupado = sum_solved()

def clean_population():
    population = pd.read_csv('population.csv', sep=";")
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
    return population
population = clean_population()

def arreglos():
    population2 = population.groupby(['Decade', 'Medidas']).sum()
    population3 = population2.stack().unstack("Medidas").reset_index().rename(columns={'Area':'State'})
    return population3
population3 = arreglos()

def converger():
    df = agrupado.reset_index()
    df['Decade']=df['Decade'].astype('int64')
    completo = df.merge(population3, on = ['Decade', 'State'])
    return completo 
completo = converger()

def operables(completo):
    completo['Population Density']=completo['Population Density'].apply(lambda x: x.replace('.',"").replace(',',"."))
    completo['Resident Population']=completo['Resident Population'].apply(lambda x: x.replace('.',""))
    completo['Population Density']=completo['Population Density'].astype('float')
    completo['Resident Population']=completo['Resident Population'].astype('int64')
    completo = completo[completo['Decade'] != 1970]
    return completo
completo = operables(completo)

#Hasta aqui limpiar data sobre el dataframe 1