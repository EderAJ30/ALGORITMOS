import serial
import csv
import time

""" Paso 2: con python leer el serial y escribir en csv """

puerto_serial = serial.Serial('COM3', 9600) 
time.sleep(2) 
csv_filename = 'BDRGBB.csv'
with open(csv_filename, mode='a', newline='') as file:
    escritorCsv = csv.writer(file)
    escritorCsv.writerow(["R", "G", "B", "a1", "a2", "a3"])
    seccion = ['1', '1', '0']
    contador = 0
    try:
        while True:
            if puerto_serial.in_waiting > 0:
                data = puerto_serial.readline().decode('utf-8').strip()
                rgb_values = data.split(',')
                escritorCsv.writerow(rgb_values + seccion)
                contador += 1
                print(f"{contador}.- Datos guardadoos: {rgb_values}")
    except KeyboardInterrupt:
        print("Error")
puerto_serial.close()
