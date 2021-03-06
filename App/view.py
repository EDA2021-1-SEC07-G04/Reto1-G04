﻿"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad
 * de Los Andes
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
 """

import config as cf
import sys
import controller
from DISClib.ADT import list as lt
assert cf


"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""

def printMenu():
    print("Bienvenido")
    print("1- Cargar información en el catálogo")
    print("2-Videos de mayor tendencia en un país segun la categoría ")
    print("3-Video de mayor duración como tendencia  según el país")
    print("4-Video de mayor duración como tendencia según la categoría")
    print("5-Videos con mayor cantidad de likes según el país")

def initCatalog():
    """
    Inicializa el catalogo de videos
    """
    return controller.startCatalog()

def loadData(catalog):
    """
    Carga los videos en la estructura de datos
    """
    controller.startData(catalog)
"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs[0]) == 1:
        print("Cargando información de los archivos ....")
        catalog=initCatalog()
        loadData(catalog)
        print(lt.lastElement(catalog["videos"]))
        print('Videos cargados: ' + str(lt.size(catalog['videos'])))
        print('Categorias cargadas: ' + str(lt.size(catalog['categorias'])))
    elif int(inputs[0]) == 2:
        tamaño=int(input("Indique el tamaño de la muestra a analizar"))
        tiposort=int(input("Indique 1 para shellsort,2 para insertionsort,3 para selectionsort, 4 para mergesort, 5 para quicksort."))
        result=controller.videoSort(catalog,tamaño,tiposort)
        print("mensaje de confirmacion")
    elif int(inputs[0]) == 4:
        category_name = input("Indique la categoría del video de mayor tendencia.")
        result=controller.tendenciaCateg(catalog, category_name)
        print(result)
    elif int(inputs[0]) == 5:
        numero_vids = input("Indique el número de videos a mostrar.")
        tag = input("Indique un tag a buscar.")
        pais = input("Indique un país.")
        #result=controller.likesPaisTag(catalog, category_name)
      
        

    else:
        sys.exit(0)
sys.exit(0)
