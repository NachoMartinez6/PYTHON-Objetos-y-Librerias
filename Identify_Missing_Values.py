# -*- coding: utf-8 -*-
"""
Created on Thu May 20 18:35:19 2021

@author: Nacho
"""



# =============================================================================
""" how to handle missing values """
# =============================================================================


import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
import seaborn as sns


df = pd.read_csv("property_data.txt")
# df = pd.read_csv("property_data.txt", na_values=["--","na","NA", "n/a"])

df = df.drop("PID", axis=1)


# print(df.columns.values)
# print(df.dtypes.sort_values())

""" Que tipo de features tengo?

St_num: Numero de la calle
ST_Name: Nombre de la calle
OWN_OCCUPIED: Ocupado por el propietario
Num_Bedrooms: nº habitaciones
Num_bathroom: nº aseos
Sq_ft: Pies cuadrados



Que tipo de features necesito?



St_num: Int 
St_name: string
OWN_OCCUPIED: string 
Num_Bedrooms: obj --> int
Num_bathroom: obj --> int
Sq_ft: obj --> int or float


"""


# print(df.isnull().sum().sort_values(ascending=False))
# print(round(df.isnull().sum().sort_values(ascending=False)/len(df)*100, 2))


""" Errores como na or -- con la funcion to_numeric y en errors coerce
conseguimos que se sustituyan por errores """




df["NUM_BEDROOMS"] = pd.to_numeric(df["NUM_BEDROOMS"], errors="coerce")
df["NUM_BATH"] = pd.to_numeric(df["NUM_BATH"], errors="coerce")
df["SQ_FT"] = pd.to_numeric(df["SQ_FT"], errors="coerce")



# df["OWN_OCCUPIED"] = pd.to_numeric(df["OWN_OCCUPIED"], errors="coerce")


""" PARA PASAR TODO A NUMERO Y STRINGS U OTROS A NAN USAREMOS LA FUNCION 
PD.TO_NUMERIC


PARA CAMBIAR A NAN VALORES NUMERICOS DE UNA COLUMNA DE STRING

USAREMOS UN BUCLE

"""


cont = 0

for row in df["OWN_OCCUPIED"]:
    try:
        int(row)
        df.loc[cont, "OWN_OCCUPIED"] = np.nan
    
    except ValueError:
        pass
    cont +=1




# print(df.dtypes.sort_values())


# print(df.isnull().sum().sort_values(ascending=False))
# print(round(df.isnull().sum().sort_values(ascending=False)/len(df)*100, 2))


























































































































































