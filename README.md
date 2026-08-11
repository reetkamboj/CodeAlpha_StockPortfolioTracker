# CodeAlpha_StockPortfolioTracker

A simple stock portfolio tracker built in Python. Completed as **Task 2: Stock Portfolio Tracker** for the CodeAlpha Python Programming Internship.

## Description
The user enters stock symbols and quantities from a predefined price list. The script calculates how much each holding is worth, shows a full breakdown plus the total investment value, and can optionally save the summary to a CSV file.

## Concepts Used
- **Dictionaries** – `STOCK_PRICES` hardcodes each stock symbol and its price; the user's holdings are also tracked in a dictionary (`{symbol: quantity}`).
- **Input/Output** – `input()` collects stock symbols and quantities in a loop; `print()` displays the available stocks and the final summary.
- **Basic arithmetic** – each stock's value is `price * quantity`, and these are summed for the total investment.
- **File handling (optional)** – if the user chooses to, the summary is written to a `.csv` file using Python's built-in `csv` module.
- **Functions** – logic is split into `build_portfolio()`, `calculate_investment()`, `display_summary()`, and `save_to_csv()`.

## Files
- `stock_tracker.py` – the script
- `README.md` – this file

## How to Run
1. Make sure Python 3 is installed.
2. Run:
   ```
   python stock_tracker.py
   ```
3. Enter a stock symbol from the list shown (e.g. `AAPL`), then its quantity. Repeat for as many stocks as you like, then type `done`.
4. Choose whether to save the summary to a CSV file when prompted.

## Example
```
Stock symbol (or 'done'): AAPL
Quantity of AAPL: 10
Added 10 share(s) of AAPL.

Stock symbol (or 'done'): TSLA
Quantity of TSLA: 5
Added 5 share(s) of TSLA.

Stock symbol (or 'done'): done

--- Portfolio Summary ---
Stock   Qty   Price     Value
AAPL    10    $180      $1800
TSLA    5     $250      $1250
----------------------------------
Total Investment Value: $3050
```

## Possible Improvements
- Fetch live stock prices from a free API instead of a hardcoded dictionary.
- Let the user remove a stock or edit a quantity before finishing.
- Show each holding's percentage of the total portfolio.
