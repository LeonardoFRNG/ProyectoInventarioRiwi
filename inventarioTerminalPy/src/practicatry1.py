while True:
    try:
        numero = int(input("Ingrese un numero entero: "))
        print(f"Su numero es: {numero}")
        break
    except ValueError:
        print("Debe ingresar solo numeros enteros.")