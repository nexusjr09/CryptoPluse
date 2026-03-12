import requests 
import time
import os
import sys
from numerize import numerize
from dotenv import find_dotenv,load_dotenv

dotenv_path = find_dotenv()
load_dotenv(dotenv_path)

def main():
     
     coin_input = input("Enter the coin: ").lower().strip()
     api_key = os.getenv("COINCAP_API_KEY")
     url =  f"https://rest.coincap.io/v3/assets?apiKey={api_key}"
     try:
          data = requests.get(url)
     except requests.exceptions.ConnectionError:
          print("❌ Unable to connect to API")
     except requests.exceptions.Timeout:
          print("❌ API request timed out")
     except ValueError:
          print("❌ Invalid JSON response")

     formatted = data.json()
     dict_data = find_coin(coin_input,formatted)

     print("Fetching data....🔄")
     time.sleep(2)
     print("----------------------------")
     type_text(f"Rank: {rank_coin(dict_data)}",0.03)
     type_text(f"Price: ${coin_price(dict_data)}",0.03)
     type_text(f"Circulating Supply: {supply(dict_data)}",0.03)
     type_text(f"Max Supply: {maxsupply(dict_data)}",0.03)
     type_text(f"Volume USD: {volume_usd(dict_data)}",0.03)
     type_text(f"24Hr Change percent: {change_percent(dict_data)}%",0.03)
     print("-------------------------------")
     top5_coins(formatted)

def find_coin(coin_input,formatted):
     for item in formatted["data"]:
          if coin_input== item["symbol"].lower() or coin_input == item["name"].lower():
               return item
     sys.exit(f"🔴 Unable to find the COIN called >> {coin_input}")


def type_text(text,speed=0.03):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.03)
    print()

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

def top5_coins(formatted):
     data = input("Do you want to see the Top 5 Coins?(y/n): ").lower()
     if data == "yes" or data == "y" or data == "yeh" or data == "sure":
          for item in formatted["data"]:
               if int(item["rank"])<=5:
                    print(f"{item["rank"]}| {item["symbol"]} | ${round(float(item["priceUsd"]))} | {round(float(item["changePercent24Hr"]),3)}% ")
          sys.exit()
     sys.exit("Okay !!")




if __name__ == "__main__":
     main()