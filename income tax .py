# Function to calculate tax based on income
def calculate_tax(income):
    if income <= 250000:
        return 0
    elif income <= 500000:
        return (income - 250000) * 0.05
    elif income <= 750000:
        return (income - 500000) * 0.10 + 12500
    elif income <= 1000000:
        return (income - 750000) * 0.15 + 37500
    elif income <= 1250000:
        return (income - 1000000) * 0.20 + 75000
    elif income <= 1500000:
        return (income - 1250000) * 0.25 + 125000
    else:
        return (income - 1500000) * 0.30 + 187500

while True:
    # Input from user
    income = float(input("Enter your annual income: "))

    # Calculate tax
    tax = calculate_tax(income)

    # Display the result
    print(f"Total tax applicable on ₹{income} is ₹{tax:.2f}")

    # Check if user wants another calculation
    next_calculation = input("Do you want to calculate tax for another income? (y/n): ")
    if next_calculation.lower() != 'y':
        break
