def Factorial(numero):
    if numero == 1:
        return 1
    else:
        return numero * Factorial(numero-1)

def med(numero1, numero2):
    if numero2 == 0:
        return numero1
    elif numero1 == 0:
        return numero2
    else:
        if numero1 > numero2:
            return med(numero1-numero2, numero2)
        else:
            return med(numero1,numero2-numero1)

numeroleido1 = int(input("Primer numero para calcular el MCD: "))
numeroleido2 = int(input("Segundo numero para calcular el MCD: "))
print(f"Resultado del MCD: {med(numeroleido1, numeroleido2)}")

factorial = int(input("Numero a calcular factorial es: "))

print(f"Resultado: {Factorial(factorial)}")
