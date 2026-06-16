import pytest

from bmi_calculator import bmi_calculator


def test_normal():
    result = bmi_calculator(68.89, 154.3, "imperial")
    assert result["bmi"] == 22.86
    assert result["category"] == "Normal weight"


def test_underweight():
    result = bmi_calculator(1.75, 50)
    assert result["bmi"] == 16.33
    assert result["category"] == "Underweight"


def test_overweight():
    result = bmi_calculator(1.70, 80)
    assert result["bmi"] == 27.68
    assert result["category"] == "Overweight"


def test_Obese():
    result = bmi_calculator(1.60, 90)
    assert result["bmi"] == 35.16
    assert result["category"] == "Obese"


def test_zero_height():
    with pytest.raises(ValueError):
        bmi_calculator(0, 70)


def test_negative_weight():
    with pytest.raises(ValueError):
        bmi_calculator(1.70, -5)


def test_string_input():
    with pytest.raises(ValueError):
        bmi_calculator("tall", 70)

@pytest.mark.parametrize(
    "height, weight, expected_bmi, expected_category",
    [
        (1.75, 50, 16.33, "Underweight"),
        (1.75, 70, 22.86, "Normal weight"),
        (1.70, 80, 27.68, "Overweight"),
        (1.60, 90, 35.16, "Obese"),
    ],
)
def test_bmi_calculator(height, weight, expected_bmi, expected_category):
    result = bmi_calculator(height, weight)
    assert result["bmi"] == expected_bmi
    assert result["category"] == expected_category