productos = []

print("Inventario de productos")

print("menu")
print("1, agregar producto")
print("2, ver productos actuales")
print("3, actualizar producto")
print("4, eliminar producto")
print("0, salir")

opcion = input("Ingrese una opcion: ")

if opcion == "1":
#pedir el nombre, precio y cantidad del producto
    
 nombre = input("Ingrese el nombre del producto: ")
 precio = float(input("Ingrese el precio del producto: "))
 cantidad = int(input("Ingrese la cantidad del producto: "))
 
 #imprimir el producto agregado
 print(f"producto agregado: {nombre}, precio: {precio}, Cantidad: {cantidad}, Total: {precio*cantidad}")  

    



