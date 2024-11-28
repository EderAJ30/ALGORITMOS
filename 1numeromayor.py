#primero numero mayor y segundo mayor
def encontrar_mayores(sequence):
    mayor = segundo_mayor = float('-inf')

    for num in sequence:
        if num > mayor:
            segundo_mayor = mayor
            mayor = num
        elif mayor > num > segundo_mayor:
            segundo_mayor = num

    if segundo_mayor == float('-inf'):
        return mayor, None  
    return mayor, segundo_mayor

secuencia = [10, 20, 4, 45, 99, 78]
mayor, segundo_mayor = encontrar_mayores(secuencia)
print(f"El valor más grande es: {mayor}")
print(f"El segundo valor más grande es: {segundo_mayor}")