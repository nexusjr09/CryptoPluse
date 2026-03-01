import requests
import sys
def main():
    coin_input = input("Enter coin name or symbol (e.g., bitcoin, BTC): ").lower()
    if coin_input.isdigit():
         sys.exit("Invalid Input")
    url = "https://rest.coincap.io/v3/assets?apiKey=353debcd0dbc55a8a2f151d3c6984de7d5b0a7cadb17d42a054ebf7ed3f2038b"
    response = requests.get(url)
    data = response.json()
    print(f"The current price of {coin_input.upper()} is $",coin_price(coin_input,data))
    print(f"24-Hour Change of {coin_input.upper()} :",change_within_24hr(coin_input,data))


def coin_price(input,data):
    
    found = False
    for item in data["data"]:
        if input == item["id"].lower or input == item["symbol"].lower():
            found = True
            price = float(item["priceUsd"])
            return price
            return found
        if not found:
            sys.exit("Coin not found !!")

def change_within_24hr(input,data):
    ...
    
        
if __name__ == "__main__":
    main()