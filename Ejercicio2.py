
montoCompra = float(input("Ingrese el monto de la compra: "))

if montoCompra >= 100:
  montofinal = montoCompra * 0.8

else:
  montofinal = montoCompra
  
print(f"El monto a pagar es: {montofinal}")