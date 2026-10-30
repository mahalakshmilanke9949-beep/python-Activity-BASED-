Here you # University Scholarship Allocation System

# Eligibility Criteria
MIN_AGGREGATE = 75
MIN_SUBJECT_MARKS = 40
MIN_ATTENDANCE = 75
MAX_INCOME = 300000

students = []
eligible_students = []

# Get number of students
n = int(input("Enter number of students: "))

# Input student details
for i in range(n):

    print("\nEnter details of Student", i + 1)

    name = input("Enter student name: ")

    aggregate = float(input("Enter aggregate marks: "))

    attendance = float(input("Enter attendance percentage: "))

    income = float(input("Enter annual family income: "))

    subjects = int(input("Enter number of subjects: "))

    marks = []

    for j in range(subjects):
        mark = float(input("Enter marks of subject " + str(j + 1) + ": "))
        marks.append(mark)

    # Check eligibility
    if (aggregate >= MIN_AGGREGATE and
        all(mark >= MIN_SUBJECT_MARKS for mark in marks) and
        attendance >= MIN_ATTENDANCE and
        income <= MAX_INCOME):

        eligible_students.append({
            "name": name,
            "aggregate": aggregate,
            "attendance": attendance,
            "income": income
        })

        print(name, "is eligible for scholarship.")

    else:
        print(name, "is not eligible for scholarship.")


# Sort eligible students
# Priority:
# 1. Higher aggregate marks
# 2. Higher attendance
# 3. Lower family income

eligible_students.sort(
    key=lambda x: (
        -x["aggregate"],
        -x["attendance"],
        x["income"]
    )
)


# Display scholarship ranking
print("\n========== SCHOLARSHIP MERIT LIST ==========")

if len(eligible_students) == 0:

    print("No students are eligible for scholarship.")

else:

    print("{:<10} {:<15} {:<15} {:<15} {:<15}".format(
        "Rank", "Name", "Aggregate", "Attendance", "Income"
    ))

    for rank, student in enumerate(eligible_students, start=1):

        print("{:<10} {:<15} {:<15} {:<15} {:<15}".format(
            rank,
            student["name"],
            student["aggregate"],
            student["attendance"],
            student["income"]
        ))

print("\nProgram Completed.")
have to write the code
