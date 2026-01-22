# datatypes_demo.py
# Internship Task: Python Data Types Demonstration
# This script shows how Python handles different data types,
# arithmetic operations, type casting, error handling, and dynamic typing.

# -------------------------
# 1. Declare variables of different data types
# -------------------------
my_int = 25                  # Integer
my_float = 7.5               # Float
my_string = "Python"         # String
my_boolean = True            # Boolean

# -------------------------
# 2. Print the type of each variable
# -------------------------
print("Variable Types:")
print("my_int:", my_int, "| Type:", type(my_int))
print("my_float:", my_float, "| Type:", type(my_float))
print("my_string:", my_string, "| Type:", type(my_string))
print("my_boolean:", my_boolean, "| Type:", type(my_boolean))
print()

# -------------------------
# 3. Arithmetic operations
# -------------------------
addition = my_int + my_float
multiplication = my_int * my_float

print("Arithmetic Operations:")
print("Addition:", addition)
print("Multiplication:", multiplication)
print()

# -------------------------
# 4. Type casting (string to int and float)
# -------------------------
number_str = "100"
decimal_str = "45.75"

converted_int = int(number_str)
converted_float = float(decimal_str)

print("Type Conversion:")
print("Converted Integer:", converted_int, "| Type:", type(converted_int))
print("Converted Float:", converted_float, "| Type:", type(converted_float))
print()

# -------------------------
# 5. Error handling for invalid conversion
# -------------------------
invalid_value = "abc"

try:
    result = int(invalid_value)
except ValueError:
    print("Error Handling:")
    print("Conversion failed! Cannot convert 'abc' to integer.")
print()

# -------------------------
# 6. String and number concatenation
# -------------------------
final_string = my_string + " version " + str(my_int)
print("String Concatenation:")
print(final_string)
print()

# -------------------------
# 7. Dynamic typing demonstration
# -------------------------
dynamic_var = 50
print("Dynamic Variable:", dynamic_var, "| Type:", type(dynamic_var))

dynamic_var = "Now I am a string"
print("Dynamic Variable:", dynamic_var, "| Type:", type(dynamic_var))

dynamic_var = 9.81
print("Dynamic Variable:", dynamic_var, "| Type:", type(dynamic_var))
