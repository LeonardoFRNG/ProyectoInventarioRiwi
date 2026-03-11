while True:
    try:
        numeroPositivo = int(input("Ingrese un numero positivo: \n"))

        if numeroPositivo < 0:
            print("Solo puede ingresar numeros positivos.")
            continue
        print(f"Su numero positivo es: {numeroPositivo}")
        break
    except ValueError:
        print("Solo puede ingresar numeros.")
