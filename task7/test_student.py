import pytest

from student import Student


def test_init_defaults():
    student = Student("Alice", "S001")

    assert student.name == "Alice"
    assert student.student_id == "S001"
    assert student.grades == []


def test_student_count():
    Student.student_count = 0

    Student("Alice", "S001")
    Student("Bob", "S002")

    assert Student.student_count == 2


def test_add_grade_valid():
    student = Student("Alice", "S001")

    student.add_grade(85)

    assert student.grades == [85]


def test_add_grade_invalid_raises():
    student = Student("Alice", "S001")

    with pytest.raises(ValueError):
        student.add_grade(101)


def test_get_average_normal():
    student = Student("Alice", "S001", [85, 90, 95])

    assert student.get_average() == 90.0


def test_get_average_empty():
    student = Student("Alice", "S001")

    assert student.get_average() == 0.0


def test_get_highest():
    student = Student("Alice", "S001", [85, 90, 95])

    assert student.get_highest() == 95


def test_get_lowest():
    student = Student("Alice", "S001", [85, 90, 95])

    assert student.get_lowest() == 85


def test_get_highest_empty_raises():
    student = Student("Alice", "S001")

    with pytest.raises(ValueError):
        student.get_highest()


def test_is_passing_true():
    student = Student("Alice", "S001", [70, 80])

    assert student.is_passing() is True


def test_is_passing_false():
    student = Student("Alice", "S001", [40, 50])

    assert student.is_passing() is False


def test_is_passing_custom_threshold():
    student = Student("Alice", "S001", [85, 90])

    assert student.is_passing(threshold=90) is False


def test_str_output():
    student = Student("Alice", "S001", [85, 90])

    result = str(student)

    assert "Alice" in result
    assert "S001" in result
    assert "87.50" in result


def test_repr_output():
    student = Student("Alice", "S001", [85, 90])

    result = repr(student)

    assert "Student" in result
    assert "Alice" in result
    assert "S001" in result
    assert "[85, 90]" in result


def test_grades_not_shared():
    student1 = Student("Alice", "S001")
    student2 = Student("Bob", "S002")

    student1.add_grade(100)

    assert student1.grades == [100]
    assert student2.grades == []
