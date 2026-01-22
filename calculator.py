"""
calculator.py

A simple calculator using Python functions.
Demonstrates parameters, return values, default arguments,
error handling, and docstrings.
"""

def add(a, b=0):
    """
    Add two numbers and return the result.
    b has a default value of 0.
    """
    return a + b


def subtract(a, b=0):
    """
    Subtract second number from first and return the result.
    b has a default value of 0.
    """
    return a - b


def multiply(a, b=1):
    """
    Multiply two numbers and return the result.
    b has a default value of 1.
    """
    return a * b


def divide(a, b):
    """
    Divide first number by second number.
    Handles division by zero.
    """
    if b == 0:
        return "Error: Division by zero is not allowed"
    return a / b


def get_numbers():
    """
    Take two numbers from the user and return them.
    """
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    return num1, num2


def show_menu():
    """
    Display calculator menu.
    """
    print("\nCalculator Menu")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")


def main():
    """
    Main function to run the calculator.
    """
    show_menu()
    choice = input("Enter choice (1-4): ")

    num1, num2 = get_numbers()

    if choice == "1":
        print("Result:", add(num1, num2))
    elif choice == "2":
        print("Result:", subtract(num1, num2))
    elif choice == "3":
        print("Result:", multiply(num1, num2))
    elif choice == "4":
        print("Result:", divide(num1, num2))
    else:
        print("Invalid choice")


# STEP 9: Independent testing of functions
if __name__ == "__main__":
    print("Function Testing:")
    print("Add:", add(10, 5))
    print("Subtract:", subtract(10, 5))
    print("Multiply:", multiply(10, 5))
    print("Divide:", divide(10, 0))

    main()
