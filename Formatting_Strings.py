# -*- coding: utf-8 -*-
"""
Created on Thu May 27 09:25:58 2021

@author: Nacho
"""



# =============================================================================
""" String Manipulation and Regular Expressions """
# =============================================================================

import pandas as pd


""" Formating Strings - Adjusting Case """

# fox = "The quiCk brOwn fox"


# Upper letters
# fox = fox.upper()

# Lowercase Letters
# fox = fox.lower()

# Capitalize first letter of each word
# fox = fox.title()

# Capitalize just fist letter of each sentence
# fox = fox.capitalize()

# Letters can be swappped 
# fox = fox.swapcase()





""" Formatting Strings - Adding and removing spaces

Another common need is to remove spaces (or other characters) from the 
beginning or end of the string.

-> strip()


 """


# line = '    this is the content          '


# line= line.strip()


# Remove the space to the rignt
# line= line.rstrip()


# Just remove the left side
# line= line.lstrip()


# To remove characters other than spaces 
# num = "00000000000035"

# num = num.strip("0")




""" The opposite of this operation, adding spaces or other characters, 
can be accomplished using the center(), ljust() and rjust() """



# line = 'this is the content'


## Add spaces


# line = line.center(30)
# print("- {} -".format(line))

# line = line.ljust(30)
# print("- {} -".format(line))


# line = line.rjust(30)
# print("- {} -".format(line))









""" Finding and replacing substrings 

If you want to find ocurrences of a certain character in a string, the 

-> find(), index,  and replace() 
-> rfind and rindex (the same but start at the end)

are the best built-in methods """


line = 'the quick brown fox jumped over a lazy dog'

# Tanto find como index te dan la posicion

# print(line.find("fox"))
# print(line.index("fox"))


# print(line.find("bear"))
# print(line.index("bear"))



# line = line.replace("fox", "cat")
# print(line)










""" Splitting and partitioning strings  

Split more useful, it finds all instances of the split-point and returns the
substrings points between them.
 

Split spaces (by default)

"""

# name = "Martinez Perez, Dn. Jose Ignacio"

# line = line.split()
# print("-{}-".format(line))


# line = line.partition("fox")
# print(line)













""" Para extraer informacion en PANDAS dataframes or series

We don´t need to use re module

Actuall, pandas gives us it's own built-in methods

-> contains, extract, findall, match, split...


"""


df = pd.read_csv("train.csv")

df = df[["Name", "Sex", "Pclass"]]



""" We want to create a title column in which we extract the information 
about his title Mr, Mrs, Ms...


Also we want to create a column about his First Name with RegEx taking into 
account that it could have spaces, parenthesis...

"""



""" Extraemos el titulo 


Podemos observar que gran cantidad de los titulos de mayor enjundia pertenecen
a los pasajeros de la 1º clase. Mientras que no habia ni un solo titulo 
diferente al de Ms,Mrs, Mr o Master (infantes o niños) asociado a los pasajeros
de la 3º Clase

Por lo que estos titulos pueden ser de importancia a la hora de conocer si 
como vario la mortalidad para cada uno de estos titulos."""



df["Title"] = df.Name.str.extract("([A-Za-z]+)\.")

# print(df.isnull().sum())


# print(pd.crosstab(df["Title"], df["Sex"]))
# print(pd.crosstab(df["Title"], df["Pclass"]))



""" Combinar para varias clases """
# print(pd.crosstab(df["Title"], [df["Sex"], df["Pclass"]]))








""" Extraemos el 1º nombre

En este caso, se trata de una tarea extremadamente dificil, sin embargo, 
hemos encontrado una expresion regular que nos puede ofrecer ayuda para 
obtener aproximandamente más de 885 de 891 casos.

lo cual refleja un total de datos del 99%. """

# df["First_Name"] = df.Name.str.extract("\.\s\(?([A-Za-z]+)")
# print(df.isnull().sum())

























































