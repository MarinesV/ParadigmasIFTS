def sumaLineal(cantidad):
    suma = 0
    for numero in range (1, cantidad +1):
        suma += numero
    return suma

def sumaContinua(cantidad):
    return(cantidad/2) * (cantidad+1)

cantidad = int(input("Ingrese un numero"))
print(sumaLineal(cantidad))
print(sumaContinua(cantidad))
