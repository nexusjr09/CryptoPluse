import requests
import sys
def main():
    coin_input = input("Enter coin name or symbol (e.g., bitcoin, BTC): ").lower()
    if coin_input.isdigit():
         sys.exit("Invalid Input")
    print(coin_price(coin_input))
    print(get_historical_prices(coin_input))
    

def coin_price(input):
    
    url = "https://rest.coincap.io/v3/assets?apiKey=353debcd0dbc55a8a2f151d3c6984de7d5b0a7cadb17d42a054ebf7ed3f2038b"
    response = requests.get(url)
    data = response.json()
    for coin in data["data"]:
         if input == coin["id"].lower() or input == coin["symbol"].lower():
                price = float(coin["priceUsd"])
                found = True
                return price
    sys.exit("Unable to find the coin !")

import requests

def get_historical_prices(asset_id, days=30):
    url = f"https://api.coincap.io/v2/assets/{asset_id}/history?interval=d1"
    # CoinCap returns data in descending order? Let's check docs.
    # We'll assume we get the latest first, so we'll slice the last 'days'.
    response = requests.get(url)
    data = response.json()['data']
    # Each entry has 'priceUsd' and 'time'
    prices = [float(entry['priceUsd']) for entry in data[-days:]]
    dates = [entry['time'] for entry in data[-days:]]
    # Convert timestamps to readable dates (optional)
    from datetime import datetime
    dates = [datetime.fromtimestamp(ts/1000).strftime('%Y-%m-%d') for ts in dates]
    return dates, prices
         

if __name__ == "__main__":
     main()