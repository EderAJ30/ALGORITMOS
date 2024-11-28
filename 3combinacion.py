#tercero combinacion
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

def combinaciones(r, n):
    def comb(n, r):
        return factorial(n) // (factorial(r) * factorial(n - r))

    combinacion = list(range(1, r + 1))
    print(combinacion)

    total_combinaciones = comb(n, r) 

    for i in range(2, total_combinaciones + 1):
        m = r - 1
        val_max = n
        while combinacion[m] == val_max:
            m -= 1
            val_max -= 1
        combinacion[m] += 1
        for j in range(m + 1, r):
            combinacion[j] = combinacion[j - 1] + 1

        print(combinacion)

combinaciones(3, 5)
