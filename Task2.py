
# Task 2: Stock Portfolio Tracker (Beginner-Friendly Version)

print("📈 Welcome to the Stock Portfolio Tracker!\n")

# Create an empty dictionary to store stocks
portfolio = {}

# Ask how many stocks the user wants to enter
num_stocks = int(input("How many stocks do you want to add? "))

# Loop to take stock details
for i in range(num_stocks):
    print(f"\nEnter details for Stock {i + 1}:")
    name = input("Enter stock name: ").capitalize()
    quantity = int(input("Enter quantity: "))
    price = float(input("Enter price per share (₹): "))
    
    # Store stock details in dictionary
    portfolio[name] = {
        "Quantity": quantity,
        "Price": price,
        "Total Value": quantity * price
    }

# Display portfolio summary
print("\n📊 Your Stock Portfolio Summary:")
print("----------------------------------")

total_portfolio_value = 0

for stock, details in portfolio.items():
    print(f"{stock}: Quantity = {details['Quantity']}, Price = ₹{details['Price']}, Total = ₹{details['Total Value']}")
    total_portfolio_value += details["Total Value"]

print("----------------------------------")
print(f"💰 Total Portfolio Value: ₹{total_portfolio_value}")
