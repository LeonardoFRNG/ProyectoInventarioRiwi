name = input("Ingrese el nombre del producto: ")

precio = None

while precio is None:
    try:
        valor = float(input("Ingrese el precio del producto: "))
        
        if valor < 0:
            print("El precio debe ser positivo")
        else:
            precio = valor
            
    except ValueError:
        print("Ingrese solo números")


cantidad = None

while cantidad is None:
    try:
        valor = int(input("Ingrese la cantidad: "))
        
        if valor < 0:
            print("La cantidad debe ser positiva")
        else:
            cantidad = valor
            
    except ValueError:
        print("Ingrese solo números")


total = precio * cantidad

print(f"Producto: {name} | Precio: {precio} | Cantidad: {cantidad} | Total: {total}")