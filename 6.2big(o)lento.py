#sexto lento
def maxSuma(s, n):
    suma = [[0] * n for _ in range(n)]
    
    for i in range(n):
        for j in range(i):
            suma[j][i] = suma[j][i - 1] + s[i] 
        suma[i][i] = s[i]  
    
    max_sum = 0
    for i in range(n):
        for j in range(i):
            if suma[j][i] > max_sum:
                max_sum = suma[j][i]
    
    return max_sum

s = [27, 6, -50, 21, -3, 14, 16, -8, 42, 33, -21, 9]
n = len(s)
resultado = maxSuma(s, n)
print("La suma máxima es:", resultado)