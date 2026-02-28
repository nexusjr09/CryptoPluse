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

def get_historical_prices(asset_id, days=30):
    url = f"https://rest.coincap.io/v3/assets/{asset_id}/history?interval=d1&limit={days}&apiKey=353debcd0dbc55a8a2f151d3c6984de7d5b0a7cadb17d42a054ebf7ed3f2038b"

    response = requests.get(url)
    data = response.json()

    prices = []
    dates = []

    for item in data["data"]:
         ...
         

if __name__ == "__main__":
     main()