class Student:
    student_count = 0

    def __init__(self, name, student_id, grades=None):
        self.name = name
        self.student_id = student_id
        self.grades = grades if grades is not None else []

        Student.student_count += 1

    def add_grade(self, grade):
        if grade < 0 or grade > 100:
            raise ValueError("Grade must be between 0 and 100")

        self.grades.append(grade)

    def get_average(self):
        if not self.grades:
            return 0.0

        return round(sum(self.grades) / len(self.grades), 2)

    def get_highest(self):
        if not self.grades:
            raise ValueError("No grades available")

        return max(self.grades)

    def get_lowest(self):
        if not self.grades:
            raise ValueError("No grades available")

        return min(self.grades)

    def is_passing(self, threshold=60):
        return self.get_average() >= threshold

    def __str__(self):
        return (
            f"Student: {self.name} | "
            f"ID: {self.student_id} | "
            f"Average: {self.get_average():.2f}"
        )

    def __repr__(self):
        return (
            f"Student(name={self.name!r}, "
            f"student_id={self.student_id!r}, "
            f"grades={self.grades!r})"
        )
