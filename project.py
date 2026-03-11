import requests 
import os
from dotenv import find_dotenv,load_dotenv

dotenv_path = find_dotenv()
load_dotenv(dotenv_path)
def main():
     coin = input("Enter the coin: ")
     api_key = os.getenv("API_KEY")
     url =  "https://rest.coincap.io/v3/assets?apiKey={api_key}"
     data = requests.get(url)
     print(data)


if __name__ == "__main__":
     main()