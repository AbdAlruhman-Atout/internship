def bmi_calculator(height: float, weight: float) -> dict:

    if not isinstance(height, (int, float)):
        raise ValueError("height must be a number")
    if not isinstance(weight, (int, float)):
        raise ValueError("weight must be a number")
    if height <= 0:
        raise ValueError("height should be a positive number")
    if weight <= 0:
        raise ValueError("weight should be a positive number")

    bmi: float = round(weight / (height**2), 2)
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
