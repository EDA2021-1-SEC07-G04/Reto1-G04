﻿"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 *
 * Contribuciones:
 *
 * Dario Correal - Version inicial
 """


import config as cf
from DISClib.ADT import list as lt
from DISClib.Algorithms.Sorting import shellsort as sa
assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

# Construccion de modelos
def CatalNuevo():
    catalog={"videos": None,"categorias":None}
    catalog["videos"]=lt.newList()
    catalog["categorias"]=lt.newList("ARRAY_LIST")
    return catalog

# Funciones para agregar informacion al catalogo

"""def addVideo(catalog, video):
    lt.addLast(catalog['books'], book)
 """   
def addCateg(catalog, categ):
    """
    Adiciona una categoria a la lista de categorias
    """
    print(categ.keys())
    c = newCateg(categ['name'], categ['id'])
    lt.addLast(catalog['categorias'], c)

# Funciones para creacion de datos

def newCateg(name, id):
    """
    Esta estructura almancena las categorias utilizadas para los videos.
    """
    categ = {'name': '', 'categ_id': ''}
    categ['name'] = name
    categ['categ_id'] = id
    return categ
# Funciones de consulta

# Funciones utilizadas para comparar elementos dentro de una lista

# Funciones de ordenamiento