#sexto intermedio 
def maxSumas(s, n):
    sumax = 0
    sumactual = 0
    
    for i in range(n):
        sumactual += s[i]
        
        if sumactual > sumax:
            sumax = sumactual
        
        if sumactual < 0:
            sumactual = 0
    
    print("La suma maxima es:", sumax)
    return sumax

s = [27, 6, -50, 21, -3, 14, 16, -8, 42, 33, -21, 9]
n = len(s)
maxSumas(s, n)