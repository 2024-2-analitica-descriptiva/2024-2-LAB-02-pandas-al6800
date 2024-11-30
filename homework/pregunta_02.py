"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en los archivos `tbl0.tsv`, `tbl1.tsv` y 
`tbl2.tsv`. En este laboratorio solo puede utilizar las funciones y 
librerias de pandas para resolver las preguntas.
"""


import pandas as pd

def pregunta_02():
    """
    ¿Cuál es la cantidad de columnas en la tabla `tbl0.tsv`?

    Rta/
    4
    """
    # Leer el archivo tbl0.tsv desde la carpeta especificada
    tbl0 = pd.read_csv("files/input/tbl0.tsv", sep="\t")
    # Contar el número de columnas y retornarlo
    return tbl0.shape[1]

# Llamar a la función y mostrar el resultado
resultado = pregunta_02()
print(resultado)
