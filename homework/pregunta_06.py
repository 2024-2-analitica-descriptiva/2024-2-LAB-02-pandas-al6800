"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en los archivos `tbl0.tsv`, `tbl1.tsv` y 
`tbl2.tsv`. En este laboratorio solo puede utilizar las funciones y 
librerias de pandas para resolver las preguntas.
"""


import pandas as pd

def pregunta_06():
    """
    Retorne una lista con los valores únicos de la columna `c4` del archivo
    `tbl1.tsv` en mayúsculas y ordenados alfabéticamente.

    Rta/
    ['A', 'B', 'C', 'D', 'E', 'F', 'G']
    """
    # Leer el archivo tbl1.tsv con el separador de tabulaciones
    tbl1 = pd.read_csv("files/input/tbl1.tsv", sep="\t")
    
    # Obtener los valores únicos de la columna 'c4' en mayúsculas
    valores_unicos = tbl1['c4'].str.upper().unique()
    
    # Ordenar alfabéticamente
    resultado = sorted(valores_unicos)
    
    return resultado

# Llamar a la función y mostrar el resultado
resultado = pregunta_06()
print(resultado)


