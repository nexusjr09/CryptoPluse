import requests
import sys
from numerize import numerize

def main():
    coin_input = input("Enter coin name or symbol (e.g., bitcoin, BTC): ").lower().strip()
    if coin_input.isdigit():
         sys.exit("Invalid Input")
    url = "https://rest.coincap.io/v3/assets?apiKey=353debcd0dbc55a8a2f151d3c6984de7d5b0a7cadb17d42a054ebf7ed3f2038b"
    response = requests.get(url)
    data = response.json()
    print(f"{coin_input.upper()}: #{rank(coin_input,data)}")
    print(f"Price: ${coin_price(coin_input,data)}")
    print(f"24h change:",change_within_24hr(data))
    print(f"Market Cap: ${marketcap(data)}")
    print(f"Volume (24h): ${volume(data)}")


def coin_price(input,data):

    for item in data["data"]:
        if input == item["id"].lower() or input == item["symbol"].lower():
            price = float(item["priceUsd"])
            return price
    
    sys.exit("Coudn't find the coin !")

def rank(input,data):
    for item in data["data"]:
        rank = item["rank"]
        return rank


def change_within_24hr(data):
    for item in data["data"]: 
        change = float(item["changePercent24Hr"])
        change = round(change,3)
        return change 

def marketcap(data):
    for item in data["data"]:
        cap = float(item["marketCapUsd"])
        formatted = numerize.numerize(cap)
        return formatted

def volume(data):
    for item in data["data"]:
        vol =  float(item["volumeUsd24Hr"])
        formattedvol = numerize.numerize(vol)
        return formattedvol

def circulatingsupply(data):
    ...

if __name__ == "__main__":
    main()