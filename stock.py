# Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 150,
    "MSFT": 400,
    "AMZN": 170
}

total_investment = 0
portfolio = {}

print("===== STOCK PORTFOLIO TRACKER =====")
print("Available Stocks:")
for stock, price in stock_prices.items():
    print(f"{stock} : ${price}")

# Number of different stocks
n = int(input("\nHow many different stocks do you want to buy? "))

# Get user input
for i in range(n):
    stock_name = input("\nEnter stock name: ").upper()

    if stock_name in stock_prices:
        quantity = int(input("Enter quantity: "))
        portfolio[stock_name] = quantity

        investment = stock_prices[stock_name] * quantity
        total_investment += investment
    else:
        print("Stock not available!")

# Display Portfolio
print("\n===== YOUR PORTFOLIO =====")
for stock, quantity in portfolio.items():
    price = stock_prices[stock]
    value = price * quantity
    print(f"{stock} - Quantity: {quantity}, Value: ${value}")

print(f"\nTotal Investment Value = ${total_investment}")

# Save to a text file
with open("portfolio.txt", "w") as file:
    file.write("STOCK PORTFOLIO\n")
    file.write("---------------------\n")

    for stock, quantity in portfolio.items():
        price = stock_prices[stock]
        value = price * quantity
        file.write(
            f"{stock} - Quantity: {quantity}, Value: ${value}\n"
        )

    file.write(f"\nTotal Investment Value = ${total_investment}")

print("\nPortfolio saved to 'portfolio.txt'")