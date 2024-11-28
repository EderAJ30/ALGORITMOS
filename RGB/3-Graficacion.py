import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import pandas as pd

""" gráfica para ver donde poner las fronteras """

np.random.seed(1968801)

def randrange(n, vmin, vmax):
    return (vmax - vmin)*np.random.rand(n) + vmin

x = np.linspace(-5, 5, 100)  
y = np.linspace(-5, 5, 100)  
x, y = np.meshgrid(x, y) 
df = pd.read_csv("BDRGB.csv")

r1 = df['R'][0:199] 
g1 = df['G'][0:199]  
b1 = df['B'][0:199] 
r2 = df['R'][200:400]  
g2 = df['G'][200:400]  
b2 = df['B'][200:400]  
r3 = df['R'][400:600]  
g3 = df['G'][400:600]  
b3 = df['B'][400:600]  

z1 = 5 * x + 5 * y  
z2 = 3 * x + 7 * y  

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(r1, g1, b1, marker='o', color='red') 
ax.scatter(r2, g2, b2, marker='o', color='green')  
ax.scatter(r3, g3, b3, marker='o', color='yellow') 
ax.set_xlabel('Eje X')  
ax.set_ylabel('Eje Y')  
ax.set_zlabel('Eje Z')  

plt.show()
