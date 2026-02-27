import requests
import sys

def main():
    coin_input = input("Enter coin name or symbol (e.g., bitcoin, BTC): ").lower()
    if coin_input.isdigit():
         sys.exit("Invalid Input")
    coin_price(coin_input)
    

def coin_price(input):
    found = False
    url = "https://rest.coincap.io/v3/assets?apiKey=353debcd0dbc55a8a2f151d3c6984de7d5b0a7cadb17d42a054ebf7ed3f2038b"
    response = requests.get(url)
    data = response.json()
    for coin in data["data"]:
         if input == coin["id"].lower() or input == coin["symbol"].lower():
                price = float(coin["priceUsd"])
                found = True
                return price
         elif not found:
              sys.exit("Unable to find the coin !")
   
if __name__ =="__main__":
    main()


