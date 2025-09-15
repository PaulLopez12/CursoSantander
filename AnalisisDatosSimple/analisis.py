import csv
import numpy as np
import matplotlib.pyplot as plt

#Pedir ruta de archivo csv
ruta = input("Ingrese la ruta del archivo csv: ")
#Leer archivo csv
with open(ruta, 'r') as file:
    reader = csv.reader(file)
#Calcular la media, mediana, desviacion estandar de cada columna
    for row in reader:
        print(row)
        #Convertir a numeros
        numeric_row = [float(x) for x in row]
        media = np.mean(numeric_row)
        mediana = np.median(numeric_row)
        desviacion = np.std(numeric_row)
        print(f"Media: {media}, Mediana: {mediana}, Desviacion: {desviacion}")
#Generar grafica de dispersion de cada columna vs la otra
    plt.scatter(numeric_row[0], numeric_row[1])
    plt.show()
    