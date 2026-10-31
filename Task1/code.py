
# University Scholarship Allocation System

AGGREGATE_MIN = 75
SUBJECT_MIN = 60
ATTENDANCE_MIN = 75
INCOME_MAX = 250000


def check_eligibility(student):
    """Return True if the student satisfies all scholarship criteria."""
    return (
        student["aggregate"] >= AGGREGATE_MIN
        and all(mark >= SUBJECT_MIN for mark in student["subjects"])
        and student["attendance"] >= ATTENDANCE_MIN
        and student["income"] <= INCOME_MAX
    )


def main():
    students = []
    eligible_students = []

    n = int(input("Enter number of applicants: "))

    for i in range(n):
        print(f"\nApplicant {i + 1}")

        name = input("Enter student name: ")
        aggregate = float(input("Enter aggregate marks (%): "))

        subject_count = int(input("Enter number of subjects: "))
        subjects = []

        for j in range(subject_count):
            mark = float(input(f"Enter subject {j + 1} marks (%): "))
            subjects.append(mark)

        attendance = float(input("Enter attendance (%): "))
        income = float(input("Enter annual family income (₹): "))

        student = {
            "name": name,
            "aggregate": aggregate,
            "subjects": subjects,
            "attendance": attendance,
            "income": income,
        }

        students.append(student)

        if check_eligibility(student):
            eligible_students.append(student)

    # Ranking: aggregate, attendance, minimum subject mark,
    # and lower family income.
    eligible_students.sort(
        key=lambda s: (
            -s["aggregate"],
            -s["attendance"],
            -min(s["subjects"]),
            s["income"],
        )
    )

    print("\n--- SCHOLARSHIP ALLOCATION RESULTS ---")

    if not eligible_students:
        print("No eligible applicants.")
    else:
        print(
            f"{'Rank':<6}{'Name':<20}{'Aggregate':<12}"
            f"{'Attendance':<12}{'Min Subject':<13}{'Income (₹)':<12}"
        )
        print("-" * 75)

        for rank, student in enumerate(eligible_students, start=1):
            print(
                f"{rank:<6}{student['name']:<20}"
                f"{student['aggregate']:<12.2f}"
                f"{student['attendance']:<12.2f}"
                f"{min(student['subjects']):<13.2f}"
                f"{student['income']:<12.2f}"
            )

    print("\nIneligible Applicants:")
    for student in students:
        if not check_eligibility(student):
            print(student["name"])


if __name__ == "__main__":
    main()

