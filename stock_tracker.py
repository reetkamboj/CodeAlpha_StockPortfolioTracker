"""
Stock Portfolio Tracker
Calculates total investment value based on user-entered stock quantities
and a hardcoded dictionary of stock prices.

Concepts used: dictionary, input/output, basic arithmetic, file handling (optional)
"""

import csv

# Hardcoded stock prices (in USD)
STOCK_PRICES = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 410,
    "AMZN": 185,
    "META": 480,
    "NFLX": 670,
    "NVDA": 125,
}


def show_available_stocks():
    print("Available stocks and prices (USD):")
    for symbol, price in STOCK_PRICES.items():
        print(f"  {symbol}: ${price}")
    print()


def build_portfolio():
    """It ask to the user for stock symbols and quantities until they type 'done'."""
    portfolio = {}

    print("Enter a stock symbol and quantity to add it to your portfolio.")
    print("Type 'done' as the stock symbol when you're finished.\n")

    while True:
        symbol = input("Stock symbol (or 'done'): ").upper().strip()

        if symbol == "DONE":
            break

        if symbol not in STOCK_PRICES:
            print(f"'{symbol}' isn't in the price list. Try one of: {', '.join(STOCK_PRICES)}\n")
            continue

        while True:
            qty_input = input(f"Quantity of {symbol}: ").strip()
            if qty_input.isdigit() and int(qty_input) > 0:
                quantity = int(qty_input)
                break
            print("Please enter a positive whole number for quantity.")

        portfolio[symbol] = portfolio.get(symbol, 0) + quantity
        print(f"Added {quantity} share(s) of {symbol}.\n")

    return portfolio


def calculate_investment(portfolio):
    """Return a list of (symbol, quantity, price, value) rows and the grand total."""
    rows = []
    total = 0

    for symbol, quantity in portfolio.items():
        price = STOCK_PRICES[symbol]
        value = price * quantity
        rows.append((symbol, quantity, price, value))
        total += value

    return rows, total


def display_summary(rows, total):
    print("\n--- Portfolio Summary ---")
    print(f"{'Stock':<8}{'Qty':<6}{'Price':<10}{'Value':<10}")
    for symbol, quantity, price, value in rows:
        print(f"{symbol:<8}{quantity:<6}${price:<9}${value:<9}")
    print("-" * 34)
    print(f"Total Investment Value: ${total}")


def save_to_csv(rows, total, filename="portfolio_summary.csv"):
    with open(filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["Stock", "Quantity", "Price", "Value"])
        for row in rows:
            writer.writerow(row)
        writer.writerow([])
        writer.writerow(["Total", "", "", total])
    print(f"Saved summary to '{filename}'.")


if __name__ == "__main__":
    print("=== Stock Portfolio Tracker ===\n")
    show_available_stocks()

    portfolio = build_portfolio()

    if not portfolio:
        print("No stocks were added. Exiting.")
    else:
        rows, total = calculate_investment(portfolio)
        display_summary(rows, total)

        save_choice = input("\nSave this summary to a CSV file? (y/n): ").lower().strip()
        if save_choice == "y":
            save_to_csv(rows, total)
        else:
            print("Summary not saved.")
