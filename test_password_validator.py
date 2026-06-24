import pytest

from password_validator import WeakPasswordError, strong_password, validate_and_report


def test_valid_password():
    assert strong_password("Strong123!") is True


def test_too_short():
    with pytest.raises(WeakPasswordError):
        strong_password("A1!")


def test_no_uppercase():
    with pytest.raises(WeakPasswordError):
        strong_password("strong123!")


def test_no_digit():
    with pytest.raises(WeakPasswordError):
        strong_password("Stronggg!")


def test_no_special_char():
    with pytest.raises(WeakPasswordError):
        strong_password("Strong123")


def test_empty_string():
    with pytest.raises(WeakPasswordError):
        strong_password("")


def test_report_valid():
    result = validate_and_report("Strong123!")

    assert result == {
        "valid": True,
        "message": "OK",
    }


def test_report_invalid():
    result = validate_and_report("weak")

    assert result["valid"] is False
    assert result["message"] != "OK"


def test_error_message_specific():
    with pytest.raises(WeakPasswordError) as error:
        strong_password("strong123!")

    assert "uppercase" in str(error.value)