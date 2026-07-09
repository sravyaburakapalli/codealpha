# Stock Portfolio Tracker

# Predefined stock prices
stock_prices = {
    "apple": 180,
    "tesla": 250,
    "google": 140,
    "amazon": 160,
    "microsoft": 320
}

portfolio = {}
total_value = 0

print("=" * 40)
print("     STOCK PORTFOLIO TRACKER")
print("=" * 40)

print("\nAvailable Stocks:")
for stock, price in stock_prices.items():
    print(f"{stock.title()} : ${price}")

while True:
    stock = input("\nEnter stock name (or type 'done' to finish): ").lower()

    if stock == "done":
        break

    if stock not in stock_prices:
        print("Stock not available.")
        continue

    quantity = int(input(f"Enter quantity of {stock.title()}: "))

    portfolio[stock] = portfolio.get(stock, 0) + quantity

print("\n" + "=" * 40)
print("        PORTFOLIO SUMMARY")
print("=" * 40)

for stock, quantity in portfolio.items():
    value = stock_prices[stock] * quantity
    total_value += value
    print(f"{stock.title():12} Quantity: {quantity:<3} Value: ${value}")

print("-" * 40)
print(f"Total Portfolio Value = ${total_value}")
print("=" * 40)

# Save to file
with open("portfolio_summary.txt", "w") as file:
    file.write("STOCK PORTFOLIO SUMMARY\n")
    file.write("=" * 35 + "\n")

    for stock, quantity in portfolio.items():
        value = stock_prices[stock] * quantity
        file.write(f"{stock.title()} - Quantity: {quantity} - Value: ${value}\n")

    file.write("=" * 35 + "\n")
    file.write(f"Total Portfolio Value = ${total_value}")

print("\nPortfolio summary has been saved to 'portfolio_summary.txt'.")