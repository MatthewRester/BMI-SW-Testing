# This function takes the person's height and weight and returns their bmi.
def calculate_bmi(height_in_inches, weight_in_pounds):
    if height_in_inches <= 0 or weight_in_pounds <= 0:
        raise ValueError("Height and weight must be positive values.")

    weight_in_kilos = weight_in_pounds * 0.45359237
    height_in_meters = height_in_inches * 0.0254
    bmi = weight_in_kilos / height_in_meters**2
    return round(bmi, 1)  # Round to 1 decimal place

# This function takes a person's bmi and categorizes them in one of 4 categories.
def categorize_bmi(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi <= 24.9:
        return "Normal weight"
    elif 25.0 <= bmi <= 29.9:
        return "Overweight"
    else:
        return "Obese"
    
