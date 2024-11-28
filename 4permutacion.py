#cuarto permutacion
def permutaciones(n):
    s = list(range(1, n + 1))
    print(s)

    for i in range(1, factorial(n)):
        m = n - 2
        while m >= 0 and s[m] > s[m + 1]:
            m -= 1

        k = n - 1
        while s[m] > s[k]:
            k -= 1

        s[m], s[k] = s[k], s[m]
        p = m + 1
        q = n - 1

        while p < q:
            s[p], s[q] = s[q], s[p]
            p += 1
            q -= 1

        print(s)

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

permutaciones(3)