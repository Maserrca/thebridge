import streamlit as st
from PIL import Image
import mysql.connector
""" Siempre que veas 'pass' es un TO-DO (por hacer)"""

"""1"""
# Haz que se pueda importar correctamente estas funciones que están en la carpeta utils/

import sys, os
'''
dir = os.path.dirname
path = dir(dir(dir(os.path.abspath(__file__))
'''



from utils.stream_config import draw_map
from utils.dataframes import load_csv_for_map
menu = st.sidebar.selectbox('Menu:',
            options=["No selected", "Load Image", "Map", "API", "MySQL", "Machine Learning"])

if menu == "No selected": 
    """2"""
    # Pon el título del proyecto que está en el archivo "config.json" en /config
    st.title(pass)
    # Pon la descripción del proyecto que está en el archivo "config.json" en /config
    st.write(pass)
    
if menu == "Load Image": 
    """3"""
    # Carga la imagen que está en data/img/happy.jpg
    image = Image.open(pass)  
    st.image (image,use_column_width=True)

if menu == "Map":
    """4"""
    # El archivo que está en data/ con nombre 'red_recarga_acceso_publico_2021.csv'
    csv_map_path = pass
    df_map = load_csv_for_map(csv_map_path)
    draw_map(df_map)

if menu == "API":
    r = requests.get("http://localhost:6060/").json()
    df = pd.DataFrame(r)
    st.write(df)

if menu == "Australia Fire":
    with(open(dir(path1) + os.path + 'config' + os.sep + 'bd_info.json')) as json_file:
        
    
    st.write(df)

    # 1. Conecta a la BBDD
    # 2. Obtén, a partir de sentencias SQL (no pandas), la información de las tablas que empiezan por 'fire_archive*' (join)
    # 3. Entrena tres modelos de ML diferentes siendo el target la columna 'fire_type'. Utiliza un pipeline que preprocese los datos con PCA. Usa Gridsearch.  
    # 4. Añade una entrada en la tabla 'student_findings' por cada uno de los tres modelos. 'student_id' es EL-ID-DE-TU-GRUPO.
    # 5. Obtén la información de la tabla 'fire_nrt_M6_96619' y utiliza el mejor modelo para predecir la columna target de esos datos. 
    # 6. Usando SQL (no pandas) añade una columna nueva en la tabla 'fire_nrt_M6_96619' con el nombre 'fire_type_EL-ID-DE-TU-GRUPO'
    # 7. Muestra por pantalla en Streamlit la tabla completa (X e y)
    pass



