numero1 = float(input("Ingrese el número escogido al azar: "))
compras1 = float(input("Ingrese el total de la compra: "))
if numero1 <74:
    descuento1 = compras1 *0.15
else:
    descuento1 = compras1 *0.20
total_compras = compras1 -descuento1
print(f"El descuento aplicado es {descuento1} y el total a pagar es {total_compras}")