from functools import reduce

students = [
    {"name": "Alice", "grade": 88},
    {"name": "Bob", "grade": 72},
    {"name": "Carol", "grade": 95},
    {"name": "David", "grade": 61},
    {"name": "Eva", "grade": 79},
    {"name": "Frank", "grade": 55},
    {"name": "Grace", "grade": 91},
]


def get_top_students(students, n=3):
    return sorted(students, key=lambda x: x["grade"], reverse=True)[:n]


def get_pass_fail(students, passing_grade=60):
    return {
        student["name"]: "Pass" if student["grade"] >= passing_grade else "Fail"
        for student in students
    }


def get_grade_labels(students):

    return [f'{student["name"]}: {student["grade"]}' for student in students]


def get_unique_grades(students):
    return {student["grade"] for student in students}


def summarize(students):
    total_number = len(students)
    grades = list(map(lambda student: student["grade"], students))
    grades_sum = reduce(lambda x, y: x + y, grades)
    average = round(grades_sum / total_number, 2)
    has_top_scorer = any(student["grade"] > 90 for student in students)
    all_passed = all(student["grade"] >= 60 for student in students)
    passing_students = filter(lambda student: student["grade"] >= 60, students)
    passing_students_names = list(
        map(lambda student: student["name"], passing_students)
    )
    summary = {
        "total": total_number,
        "average": average,
        "has_top_scorer": has_top_scorer,
        "all_passed": all_passed,
        "passing_students": passing_students_names,
    }

    for i, student in enumerate(students):
        print(f' {i + 1} : {student["name"]} - {student["grade"]} ')
    return summary


def find_student(students, name):
    i = 0
    while i < len(students):
        if students[i]["name"] != name:
            i += 1
            continue

        else:
            break

    if i == len(students):
        return None

    return students[i]


def has_student(
    students, name
):  # this function is only added to demonstrate the for/else block
    for student in students:
        if student["name"] == name:
            return True
    else:
        # else runs only if the loop finishes without finding a match
        return False


def get_grade_distribution(students):
    distribution = {
        "A": 0,
        "B": 0,
        "C": 0,
        "D": 0,
        "F": 0,
    }

    for student in students:
        grade = student["grade"]

        if grade >= 90:
            distribution["A"] += 1
        elif grade >= 80:
            distribution["B"] += 1
        elif grade >= 70:
            distribution["C"] += 1
        elif grade >= 60:
            distribution["D"] += 1
        else:
            distribution["F"] += 1

    return distribution
