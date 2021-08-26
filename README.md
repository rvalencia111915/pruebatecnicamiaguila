# Prueba técnica Mi Águila
Se desarrollo un script en Python llamado **pueba_tecnica_mi_aguila.py** para cumplir con la funcionalidad del reto propuesto en la prueba técnica. 
- Se crea la función read_data() que recibe dos parámetros, el nombre y el tipo del archivo, valida el tipo de formato y lo guarda en un dataframe.

![](https://github.com/rvalencia111915/pruebatecnicamiaguila/blob/main/Images/function_read_data.JPG)

- Se crea la función generate_post_code() que recibe dos parámetros, la longitud y la latitud, utilizando el método get de la librería requests consumo el API enviando los parámetros requeridos.

![](https://github.com/rvalencia111915/pruebatecnicamiaguila/blob/main/Images/function_generate_post_code.JPG)

- Se cargan las variable desde el archivo de configuración definido, esto para no utilizar valores quemados en el código.

![](https://github.com/rvalencia111915/pruebatecnicamiaguila/blob/main/Images/archivo_configuracion_variables.JPG)


![](https://github.com/rvalencia111915/pruebatecnicamiaguila/blob/main/Images/carga_variables.JPG)

- Utilizando la función read_data() antes creada se realiza la lectura del archivo y se guarda en un dataframe. 
- Utilizando la función generate_post_code se obtiene la data requerida para cada registro.

![](https://github.com/rvalencia111915/pruebatecnicamiaguila/blob/main/Images/lectura_archivo_consumo_API.JPG)

- Utilizando las librerías pyodbc y sqlalchemy se tiene la opción de guardar el resultado en una base de datos de SQL, además se guarda el dataframe a través del método to_csv () en un archivo csv ubicado en la ruta raíz de la solución.

![](https://github.com/rvalencia111915/pruebatecnicamiaguila/blob/main/Images/guardar_resultados.JPG)

- Resultados obtenidos

![](https://github.com/rvalencia111915/pruebatecnicamiaguila/blob/main/Images/resultados.JPG)
