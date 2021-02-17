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

catalog = None
def iniciar_catalogo():
    """
    Inicializa el catalogo de libros
    """
    return controller.iniciar_catalog()
def CargarDatos(catalog):
    """
    Carga los libros en la estructura de datos
    """
    controller.dataLoad(catalog)    

"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs[0]) == 1:
        print("Cargando información de los archivos ....")
        catalogo=iniciar_catalogo()
        CargarDatos(catalogo)
    elif int(inputs[0]) == 2:
        pass

    else:
        sys.exit(0)
sys.exit(0)
