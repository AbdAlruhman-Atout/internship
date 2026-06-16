import pytest


def bmi_calculator(height: float, weight: float, system: str = "metric") -> dict:

    if system == "metric":
        height_conversion_factor = 1
        weight_conversion_factor = 1

    elif system == "imperial":
        height_conversion_factor = 0.0254
        weight_conversion_factor = 0.453592

    else:
        raise ValueError("invalid measurement system")

    if not isinstance(height, (int, float)) or not isinstance(weight, (int, float)):
        raise ValueError("height and weight must be numbers")
    if height <= 0 or weight <= 0:
        raise ValueError("height and weight must be positive numbers")

    # short-circuit evaluation : program stops evaluating the expression once it determines the output
    # for example : true or expression -> expression is not evaluated/executes
    #              false and expression-> expression is not evaluated/executed

    bmi: float = round(
        weight * weight_conversion_factor / ((height_conversion_factor * height) ** 2),
        2,
    )
    category: str
    match bmi:
        case _ if bmi < 18.5:
            category = "Underweight"
        case _ if bmi < 25:
            category = "Normal weight"
        case _ if bmi < 30:
            category = "Overweight"
        case _:
            category = "Obese"

    label = "looks good" if category == "Normal weight" else "consult a doctor"

    return {"bmi": bmi, "category": category, "label": label}
