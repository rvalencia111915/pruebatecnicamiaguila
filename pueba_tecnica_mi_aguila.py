"""
Created on Wed Aug 25 20:10:28 2021
@author: Raul Estiven Valencia Toro
"""
# Importar librerias necesarias
import pandas as pd
import requests as rq
import pyodbc
import sqlalchemy as sa
import urllib
import configparser

# Archivo de configuracion de variables
config = configparser.ConfigParser()
config.read('config.ini')

# Funcion para leer archivo
def read_data(path, format_file):
    if format_file == 'csv' :
        df = pd.read_csv(path, decimal = '.')
    elif format_file == 'json' :
        df = pd.read_json(path, lines = True)
    return df

# Funcion para integrar API
def generate_post_code(lon, lat):
    params = {'lon' : lon, 'lat' : lat, 'limit' : 1, 'radius':15000}
    response = rq.get(url, params = params)
    
    response = response.json()
    response = response['result'][0]
    return response

if __name__ == '__main__':
    
    # Carga de variables de archivo de configuracion    
    servidor = config['DEFAULT']['SERVER']
    bddatos = config['DEFAULT']['BD']
    usuario = config['DEFAULT']['USER']
    clave = config['DEFAULT']['PASS']
    url = config['DEFAULT']['URL']
    file = config['DEFAULT']['FILE']
    load_type = config['DEFAULT']['LOAD_TYPE']
    
    # Lectura de archivo
    df_coordenadas = read_data(file, 'csv')
    # Se realiza seleccion de filas por temas de rendimiento de computo
    #df_coordenadas = df_coordenadas.head(30)
    
    # Consumo de API y adicion de nuevas columnas
    df_coordenadas['response'] = df_coordenadas.apply( lambda x : generate_post_code(x.lon,x.lat), axis=1)
    df_coordenadas = pd.concat([df_coordenadas,df_coordenadas['response'].apply(pd.Series)],axis=1).drop('response',axis=1)
    
    # Guardar en BD en caso de ser necesario
    if load_type == 'bd':
        conn= urllib.parse.quote_plus('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+servidor+';DATABASE='+bddatos+';UID='+usuario+';PWD='+ clave)
        engine = sa.create_engine('mssql+pyodbc:///?odbc_connect={}'.format(conn))

        df_coordenadas.to_sql("postcode", engine, schema='dbo', if_exists='append')
    else:
        # Guardar dataframe en csv en la ruta raiz e imprimir resultados
        df_coordenadas.to_csv('detailpostcode.csv', index=False)
        print(df_coordenadas, df_coordenadas.dtypes)
        
    
    