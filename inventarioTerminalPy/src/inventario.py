name = input("Ingrese el nombre del producto: ")

price= None

while price is None:
    try:
        value = float(input("Ingrese el precio del producto: "))
        
        if value < 0:
            print("El precio debe ser positivo")
        else:
            price = value
            
    except ValueError:
        print("Ingrese solo números")


quantity = None

while quantity is None:
    try:
        value = int(input("Ingrese la cantidad: "))
        
        if value < 0:
            print("La cantidad debe ser positiva")
        else:
            quantity = value
            
    except ValueError:
        print("Ingrese solo números")


total = price * quantity

print(f"Producto: {name} | Precio: {price} | Cantidad: {quantity} | Total: {total}")