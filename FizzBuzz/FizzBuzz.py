#Recorrer los numeros del 1 al 50, si el numero es divisible por 3, imprimir Fizz, si es divisible por 5, imprimir Buzz, si es divisible por 3 y 5, imprimir FizzBuzz.
for i in range(1, 51):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)
