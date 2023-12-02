
# Ejemplo de condicional
n = int(input("Ingrese un número: \n"))
if n > 0:
    print("El número es positivo.")
    if n % 2 == 0:
        print("El numero es par")
    elif n % 2 ==1:
        print("El numero es impar")
elif n < 0:
    print("El número es negativo.")
else:
    print("El número es cero.")
