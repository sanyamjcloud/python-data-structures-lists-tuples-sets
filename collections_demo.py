"""
collections_demo.py
Demonstration of Python collections: list, tuple, set
"""

# 1. Store student names in a list
students = ["Amit", "Sanyam", "Ravi", "Neha", "Amit"]

print("Original student list:", students)

# 2. Add elements
students.append("Pooja")
print("After adding Pooja:", students)

# 3. Remove elements
students.remove("Ravi")
print("After removing Ravi:", students)

# 4. Sort elements
students.sort()
print("Sorted student list:", students)

# 5. Tuple for fixed data (immutable)
course_info = ("Python", "3 Months", "Beginner")
print("\nCourse Information (Tuple):", course_info)

# 6. Convert list to set to remove duplicates
unique_students = set(students)
print("\nUnique students (Set):", unique_students)

# 7. Set operations
online_students = {"Sanyam", "Amit", "Neha"}
offline_students = {"Rohit", "Neha"}

print("\nUnion:", online_students | offline_students)
print("Intersection:", online_students & offline_students)
print("Difference:", online_students - offline_students)

# 8. Iterate over collections
print("\nIterating over student list:")
for student in students:
    print("-", student)

print("\nIterating over set:")
for student in unique_students:
    print("-", student)

# 9. Mutable vs Immutable comparison
print("\nMutable vs Immutable Example:")

# Mutable (List)
numbers_list = [1, 2, 3]
numbers_list.append(4)
print("Mutable List:", numbers_list)

# Immutable (Tuple)
numbers_tuple = (1, 2, 3)
print("Immutable Tuple:", numbers_tuple)

print("\nConclusion:")
print("Lists and sets are mutable, tuples are immutable.")
