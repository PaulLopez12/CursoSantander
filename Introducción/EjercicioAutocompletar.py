#Crea una lista con los cuadrados de los n primeros numeros naturales
def cuadrados(n):
    lista = []
    for i in range(1, n+1):
        lista.append(i**2)
    return lista
cuadrados(5)
print(cuadrados(5))
