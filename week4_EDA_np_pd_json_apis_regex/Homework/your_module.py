# This file represents your module.
# Write the code...
import pandas as pd
import numpy as np

def mean_visualization():
    """Draw the mean in a plot"""
    return None

def show_list_of_elements(lista):
    # TODO 
    pass


if __name__ == '__main__':
    x = mean_visualization()
    print(x)

'''
funcion  de acceso path para import 
'''
def get_root_path(n):
    path = os.getcwd() # para notebook ||| __file__ --> para .py
    for i in range(n):
        path = os.path.dirname(path)
    print(path)
    sys.path.append(path)

# n --> es el número de veces que se tiene que hacer os.path.dirname 
# si en .ipynb notebook es 5 entonces en .py usando __file__ es 4. 
get_root_path(n=5)

# Con esta función leemos los datos y lo pasamos a un DataFrame de Pandas
def sql_query(query):
    curs.execute(query)
    datos_query = curs.fetchall()
    col_names = [description[0] for description in curs.description]
    return pd.DataFrame(datos_query,columns=col_names)
sql_query(query)