#quinto caminos
def factorial(num):
    resultado = 1
    for i in range(2, num + 1):
        resultado *= i
    return resultado

def calcular_combinaciones(n, k):
    return factorial(n) // (factorial(k) * factorial(n - k))

def calcular_trayectorias():
    x1, y1 = 2, 1
    x2, y2 = 7, 4

    pasos_derecha = x2 - x1  
    pasos_arriba = y2 - y1   

    numero_de_trayectorias = calcular_combinaciones(pasos_derecha + pasos_arriba, pasos_arriba)

    print(f"El número de trayectorias ({x1}, {y1}) a ({x2}, {y2}) es: {numero_de_trayectorias}")

def generar_trayectorias(r, u):
    from itertools import permutations

    movimientos = ['R'] * r + ['U'] * u
    trayectorias = set(permutations(movimientos))
    
    return trayectorias

def mostrar_trayectorias():
    r = 5 
    u = 3  

    trayectorias = generar_trayectorias(r, u)

    print(f"El número de trayectorias posibles es: {len(trayectorias)}")
    print("Las trayectorias posibles son:")
    for trayectoria in trayectorias:
        print(''.join(trayectoria))

if __name__ == "__main__":
    calcular_trayectorias()
    mostrar_trayectorias()
