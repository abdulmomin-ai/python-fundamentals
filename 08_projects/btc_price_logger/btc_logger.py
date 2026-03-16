import requests
import pandas as pd
import os
from datetime import datetime


# Ensure logs folder exists

BASE_DIR = os.path.dirname(os.path.abspath(__file__))    # Get current script directory
LOGS_DIR = os.path.join(BASE_DIR, "logs")
if not os.path.exists(LOGS_DIR):
    os.makedirs(LOGS_DIR)

FILE_PATH = os.path.join(LOGS_DIR, "btc_log.csv")


# Fetch Bitcoin price from API

def fetch_btc_price():
    url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd"
    try:
        response = requests.get(url, timeout=10)  # timeout for network safety
        response.raise_for_status()  # raise error if status != 200
        data = response.json()       # convert JSON to dict
        price = data['bitcoin']['usd']
        return price
    except requests.exceptions.RequestException as e:
        print("API Request failed:", e)
        return None


# Log price to CSV

def log_price():
    price = fetch_btc_price()
    
    if price is not None:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # formatted timestamp
        df = pd.DataFrame([[timestamp, price]], columns=["Timestamp", "BTC_Price_USD"])

        # Append or create CSV
        if os.path.exists(FILE_PATH):
            df.to_csv(FILE_PATH, mode='a', header=False, index=False)
        else:
            df.to_csv(FILE_PATH, index=False)

        print(f"[{timestamp}] Logged Successfully: BTC Price = ${price}")
    else:
        print("Failed to fetch BTC price")


if __name__ == "__main__":
    log_price()

