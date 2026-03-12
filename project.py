import requests 
import os
import sys
from numerize import numerize
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
     print(f"Circulating Supply: {supply(dict_data)}")
     print(f"Max Supply: {maxsupply(dict_data)}")
     print(f"Volume USD: {volume_usd(dict_data)}")
     print(f"Change percent: {change_percent(dict_data)}%")
     print("<------------------------------->")


def find_coin(coin_input,formatted):
     for item in formatted["data"]:
          if coin_input== item["symbol"].lower() or coin_input == item["name"].lower():
               return item
     sys.exit("Invalid Coin! ")


def rank_coin(dict_data):
     return dict_data["rank"]

def coin_price(dict_data):
     return round(float(dict_data["priceUsd"]),2)

def supply(dict_data):
     return numerize.numerize(float(dict_data["supply"]))

def maxsupply(dict_data):
     return numerize.numerize(float(dict_data["maxSupply"]))

def volume_usd(dict_data):
     return numerize.numerize(float(dict_data["volumeUsd24Hr"]))

def change_percent(dict_data):
     return round(float(dict_data["changePercent24Hr"]),3)



if __name__ == "__main__":
     main()