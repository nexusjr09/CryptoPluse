import sys
import requests

coin = input("Enter the coin: ")
url = "https://rest.coincap.io/v3/assets?apiKey=353debcd0dbc55a8a2f151d3c6984de7d5b0a7cadb17d42a054ebf7ed3f2038b"
data = requests.get(url)
formatted = data.json()

for item in formatted["data"]:
    if coin == item["symbol"] or coin == item["name"]:
        print(item["priceUsd"])
 