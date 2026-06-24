SPECIAL_CHARS = "!@#$%^&*"


class WeakPasswordError(Exception):
    pass


def strong_password(password: str) -> bool:
    if len(password) < 8:
        raise WeakPasswordError("Password must be at least 8 characters long.")

    if not any(char.isupper() for char in password):
        raise WeakPasswordError("Password must contain at least one uppercase letter.")

    if not any(char.isdigit() for char in password):
        raise WeakPasswordError("Password must contain at least one digit.")

    if not any(char in SPECIAL_CHARS for char in password):
        raise WeakPasswordError(
            "Password must contain at least one special character."
        )

    return True


def validate_and_report(password: str) -> dict:
    try:
        strong_password(password)
        return {
            "valid": True,
            "message": "OK",
        }
    except WeakPasswordError as error:
        return {
            "valid": False,
            "message": str(error),
        }