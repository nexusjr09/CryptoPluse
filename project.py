import requests 
import os
import sys
from dotenv import find_dotenv,load_dotenv

dotenv_path = find_dotenv()
load_dotenv(dotenv_path)

def main():
     coin_input = input("Enter the coin: ").lower()
     api_key = os.getenv("COINCAP_API_KEY")
     url =  f"https://rest.coincap.io/v3/assets?apiKey={api_key}"
     data = requests.get(url)
     formatted = data.json()
     dict_data = find_coin(coin_input,formatted)

     print("<-------------------------->")
     print(f"Rank: {rank_coin(dict_data)}")
     print(f"Price: ${coin_price(dict_data)}")

def find_coin(coin_input,formatted):
     for item in formatted["data"]:
          if coin_input== item["symbol"].lower() or coin_input == item["name"].lower():
               return item
     sys.exit("Invalid Coin! ")


def rank_coin(dict_data):
     return dict_data["rank"]

def coin_price(dict_data):
     return round(float(dict_data["priceUsd"]),2)


if __name__ == "__main__":
     main()