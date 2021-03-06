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
import time
from DISClib.ADT import list as lt
from DISClib.Algorithms.Sorting import shellsort as sa
from DISClib.Algorithms.Sorting import insertionsort as insort
from DISClib.Algorithms.Sorting import selectionsort as selsort
from DISClib.Algorithms.Sorting import mergesort as mrgsort
from DISClib.Algorithms.Sorting import quicksort as qsort

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
    categ = {}
    categ[id] = name
    #categ['name'] = name
    #categ['categ_id'] = id
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

# Funciones de ordenamiento
def sortVideos(catalog, size,tiposort):
    sorted_list=[]
    sub_list = lt.subList(catalog['videos'], 0, size)
    sub_list = sub_list.copy()
    start_time = time.process_time()
    if tiposort == 1:
     sorted_list = sa.sort(sub_list, cmpVideosByViews)
    elif tiposort == 2:
     sorted_list = insort.sort(sub_list, cmpVideosByViews)
    elif tiposort == 3:       
     sorted_list= selsort.sort(sub_list, cmpVideosByViews)
    elif tiposort == 4:       
     sorted_list= mrgsort.sort(sub_list, cmpVideosByViews)
    elif tiposort == 5:       
     sorted_list= qsort.sort(sub_list, cmpVideosByViews)
    stop_time = time.process_time() 
    msegtime = (stop_time - start_time)*1000
 
        
    return  msegtime,sorted_list

def vidTendenciaCateg(catalog, categ):
    #print(catalog['categorias'])
    lista_trend = {}
    lista_dias = []
    categ_id = hallarID(catalog, categ)
    info_video = []
    for x in catalog["videos"]["elements"]:
        if x["category_id"] == categ_id:
            if x["video_id"] in lista_trend and x["video_id"] != "#NAME?":
                lista_trend[x["video_id"]] += 1
            else:
                lista_trend[x["video_id"]] = 1
    for x in lista_trend:
        lista_dias.append(lista_trend[x])
    for x in lista_trend:
        if lista_trend[x] == max(lista_dias):
            vid_id = x
    for x in catalog["videos"]["elements"]:
        if x["video_id"] == vid_id and x["title"] not in info_video:
            info_video.append(x["title"])
            info_video.append(x["channel_title"])
            info_video.append(x["category_id"])
            info_video.append(max(lista_dias))
    return info_video
    

def hallarID(catalog, categ):
    categ_id = None
    for x in catalog["categorias"]["elements"]:
        for id in x:
            if x[id] == (" "+categ):
                categ_id = id
    return categ_id
    