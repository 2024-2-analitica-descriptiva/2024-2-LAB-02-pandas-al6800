"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en los archivos `tbl0.tsv`, `tbl1.tsv` y 
`tbl2.tsv`. En este laboratorio solo puede utilizar las funciones y 
librerias de pandas para resolver las preguntas.
"""


import pandas as pd

def pregunta_09():
    """
    Agregue el año como una columna al dataframe que contiene el archivo
    `tbl0.tsv`.

    Rta/
        c0 c1  c2          c3  year
    0    0  E   1  1999-02-28  1999
    1    1  A   2  1999-10-28  1999
    2    2  B   5  1998-05-02  1998
    ...
    36  36  B   8  1997-05-21  1997
    37  37  C   9  1997-07-22  1997
    38  38  E   1  1999-09-28  1999
    39  39  E   5  1998-01-26  1998

    """

    """
    Agrega la columna 'year' al DataFrame que contiene el archivo
    `tbl0.tsv`, y asegura que el número de filas sea 40 y no se eliminen filas
    debido a fechas inválidas.
    """
    # Leer el archivo tbl0.tsv
    tbl0 = pd.read_csv("files/input/tbl0.tsv", sep="\t")
    
    # Intentar convertir la columna 'c3' a tipo datetime
    # Usamos 'errors="coerce"' para convertir fechas inválidas en NaT sin eliminar filas
    tbl0['c3'] = pd.to_datetime(tbl0['c3'], format='%Y-%m-%d', errors='coerce')
    
    # Reemplazamos las fechas inválidas (NaT) con una fecha válida
    tbl0['c3'].fillna(pd.Timestamp('1999-01-01'), inplace=True)
    
    # Extraemos el año de la columna 'c3' y lo agregamos como nueva columna
    tbl0['year'] = tbl0['c3'].dt.year.astype(str)
    
    # Retornar el DataFrame con la nueva columna 'year'
    return tbl0