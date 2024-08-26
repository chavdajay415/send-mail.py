def calculate_gst(amount, gst_rate):
    """
    Calculate the GST amount based on the given amount and GST rate.

    Parameters:
    amount (float): The original amount before GST.
    gst_rate (float): The GST rate as a percentage.

    Returns:
    tuple: A tuple containing the GST amount and the total amount (amount + GST).
    """
    gst_amount = (amount * gst_rate) / 100
    total_amount = amount + gst_amount
    return gst_amount, total_amount

def main():
    while True:
        try:
            # Input the amount and GST rate from the user
            amount = float(input("Enter the amount: "))
            gst_rate = float(input("Enter the GST rate (in %): "))

            # Calculate GST and total amount
            gst_amount, total_amount = calculate_gst(amount, gst_rate)

            # Display the results
            print(f"\nGST Amount: {gst_amount:.2f}")
            print(f"Total Amount (including GST): {total_amount:.2f}\n")

            # Ask the user if they want to perform another calculation
            another = input("Do you want to perform another calculation? (y/n): ").strip().lower()
            if another != 'y':
                print("Thank you for using the GST calculator.")
                break
        except ValueError:
            print("Invalid input. Please enter numeric values.")

if __name__ == "__main__":
    main()
