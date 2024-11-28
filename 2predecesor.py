#segundo predecesor del primer mayor
def leer(lista):
    for i in range(1, len(lista)):
        if len(lista[i]) < len(lista[i-1]):
            for j in range(i + 1, len(lista)):
                if len(lista[j]) < len(lista[i]):
                    return j, lista[j]
            return -1
    return -1

lista = ["TOMAS","BRUNO", "ELIE", "DAN", "ZEKE"]
resultado = leer(lista)
print (resultado)