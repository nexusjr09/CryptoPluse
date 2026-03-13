import requests 
import time
import os
import sys
from numerize import numerize
from tabulate import tabulate
from dotenv import find_dotenv,load_dotenv
from colorama import Fore, Style

dotenv_path = find_dotenv()
load_dotenv(dotenv_path)

def main():
     
     coin_input = input(Fore.GREEN+"Enter the coin: "+Style.RESET_ALL).lower().strip()
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

     print(Fore.RED+"\nFetching data....🔄"+Style.RESET_ALL)
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
     compare_coins(formatted)

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
     data = input(Fore.GREEN+"\nDo you want to see the Top 5 Coins currently in Market?(y/n): "+Style.RESET_ALL).lower()
     if data == "yes" or data == "y" or data == "yeh" or data == "sure":
          my_list=[]
          for item in formatted["data"]:
               if int(item["rank"])<=5:
                    my_list.append([
    int(item["rank"]), #not a string so not using f" "
    item["symbol"],
    f"${round(float(item['priceUsd']),2)}",
    f"{round(float(item['changePercent24Hr']),2)}%"
])
          my_list.sort()
          headers = ["RANK","SYMBOL","PRICE IN USD","CHANGE IN %"]
          stats_table = tabulate(my_list,headers=headers,tablefmt="fancy_grid")
          print(stats_table)  
     else:
          print("Skipping Top 5 coins! ")
          

def compare_coins(formatted):
     data = input(Fore.GREEN+"\nDo you want to compare any two coins? (y/n)"+Style.RESET_ALL).strip().lower()
     my_list = []
     if data == "y" or data == "yes":
          coin1 = input(Fore.RED+"\nEnter coin1: "+Style.RESET_ALL).lower().strip()
          for item in formatted["data"]:
               if coin1 == item["name"].lower() or coin1 == item["symbol"].lower():
                    my_list.append([int(item["rank"]),item["name"],f"${round(float(item['priceUsd']),2)}",f"{round(float(item['changePercent24Hr']),2)}%"])
                    break #when thsi break is added it now automatically skips else function. 
          else:
               sys.exit("Invalid coin 1🛑")

          coin2 = input(Fore.RED+"Enter coin2: "+Style.RESET_ALL).lower().strip()
          for item in formatted["data"]:
               if coin2 == item["name"].lower() or coin2 == item["symbol"].lower():
                    my_list.append([int(item["rank"]),item["name"],f"${round(float(item['priceUsd']),2)}",f"{round(float(item['changePercent24Hr']),2)}%"])
                    break #if break was not there it wouldn't skip else function.
          else:
               sys.exit("Invalid Coin 2🛑")

          headers = ["RANK","NAME","PRICE IN USD","CHANGE PERCENT (24hr)"]
          stats_table = tabulate(my_list,headers=headers,tablefmt="fancy_grid")
          print(f"\n{stats_table}")
     sys.exit()



if __name__ == "__main__":
     main()

##