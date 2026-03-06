def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Error: Division by zero"


while True:
    print("\nMenu:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        x = float(input("Enter first number: "))
        y = float(input("Enter second number: "))
        print("Result:", add(x, y))

    elif choice == "2":
        x = float(input("Enter first number: "))
        y = float(input("Enter second number: "))
        print("Result:", subtract(x, y))

    elif choice == "3":
        x = float(input("Enter first number: "))
        y = float(input("Enter second number: "))
        print("Result:", multiply(x, y))

    elif choice == "4":
        x = float(input("Enter first number: "))
        y = float(input("Enter second number: "))
        print("Result:", divide(x, y))

    elif choice == "5":
        print("Exiting...")
        break

    else:
        print("Invalid choice")