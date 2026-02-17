
def get_marks():
    try:
        marks = float(input("Enter your marks: "))
        if marks < 0 or marks > 100:
            raise ValueError("Marks must be between 0 and 100.")
        return marks
    except ValueError as e:
        print("Error:", e)
        return None

def evaluate_marks(marks):
    if marks > 80:
        print("You got distinction")
    elif marks > 60:
        print("You got First class")
    elif marks > 40:
        print("You got second class")
    elif marks >= 35:
        print("PASS")
    else:
        print("Fail")


def main():
    marks = get_marks()
    if marks is not None:
        evaluate_marks(marks)


if __name__ == "__main__":
    main()
    
# ------------------

def get_salary():
    try:
        salary = float(input("Enter employee salary per year (LPA): "))
        if salary < 0:
            raise ValueError("Salary cannot be negative.")
        return salary
    except ValueError as e:
        print("Error:", e)
        return None


def get_rating():
    try:
        rating = input("Enter employee rating (A/B/C/D): ").upper()
        if rating not in ['A', 'B', 'C', 'D']:
            raise ValueError("Rating must be A, B, C or D.")
        return rating
    except ValueError as e:
        print("Error:", e)
        return None


def calculate_increment(salary, rating):

    if salary <= 5:
        rates = {'A': 16, 'B': 12, 'C': 10, 'D': 6}

    elif salary <= 10:
        rates = {'A': 14, 'B': 10, 'C': 8, 'D': 6}

    elif salary <= 15:
        rates = {'A': 8, 'B': 6, 'C': 4, 'D': 0}

    elif salary <= 23:
        rates = {'A': 7, 'B': 5, 'C': 4, 'D': 0}

    else:
        print("No increment policy for salary above 23 LPA.")
        return

    percent = rates[rating]
    new_salary = salary + (salary * percent / 100)

    print("Increment Percentage:", percent, "%")
    print("New Salary after increment:", new_salary, "LPA")

def main():
    salary = get_salary()
    if salary is None:
        return

    rating = get_rating()
    if rating is None:
        return

    calculate_increment(salary, rating)


if __name__ == "__main__":
    main()
