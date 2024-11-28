from metodos_ordenamiento import Ordenamientos
from time import time
import csv
import random
import copy

""" CLASE MAIN PARA EJECUTAR CADA DEF DE LOS METODOS DE ORDENAMIENTO Y CONSTRUIR EL CSV """

def generar_lista(tamano):
    return [random.randint(0, 200) for _ in range(tamano)]

def calcular_tiempo(algoritmo, datos):
    inicio = time()
    if algoritmo == Ordenamientos.quick_sort:
        resultado = algoritmo(datos)
    else:
        algoritmo(datos)
    fin = time()
    return fin - inicio

def guardar_csv(nombre, datos_tiempos):
    with open(nombre, mode='w', newline='') as archivo_csv:
        escritor = csv.writer(archivo_csv)
        escritor.writerow(['Tamano', 'Tiempo'])
        for tamano, tiempo in datos_tiempos:
            escritor.writerow([tamano, tiempo])

def ejecutar_ordenamiento(tamano_max, nombre_algoritmo):
    metodos = {
        "burbuja": Ordenamientos.burbuja,
        "mezcla": Ordenamientos.mezcla,
        "quick_sort": Ordenamientos.quick_sort,
        "insercion": Ordenamientos.inserccion,
        "seleccion": Ordenamientos.seleccion,
        "sacudida": Ordenamientos.sacudida
    }

    if nombre_algoritmo not in metodos:
        print(f"Algoritmo desconocido. Opciones disponibles: {', '.join(metodos.keys())}")
        return

    metodo_ordenamiento = metodos[nombre_algoritmo]
    lista_original = generar_lista(tamano_max)
    resultados_tiempos = []

    for tamano_actual in range(100, tamano_max + 1, 100):
        lista_copia = copy.deepcopy(lista_original[:tamano_actual])
        duracion = calcular_tiempo(metodo_ordenamiento, lista_copia)
        resultados_tiempos.append((tamano_actual, duracion))
        print(f'Algoritmo: {nombre_algoritmo}, Tamaño: {tamano_actual}, Tiempo: {duracion:.3f} segundos')

    guardar_csv(f'{nombre_algoritmo}.csv', resultados_tiempos)

if __name__ == "__main__":
    ejecutar_ordenamiento(100000, 'quick_sort')
