import random

""" DEF DE LOS METODOS DE ORDENAMIENTO """

class Ordenamientos:
    @staticmethod
    def burbuja(lista):
        n = len(lista)
        for i in range(n):
            for j in range(0, n-i-1):
                if lista[j] > lista[j+1]:
                    lista[j], lista[j+1] = lista[j+1], lista[j]
    @staticmethod         
    def inserccion(lista):
        for i in range(1, len(lista)):
            key = lista[i]
            j = i - 1
            while j >= 0 and key < lista[j]:
                lista[j + 1] = lista[j]
                j -= 1
            lista[j + 1] = key
    @staticmethod
    def mezcla(lista):
        if len(lista) > 1:
            medio = len(lista) // 2
            izquierda = lista[:medio]
            derecha = lista[medio:]
            Ordenamientos.mezcla(izquierda)
            Ordenamientos.mezcla(derecha)
            i = j = k = 0
            while i < len(izquierda) and j < len(derecha):
                if izquierda[i] < derecha[j]:
                    lista[k] = izquierda[i]
                    i += 1
                else:
                    lista[k] = derecha[j]
                    j += 1
                k += 1

            while i < len(izquierda):
                lista[k] = izquierda[i]
                i += 1
                k += 1

            while j < len(derecha):
                lista[k] = derecha[j]
                j += 1
                k += 1
    @staticmethod
    def quick_sort(lista):
        if len(lista) <= 1:
            return lista
        else:
            pivote = lista[len(lista) // 2]
            izquierda = [x for x in lista if x < pivote]
            medio = [x for x in lista if x == pivote]
            derecha = [x for x in lista if x > pivote]
            return Ordenamientos.quick_sort(izquierda) + medio + Ordenamientos.quick_sort(derecha)
    lista = [random.randint(0, 10000) for _ in range(10000)]
    @staticmethod
    def sacudida(lista):
        n = len(lista)
        intercambiado = True
        inicio = 0 
        fin = n - 1
        while intercambiado:
            intercambiado = False
            for i in range(inicio, fin):
                if lista[i] > lista[i + 1]:
                    lista[i], lista[i + 1] = lista[i + 1], lista[i]
                    intercambiado = True
            if not intercambiado:
                break
            intercambiado = False
            fin -= 1
            for i in range(fin - 1, inicio - 1, -1):
                if lista[i] > lista[i + 1]:
                    lista[i], lista[i + 1] = lista[i + 1], lista[i]
                    intercambiado = True
            inicio += 1
    @staticmethod
    def seleccion(lista):
        n = len(lista)
        for i in range(n):
            minimo = i
            for j in range(i + 1, n):
                if lista[j] < lista[minimo]:
                    minimo = j
            lista[i], lista[minimo] = lista[minimo], lista[i]
    lista = [random.randint(0, 100000) for _ in range(10000)]