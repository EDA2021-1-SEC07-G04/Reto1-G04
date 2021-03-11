"""
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

import collections
import config as cf
import time
from DISClib.ADT import list as lt
from DISClib.Algorithms.Sorting import shellsort as sa
from DISClib.Algorithms.Sorting import insertionsort as insort
from DISClib.Algorithms.Sorting import selectionsort as selsort
assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

# Construccion de modelos
def CatalNuevo():
    catalog={"videos": None,"categorias":None}
    catalog["videos"]=lt.newList("ARRAY_LIST")
    catalog["categorias"]=lt.newList("ARRAY_LIST")
    return catalog

# Funciones para agregar informacion al catalogo

def addVideo(catalog, video):
    lt.addLast(catalog['videos'], video)
   
def addCateg(catalog, categ):
    """
    Adiciona una categoria a la lista de categorias
    """
    c = newCateg(categ['name'], categ['id'])
    lt.addLast(catalog['categorias'], c)



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
def cmpVideosByViews(video1, video2):
 x=None
 if (float(video1['views']) < float(video2['views'])):
  x=True
  return x 
 else:
  x=False
  return x

def cmpVideosByLikes(video1, video2):
 x=None
 if (int(video1['likes']) < int(video2['likes'])):
  x=True
  return x 
 else:
  x=False
  return x


# Funciones de ordenamiento
def sortVideos(catalog, size,checker):
    sorted_list=[]
    sub_list = lt.subList(catalog['videos'], 0, size)
    sub_list = sub_list.copy()
    if checker == 2:
     sorted_list = sa.sort(sub_list, cmpVideosByViews)
    else:
     sorted_list = sa.sort(sub_list, cmpVideosByLikes)    
             
    return  sorted_list

def masDias(catalog,pais):
    used=[]
    counted=[]
    videostitulos=[]
    for i in range(0,lt.size(catalog["videos"])):
     if catalog["videos"]["elements"][i]["country"] == pais:
        
              videostitulos.append(catalog["videos"]["elements"][i]["title"])
    
    for i in videostitulos:
     if i not in used:  
        used.append(i)   
        trendingdays=videostitulos.count(i)    
        counted.append(trendingdays)      
    mastrending=max(counted)
    alah=counted.index(mastrending)
    correspondent=used[alah]
    for i in range(0,lt.size(catalog["videos"])):
        if catalog["videos"]["elements"][i]["title"] == correspondent:
            titulocanal=catalog["videos"]["elements"][i]["channel_title"]
    return correspondent,mastrending,titulocanal,pais
