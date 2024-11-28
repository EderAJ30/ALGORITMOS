#sexto rapido 
def sumaMaxima(s, n):
    suma_maxima = 0
    suma_actual = 0
    
    for i in range(n):
        if suma_actual + s[i] > 0:
            suma_actual += s[i]
        else:
            suma_actual = 0
        
        if suma_actual > suma_maxima:
            suma_maxima = suma_actual
    
    print("La suma máxima es:", suma_maxima)
    return suma_maxima

s = [27, 6, -50, 21, -3, 14, 16, -8, 42, 33, -21, 9]
n = len(s)

sumaMaxima(s, n)