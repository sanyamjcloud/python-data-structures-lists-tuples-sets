print("Task 2: For loop 1-100")
for i in range(1, 101):
    print(i, end=" ")
print("Task 3: Countdown timer using while loop")
count = 10
while count > 0:
    print(count)
    count -= 1
print("Lift off!\n")
print("Task 4: Break and Continue example")
for i in range(1, 11):
    if i == 5:
        print("Skipping number 5")
        continue  # Skip number 5
    if i == 8:
        print("Stopping at number 8")
        break  # Stop loop at 8
    print(i)
print()
print("Task 5: Iterate over string")
text = "Hello"
for char in text:
    print(char)
print()
print("Task 6: Multiplication table of 7")
num = 7
for i in range(1, 11):
    print(f"{num} x {i} = {num*i}")
print()
print("Task 7: Numbers from 0 to 20 with step 2")
for i in range(0, 21, 2):
    print(i, end=" ")
print("\n")
print("Task 8: Print even numbers from 1-20")
for i in range(1, 21):
    if i % 2 == 0:
        print(i, end=" ")
print("\n")
print("Task 9: Real-world example - shopping cart")
shopping_cart = ["apple", "banana", "chocolate", "milk"]
for item in shopping_cart:
    if item == "chocolate":
        print(f"{item} is on discount!")
    else:
        print(f"Adding {item} to the bag")
print()
