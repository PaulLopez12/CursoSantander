#1. Cargar datos del archivo csv
import csv
with open('ventas.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
#2. Calcular el total de ventas por mes
ventas_por_mes = {}
for row in reader:
    if row[0] not in ventas_por_mes:
        ventas_por_mes[row[0]] = 0
    ventas_por_mes[row[0]] += float(row[1])
print(f"Las ventas por mes son: {ventas_por_mes}")


#3. Determinarr el producto mas vendido y con mayor ingresos
producto_mas_vendido = max(reader, key=lambda x: x[1])
print(f"El producto mas vendido es: {producto_mas_vendido}")
producto_mas_ingresos = max(reader, key=lambda x: x[2])
print(f"El producto con mayor ingresos es: {producto_mas_ingresos}")

#4. Graficar ventas por mes
import matplotlib.pyplot as plt
plt.bar(ventas_por_mes.keys(), ventas_por_mes.values())
plt.show()

#5.Graficar top 5 productos por ingresos
top_5_productos = sorted(reader, key=lambda x: x[2], reverse=True)[:5]
plt.bar(top_5_productos.keys(), top_5_productos.values())
plt.show()

