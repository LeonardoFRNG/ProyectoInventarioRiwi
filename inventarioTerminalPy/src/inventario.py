#solicitar el nombre del producto al usuario
name = input("Ingrese el nombre del producto: ")

#este while repite la pregunta al usuario siempre que ingrese un valor incorrecto
while True:
    
    #este try atrapa lo que el user ingresa y si la variable no es correcta entonces pasa al except mostrando el menaje de error y el ciclo se repite, ya que nunca hubo break.
    try:
        #solictamos dato al usuario
        precio = float(input("Ingrese el precio del producto: "))
        if precio <0:
            print("Por favor ingrese valores numericos positivos.")
            continue
        break
    except ValueError:
        print("Por favor ingrese solo valores numericos.")
        
while True:
    #solicitar dato al usuario.  
    try:
        cantidad = int(input("Ingrese la cantidad del producto: "))
        if cantidad <0:
            print("Por favor, ingrese solo valores numericos positivos.")
            continue
        break
    except ValueError:
        print("Ingrese solo valores numericos")
        
#costo total, calculo

costo_total = precio * cantidad

#se imprime el nombre, precio, cantidad y el total del producto y se muestra por consola.add()

print(
    f"Producto: {name} | precio: {precio} | cantidad: {cantidad} | total: {costo_total}"
)