name = input("Enter your product name: ")

price = None

while price is None:
    try:
        value = float(input("Enter the product price: "))

        if value < 0:
            print("You only can enter positive numbers.")
        else:
            price = value

    except ValueError:
        print("Enter only numbers.")

quantity = None

while quantity is None:
    try:
        value = int(input("Enter the quantity: "))

        if value < 0:
                    print("You only can enter a positive quantity.")
        else:
                    quantity = value

    except ValueError:
                print("You only can enter numbers.")


total = price * quantity

print(f"Product: {name} | Price: {price} | Quantity: {quantity} | Total: {total}")