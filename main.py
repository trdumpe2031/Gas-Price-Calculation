# Gas Price Calculation System
# Dumpe, Celicious, Lavador
# This program will calculate the total cost, handle different payment options, and provide clear receipts. 


# Function to get gas type and price
def GetGasType(code):
    if code == 1:
        return "Regular", 94.50
    elif code == 2:
        return "Premium", 96.50
    elif:
        return "Full Meal", 92.20
    else: 
        return None, 0

# Function to calculate total price
def CalculateTotalPrice(price, quantity):
    return price * quantity

# Function to calculate change
def CalculateChange(payment, total):
    return payment - total

# Main Program Loop
while True:
    print("Gas Price Calculation System")
    print("1 - Regular (94.50)")
    print("2 - Premium (96.50)")
    print("3 - Diesel (92.20)")
    print("0 - Exit")

    # Input validation for gas type
    code = int(input("Gas type: "))
    if code == 0:
        break

    gas_type, price = GetGasType(code)

    if gas_type is None: 
        print("Invalid choice")
        continue

    quantity = float(input("Quantity of gas in liters: "))
    payment = float(input("Payment: "))

    # Process
    total = CalculateTotalPrice(price, quantity)
    change = CalculateChange(payment, total)

    # Output
    print("\n----RECEIPT----")
    print("Gas Type: ", gas_type)
    print("Quantity of gas in liters: ", quantity)
    print("Price per liter: ", price)
    print("Total cost: ", total)
    print("Payment: ", payment)
    print("Change: ", change)
