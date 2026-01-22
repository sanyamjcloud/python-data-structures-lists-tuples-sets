def calculate_grade(marks):
    """
    Determines grade based on marks using business-style rules.
    """

    # Handle invalid marks
    if marks < 0 or marks > 100:
        return "Invalid marks! Please enter a value between 0 and 100."

    if marks >= 90 and marks <= 100:
        return "Grade A+ : Outstanding performance"
    elif marks >= 80 and marks < 90:
        return "Grade A : Excellent performance"
    elif marks >= 70 and marks < 80:
        return "Grade B : Good performance"
    elif marks >= 60 and marks < 70:
        return "Grade C : Average performance"
    elif marks >= 40 and marks < 60:
        return "Grade D : Needs improvement"
    else:
        return "Grade F : Fail"


def main():
    try:
        marks = float(input("Enter your marks (0-100): "))
        print(calculate_grade(marks))
    except ValueError:
        print("Invalid input! Please enter numeric marks only.")


if __name__ == "__main__":
    main()
