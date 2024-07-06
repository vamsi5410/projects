import pywebio
def calculate_bmi(weight, height):
    """
    Calculate BMI based on weight (kg) and height (m).
    """
    bmi = weight / (height ** 2)
    return bmi

def classify_bmi(bmi):
    """
    Classify BMI into categories (underweight, normal, overweight).
    """
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal Weight"
    else:
        return "Overweight"

def main():
    print("BMI Calculator")

    # Input weight and height from the user
    try:
        weight = float(input("Enter your weight in kilograms: "))
        height = float(input("Enter your height in meters: "))
    except ValueError:
        print("Invalid input. Please enter numeric values for weight and height.")
        return

    # Check if weight and height are positive
    if weight <= 0 or height <= 0:
        print("Invalid input. Please enter positive values for weight and height.")
        return

    # Calculate BMI
    bmi = calculate_bmi(weight, height)

    # Classify BMI
    category = classify_bmi(bmi)

    # Display the results
    print(f"\nYour BMI is: {bmi:.2f}")
    print(f"You are classified as: {category}")

if __name__ == "__main__":
    main()
