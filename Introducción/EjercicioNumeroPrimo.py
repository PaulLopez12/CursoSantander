def numero_primo(n):
    if n==0 or n==1:
        return False
    else:
        for i in range(2, n):
            if n%i==0:
                return False
        return True

# Pruebas de la función numero_primo
print("=== Pruebas de la funcion numero_primo ===")

# Prueba con diferentes números
numeros_prueba = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 17, 20, 23]

for num in numeros_prueba:
    resultado = numero_primo(num)
    print(f"¿{num} es primo? {resultado}")

# Prueba específica con el número 4
print(f"\nPrueba específica: ¿4 es primo? {numero_primo(4)}")

# Prueba con números más grandes
print(f"¿97 es primo? {numero_primo(97)}")
print(f"¿100 es primo? {numero_primo(100)}")