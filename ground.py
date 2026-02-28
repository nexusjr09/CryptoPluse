import requests
import sys
def main():
    coin_input = input("Enter coin name or symbol (e.g., bitcoin, BTC): ").lower()
    if coin_input.isdigit():
         sys.exit("Invalid Input")
    print(coin_price(coin_input))

def coin_price(input):
    
    url = "https://rest.coincap.io/v3/assets?apiKey=353debcd0dbc55a8a2f151d3c6984de7d5b0a7cadb17d42a054ebf7ed3f2038b"
    response = requests.get(url)
    data = response.json()
    return data

if __name__ == "__main__":
    main()