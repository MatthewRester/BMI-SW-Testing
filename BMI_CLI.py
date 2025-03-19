from BMI_Calculator import calculate_bmi, categorize_bmi

def get_user_input():
    try:
        feet = int(input("Enter height (feet component): "))
        inches = int(input("Enter height (inches component): "))
        weight = float(input("Enter weight (pounds): "))

        height_in_inches = (feet * 12) + inches

        bmi = calculate_bmi(height_in_inches, weight)
        category = categorize_bmi(bmi)

        print(f"\nYour BMI is {bmi}, which falls into the '{category}' category.\n")
    
    # Throw an error if input is not numerical.
    except ValueError:
        print("Invalid input. Please enter numerical values for height and weight.")

    # This keeps the terminal window open until the user decides to close it.
    input("Press Enter to exit...")

if __name__ == "__main__":
    get_user_input()
