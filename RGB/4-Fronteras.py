import pandas as pd

""" Paso 4: mandar los datos con fronteras al algoritmo """

df = pd.read_csv('BDRGB.csv')
df.loc[0:199, ['a1', 'a2', 'a3']] = [1, 0, 1]
df.loc[200:400, ['a1', 'a2', 'a3']] = [0, 1, 1]
df.loc[401:602, ['a1', 'a2', 'a3']] = [1, 1, 1]
df.to_csv('BDRGB.csv', index=False)
