import yfinance as yf
import pandas as pd
import os

def read_file(file_path):
    stock = pd.read_csv(file_path, delimiter=',', nrows=1, header=None)
    quantity = pd.read_csv(file_path, delimiter=',', skiprows=1, nrows=1, header=None)
    return stock, quantity

def write_to_file(file_path, new_data):
    # read existing data
    existing_stock, existing_quantity = read_file(file_path)

    # combine existing data with new data
    combined_stock = existing_stock.values.tolist()[0] + [new_data[0]]
    combined_quantity = existing_quantity.values.tolist()[0] + [new_data[1]]

    # write combined data back to the file
    with open(file_path, 'w') as f:
        f.write(','.join(map(str, combined_stock)) + '\n')
        f.write(','.join(map(str, combined_quantity)))

def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, "assets.csv")
    stock, quantity = read_file(file_path)
    tickers = stock.values.tolist()[0]
    quantities = quantity.values.tolist()[0]

    total_value = 0
    print(f"{'Stock':<10} {'Quantity':<10} {'Price':<10} {'Total':<10}")

    for ticker, qty in zip(tickers, quantities):
        price = yf.Ticker(ticker).fast_info["last_price"]
        price_formatted = "{:.2f}".format(price)
        value = price * qty
        print(f"{ticker:<10} {qty:<10} ${price_formatted:<10} ${value:.2f}")
        total_value += value

    print(f"\n{'Total portfolio value:':<10} ${total_value:.2f}")

    add_data = input("Do you want to add data to the CSV file? (y/n): ")
    if add_data.lower() == 'y':
        new_ticker = input("Enter the new stock ticker: ")
        new_quantity = input("Enter the quantity of the stock: ")
        new_data = (new_ticker, new_quantity)
        write_to_file(file_path, new_data)

if __name__ == "__main__":
    main()
