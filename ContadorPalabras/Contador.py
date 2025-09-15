#1. Pedir al usuario la ruta del archivo de texto
#2. Leer el archivo de texto
ruta = input("Ingrese la ruta del archivo de texto: ")

try:
    with open(ruta, 'r') as archivo:
        texto = archivo.read()
except FileNotFoundError:
    print("El archivo no existe")
    exit()

#3. Separar el texto en palabras
#4. Contar el numero de palabras
import re
palabras = re.findall(r"\w+", texto.lower())
total_palabras = len(palabras)
print(f"El total de palabras es: {total_palabras}")

#5. Contar el numero de veces que aparece cada palabra
contador_palabras = {}
for palabra in palabras:
    if palabra in contador_palabras:
        contador_palabras[palabra] += 1
    else:
        contador_palabras[palabra] = 1
print(contador_palabras)


