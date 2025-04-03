import requests
import os

# Function to load API key securely from api_keys.txt
def load_api_key(file_path="api_keys.txt"):
    """Load API key from the given file."""
    try:
        with open(file_path, "r") as file:
            api_key = file.readline().strip().split('=')[1]  # Assuming format is KEY=value
            return api_key
    except FileNotFoundError:
        print(f"Error: {file_path} not found. Please provide a valid API key file.")
        return None
    except IndexError:
        print("Error: Invalid API key file format. Ensure it is in 'KEY=value' format.")
        return None

# Fetch real-time stock price using the Alpha Vantage API
def get_stock_price(symbol, api_key):
    """Fetch real-time stock price using Alpha Vantage API."""
    BASE_URL = "https://www.alphavantage.co/query"
    params = {
        "function": "GLOBAL_QUOTE",
        "symbol": symbol,
        "apikey": api_key
    }
    
    try:
        response = requests.get(BASE_URL, params=params)
        data = response.json()
        
        # Check if the response contains valid data
        if "Global Quote" in data and "05. price" in data["Global Quote"]:
            return float(data["Global Quote"]["05. price"])
        else:
            print("Invalid stock symbol or API limit reached.")
            return None
    except requests.exceptions.RequestException as e:
        print(f"Error fetching stock data: {e}")
        return None

# Add a stock to the portfolio
def add_stock(symbol, quantity, portfolio, api_key):
    """Add a stock to the portfolio."""
    price = get_stock_price(symbol, api_key)
    if price:
        portfolio[symbol] = {"quantity": quantity, "price": price}
        print(f"Added {quantity} shares of {symbol} at ${price:.2f} each.")
    else:
        print("Failed to add stock. Unable to fetch stock price.")

# Remove a stock from the portfolio
def remove_stock(symbol, portfolio):
    """Remove a stock from the portfolio."""
    if symbol in portfolio:
        del portfolio[symbol]
        print(f"Removed {symbol} from the portfolio.")
    else:
        print(f"Stock {symbol} not found in portfolio.")

# Display the current portfolio
def view_portfolio(portfolio):
    """Display the current portfolio."""
    if not portfolio:
        print("Portfolio is empty.")
        return
    total_value = 0
    print("\nYour Stock Portfolio:")
    print("Symbol | Quantity | Price | Total Value")
    print("--------------------------------------")
    
    for symbol, data in portfolio.items():
        stock_value = data['quantity'] * data['price']
        total_value += stock_value
        print(f"{symbol} | {data['quantity']} | ${data['price']:.2f} | ${stock_value:.2f}")
    
    print("--------------------------------------")
    print(f"Total Portfolio Value: ${total_value:.2f}\n")

# Main function to run the Stock Portfolio Tracker
def main():
    """Main entry point for the Stock Portfolio Tracker."""
    portfolio = {}
    api_key = load_api_key()  # Load API key from file
    
    if not api_key:
        print("Exiting the program due to missing API key.")
        return
    
    while True:
        print("\nStock Portfolio Tracker")
        print("1. Add Stock")
        print("2. Remove Stock")
        print("3. View Portfolio")
        print("4. Exit")
        choice = input("Enter your choice: ")
        
        if choice == "1":
            symbol = input("Enter stock symbol (e.g., AAPL, TSLA): ").upper()
            quantity = int(input("Enter quantity: "))
            add_stock(symbol, quantity, portfolio, api_key)
        elif choice == "2":
            symbol = input("Enter stock symbol to remove: ").upper()
            remove_stock(symbol, portfolio)
        elif choice == "3":
            view_portfolio(portfolio)
        elif choice == "4":
            print("Exiting Stock Portfolio Tracker.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
