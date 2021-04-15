"""
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
    return controller.startData(catalog)
"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs[0]) == 1:
        print("Cargando información de los archivos ....")
        catalog=initCatalog()
        answer=loadData(catalog)
        print(lt.lastElement(catalog["videos"]))
        print('Videos cargados: ' + str(lt.size(catalog['videos'])))
        print('Categorias cargadas: ' + str(lt.size(catalog['categorias'])))
        #print(catalog["categorias"])
        print("Tiempo [ms]: ", answer[0], "  ||  ",
              "Memoria [kB]: ", answer[1])
        
    elif int(inputs[0]) == 2:
        tamaño=int(input("Indique el tamaño de la muestra a analizar"))
        #tiposort=int(input("Indique 1 para shellsort,2 para insertionsort,3 para selectionsort"))
        pais=input("Introduzca un país a analizar")
        categoriaa=input("Introduzca el ID de una categoría a analizar")
        result=controller.videoSortTime(catalog,tamaño,2)  
        #print(result[0])    
        for i in range(0,len(result[0]["elements"])):
            if result[0]["elements"][i]["country"] == pais and result[0]["elements"][i]["category_id"] == categoriaa:
                print(result[0]["elements"][i]["trending_date"],result[0]["elements"][i]["title"],result[0]["elements"][i]["channel_title"],result[0]["elements"][i]["publish_time"],result[0]["elements"][i]["views"],result[0]["elements"][i]["likes"],result[0]["elements"][i]["dislikes"])
        print("Tiempo [ms]: ", result[1], "  ||  ",
              "Memoria [kB]: ", result[2])
    elif int(inputs[0]) == 3:
      pais=input("seleccione un país a analizar")
      sorteados=controller.trendingVideosTime(catalog,pais)
      print(sorteados[0])
      print("Tiempo [ms]: ", sorteados[1], "  ||  ",
              "Memoria [kB]: ", sorteados[2])
    elif int(inputs[0]) == 4:
        category_name = input("Indique la categoría del video de mayor tendencia.")
        result=controller.tendenciaCategTime(catalog, category_name)
        print(result[0])
        print("Tiempo [ms]: ", result[1], "  ||  ",
              "Memoria [kB]: ", result[2])
    elif int(inputs[0]) == 5:
        tamaño=int(input("Indique el tamaño de la muestra a analizar"))
        pais=input("Introduzca un país a analizar")
        tagrequest=input("Introduzca un tag a revisar")
        result2=controller.videoSortTime(catalog,tamaño,3)
        for i in range(0,len(result2[0]["elements"])):
            if result2[0]["elements"][i]["country"] == pais and tagrequest  in result2[0]["elements"][i]["tags"] :
             print( print(result2[0]["elements"][i]["tags"],result2[0]["elements"][i]["title"],result2[0]["elements"][i]["channel_title"],result2[0]["elements"][i]["publish_time"],result2[0]["elements"][i]["views"],result2[0]["elements"][i]["likes"],result2[0]["elements"][i]["dislikes"]))
        print("Tiempo [ms]: ", result2[1], "  ||  ",
              "Memoria [kB]: ", result2[2])
       # print(result[0])
       # print(result[1]["elements"][0:2])
       
        tiposort=int(input("Indique 1 para shellsort,2 para insertionsort,3 para selectionsort, 4 para mergesort, 5 para quicksort."))
        result=controller.videoSort(catalog,tamaño,tiposort)
        print("mensaje de confirmacion")
    else:
        sys.exit(0)
sys.exit(0)
