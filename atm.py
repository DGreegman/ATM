# Initialize the account balance
balance = 1000

# Function to display the account balance
def display_balance():
    print(f"Your account balance is: ${balance}")

# Function to withdraw funds
def withdraw():
    global balance  # Use the global balance variable
    amount = float(input("Enter the amount to withdraw: $"))
    if amount > 0 and amount <= balance:
        balance -= amount
        print(f"Withdrawn ${amount}.")
    else:
        print("Invalid amount or insufficient balance.")

# Main ATM loop
while True:
    print("\nWelcome to the Simple ATM")
    print("1. Check Balance")
    print("2. Withdraw Funds")
    print("3. Exit")

    choice = input("Please select an option (1/2/3): ")

    if choice == '1':
        display_balance()
    elif choice == '2':
        withdraw()
    elif choice == '3':
        print("Thank you for using the Simple ATM. Goodbye!")
        break
    else:
        print("Invalid choice. Please select a valid option (1/2/3).")
