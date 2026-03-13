import requests 
import time
import os
import sys
from numerize import numerize
from tabulate import tabulate
from dotenv import find_dotenv,load_dotenv

dotenv_path = find_dotenv()
load_dotenv(dotenv_path)

def main():
     
     coin_input = input("Enter the coin: ").lower().strip()
     api_key = os.getenv("COINCAP_API_KEY")
     url =  f"https://rest.coincap.io/v3/assets?apiKey={api_key}"
     try:
          data = requests.get(url)
          formatted = data.json()

     except requests.exceptions.ConnectionError:
          sys.exit("❌ Unable to connect to API")
     except requests.exceptions.Timeout:
          sys.exit("❌ API request timed out")
     except ValueError:
          sys.exit("❌ Invalid JSON response")

     
     dict_data = find_coin(coin_input,formatted)

     print("\nFetching data....🔄")
     time.sleep(2)
     coin_stats = [
    ["Rank", rank_coin(dict_data)],
    ["Price", f"${coin_price(dict_data)}"],
    ["Circulating Supply", supply(dict_data)],
    ["Max Supply", maxsupply(dict_data)],
    ["Volume (USD)", volume_usd(dict_data)],
    ["24h Change", f"{change_percent(dict_data)}%"]
    ]
     stats_table = tabulate(coin_stats, tablefmt="fancy_grid")
     print(stats_table)
     top5_coins(formatted)

def find_coin(coin_input,formatted):
     for item in formatted["data"]:
          if coin_input== item["symbol"].lower() or coin_input == item["name"].lower():
               return item
     sys.exit(f"🔴 Unable to find the COIN called >> {coin_input}")



def rank_coin(dict_data):
     return dict_data["rank"]

def coin_price(dict_data):
     return round(float(dict_data["priceUsd"]),2)

def supply(dict_data):
     if dict_data["supply"] == None:
          return "None"
     else:
          return numerize.numerize(float(dict_data["supply"]))

def maxsupply(dict_data):
     if dict_data["maxSupply"] == None:
          return "None"
     else: 
          return numerize.numerize(float(dict_data["maxSupply"]))

def volume_usd(dict_data):
     return numerize.numerize(float(dict_data["volumeUsd24Hr"]))

def change_percent(dict_data):
     return round(float(dict_data["changePercent24Hr"]),3)

def top5_coins(formatted):
     data = input("\nDo you want to see the Top 5 Coins currently in Market?(y/n): ").lower()
     if data == "yes" or data == "y" or data == "yeh" or data == "sure":
          my_list=[]
          for item in formatted["data"]:
               if int(item["rank"])<=5:
                    my_list.append([
    int(item["rank"]), #not a string so not using f" "
    f"{item["symbol"]}",
    f"${round(float(item["priceUsd"]),2)}",
    f"{round(float(item["changePercent24Hr"]),2)}%"
])
          my_list.sort()
          headers = ["RANK","SYMBOL","PRICE IN USD","CHANGE IN %"]
          stats_table = tabulate(my_list,headers=headers,tablefmt="fancy_grid")
          print(stats_table)  
          sys.exit()

     sys.exit("As you Say! ")

def compare_coins():
     ...

if __name__ == "__main__":
     main()