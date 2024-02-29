# Portfolio Management System

This Python script provides a simple portfolio management system that allows users to track their stock holdings and their total portfolio value. It utilizes the Yahoo Finance API (`yfinance`) to fetch real-time stock prices and stores the data in a CSV file for easy management.

## Features
- **Read and Write Operations:** The script reads stock tickers and quantities from a CSV file and updates the file with new data if requested by the user.
- **Real-time Data Retrieval:** Utilizes the `yfinance` library to fetch the last price of each stock ticker in real-time.
- **Portfolio Valuation:** Calculates the total value of the portfolio based on the current stock prices and quantities held.
- **User Interaction:** Allows users to add new stock data to the portfolio directly through the terminal.

## File Structure
- `portfolio_management.py`: The main Python script containing the portfolio management functionalities.
- `assets.csv`: CSV file storing the stock tickers and quantities.
- `README.md`: Brief documentation describing the script and its usage.

## Instructions
1. **Setup:** Ensure you have Python installed along with the required libraries (`yfinance`, `pandas`).
2. **CSV File:** Modify `assets.csv` with your stock holdings data. The file should have two columns: stock ticker and quantity.
3. **Run the Script:** Execute `portfolio_management.py` to see the current portfolio valuation and interactively add new stock data if desired.
4. **Follow Terminal Prompts:** Respond to the prompts in the terminal to add new stock data or exit the program.

## Usage Example
```
$ python portfolio_management.py

Stock     Quantity   Price      Total     
AAPL      10         $150.00    $1500.00
GOOG      5          $2800.00   $14000.00

Total portfolio value: $15500.00

Do you want to add data to the CSV file? (y/n): y
Enter the new stock ticker: MSFT
Enter the quantity of the stock: 8
```

## Note
- This script fetches real-time stock prices using the Yahoo Finance API, which may have usage limits or require an API key for extended usage.
- Ensure proper handling of sensitive data if deploying this script in a production environment.

Feel free to customize and expand upon this script to suit your specific portfolio management needs!
