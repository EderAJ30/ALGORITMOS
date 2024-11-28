import numpy as np
import pandas as pd

def funcion_escalon(entrada):
    for x in range(entrada.shape[0]):
        for y in range(entrada.shape[1]):
            entrada[x][y] = 1 / (1 + np.exp(entrada[x][y]))
    return entrada

datos = pd.read_csv('BDRGB.csv')
entradas = datos[['R', 'G', 'B']].to_numpy()
salidas_esperadas = datos[['a1', 'a2', 'a3']].to_numpy()

# Inicializar pesos, sesgos y error
pesos = np.random.rand(3, 3) - 1
sesgos = np.random.rand(1, 3) - 1
errores = np.zeros((601, 3))

# Ciclo de entrenamiento
for epoca in range(1000):
    for indice in range(601):
        valor_predicho = funcion_escalon(np.dot(pesos, entradas[indice].T) + sesgos)
        if (valor_predicho != salidas_esperadas[indice]).all():
            errores[indice] = salidas_esperadas[indice] - valor_predicho
            pesos = pesos + (errores[indice] * entradas[indice] * 0.1)
            sesgos = sesgos + errores[indice]

errores_df = pd.DataFrame(errores)

print("Pesos finales:", pesos)
print("Sesgos finales:", sesgos)
print("Errores:", errores)





