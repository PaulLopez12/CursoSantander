#1. Pedir al usuario que ingrese dos numeros para operar y la operacion a realizar
while True:
    operacion = input("Ingrese la operacion a realizar: ")
    if operacion == "salir":
        break
    numero1 = float(input("Ingrese el primer numero: "))
    numero2 = float(input("Ingrese el segundo numero: "))
    if numero1 != float(numero1) or numero2 != float(numero2):
        print("Numero no valido")
        continue
    if operacion == "+":
        resultado = numero1 + numero2
    elif operacion == "-":
        resultado = numero1 - numero2
    elif operacion == "*":
        resultado = numero1 * numero2
    elif operacion == "/":
        if numero2 == 0:
            print("No se puede dividir por cero")
            continue
        resultado = numero1 / numero2
    else:
        print("Operacion no valida")
        continue
    print(f"El resultado de la operacion es: {resultado}")