import pytest
from grades import *


def test_top_students_count():
    result = get_top_students(students)
    assert len(result) == 3


def test_top_students_order():
    result = get_top_students(students)
    assert result[0]["grade"] == 95


def test_top_students_custom_n():
    result = get_top_students(students, 1)
    assert len(result) == 1


def test_pass_fail_pass():
    result = get_pass_fail(students)
    assert result["Alice"] == "Pass"


def test_pass_fail_fail():
    result = get_pass_fail(students)
    assert result["Frank"] == "Fail"


def test_pass_fail_custom_threshold():
    result = get_pass_fail(students, 90)
    assert result["Alice"] == "Fail"


def test_summarize_average():
    result = summarize(students)
    assert result["average"] == 77.29


def test_summarize_has_top_scorer():
    result = summarize(students)
    assert result["has_top_scorer"] is True


def test_summarize_all_passed():
    result = summarize(students)
    assert result["all_passed"] is False


def test_find_student_found():
    result = find_student(students, "Alice")
    assert result == {"name": "Alice", "grade": 88}


def test_find_student_not_found():
    result = find_student(students, "John")
    assert result is None


@pytest.mark.parametrize(
    " passing_grade, student_name, expected_result",
    [
        (80, "Alice", "Pass"),
        (75, "Bob", "Fail"),
        (60, "Carol", "Pass"),
        (50, "Frank", "Pass"),
        (70, "David", "Fail"),
    ],
)
def test_get_pass_fail(passing_grade, student_name, expected_result):
    result = get_pass_fail(students, passing_grade)
    assert result[student_name] == expected_result
