import serial
import numpy as np

arduino = serial.Serial(port='COM3', baudrate=9600, timeout=1)

w = np.array([
    [0.2, -0.1, 0.05],
    [0.1, 0.3, -0.2],
    [0.05, -0.05, 0.4]
])
b = np.array([-0.1, 0.2, -0.05])

# Función de activación sigmoide
def escalon(n):
    return 1 / (1 + np.exp(-n))

def clasificar_color(salida):
    salida_binaria = np.round(salida)
    # Mapear las fronteras de decisión a colores con el paso 4
    if np.array_equal(salida_binaria, [1, 0, 1]):
        return "Rojo"
    elif np.array_equal(salida_binaria, [0, 1, 1]):
        return "Verde"
    elif np.array_equal(salida_binaria, [1, 1, 1]):
        return "Amarillo"
    else:
        return "No definidooooo"

while True:
    linea = arduino.readline().decode('utf-8').strip()
    if linea:
        try:
            rgb = np.array([float(x) for x in linea.split(',')])
            valor = escalon(np.dot(w, rgb.T) + b)

            color = clasificar_color(valor)

            print(f"Entrada RGB: {rgb}")
            print(f"Salida activación: {valor}")
            print(f"Color de la fruta es: {color}\n")
        except Exception as e:
            print(f"Errooooor: {linea}, {e}")
