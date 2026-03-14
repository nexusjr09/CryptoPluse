# CryptoPluse - Crypto Coin Tracker
#### Video Demo: https://youtu.be/D_i6wXY5PVI?si=DFcLCnrDPK6Q50E3
#### Description:

CryptoPluse is a Python-based command-line tool that fetches live cryptocurrency data directly from the CoinCap API. The program allows you to look up any cryptocurrency by name or symbol, view detailed statistics, see the current top 5 coins in the market, and compare any two coins side by side — all displayed in a clean, colorful terminal interface using formatted tables.

The idea behind this project was to build something practical and real-world that goes beyond simple scripts. Instead of working with static data, CryptoPluse connects to a live API on every run, meaning the data you see is always current. This makes it genuinely useful for anyone who wants quick crypto information without opening a browser.

---

## Files

### `project.py`
This is the main file of the project and contains all the core logic. It includes the `main` function as well as all helper functions. Here is what each function does:

- **`main()`** — The entry point of the program. It takes the coin input from the user, calls the CoinCap API, fetches the data, and then calls the other functions in sequence to display coin stats, top 5 coins, and the comparison feature.

- **`find_coin(coin_input, formatted)`** — Searches through the API response data to find the coin the user entered. It matches against both the coin's full name (e.g. `bitcoin`) and its symbol (e.g. `btc`), making the search case-insensitive. If no match is found, the program exits with a clear error message.

- **`rank_coin(dict_data)`** — Returns the market rank of the coin from the coin's data dictionary.

- **`coin_price(dict_data)`** — Extracts the coin's current price in USD from the data and rounds it to 2 decimal places.

- **`supply(dict_data)`** — Returns the circulating supply of the coin. If the API returns `None` for supply (which some coins do), it returns the string `"None"` instead of crashing. Otherwise it formats the number using `numerize` for readability (e.g. `19.6M`).

- **`maxsupply(dict_data)`** — Same as `supply` but for the maximum supply of the coin. Many coins like Bitcoin have a hard cap while others like Ethereum do not, so `None` handling is important here.

- **`volume_usd(dict_data)`** — Returns the 24-hour trading volume of the coin in USD, formatted using `numerize` for readability (e.g. `35.2B`).

- **`change_percent(dict_data)`** — Returns the percentage change in price over the last 24 hours, rounded to 3 decimal places. This can be negative if the coin's price dropped.

- **`top5_coins(formatted)`** — Asks the user if they want to see the top 5 coins in the market. If yes, it filters the API data for coins ranked 1 through 5, sorts them by rank, and displays them in a formatted table.

- **`compare_coins(formatted)`** — Asks the user if they want to compare two coins. If yes, it takes two coin inputs, searches for each one in the API data, and displays both side by side in a table. It uses Python's `for/else` syntax to handle invalid coin names gracefully.

### `test_project.py`
This file contains all the pytest unit tests for the project. Since the helper functions rely on a coin data dictionary, the tests use a `fake_coin()` function that returns a mock dictionary mimicking the real API response. This means the tests run without needing an internet connection or a real API key. Tests cover `rank_coin`, `coin_price`, `supply`, `maxsupply`, `volume_usd`, and `change_percent`, including edge cases like `None` supply values and negative price changes.

### `requirements.txt`
Lists all the pip-installable libraries the project depends on: `requests`, `numerize`, `tabulate`, `python-dotenv`, and `colorama`.

### `.env`
Stores the CoinCap API key locally. This file is not committed to version control to keep the API key private.

---

## Design Choices

One of the key design decisions was how to handle invalid coin inputs in the comparison feature. Initially the code used a simple `sys.exit()` after the loop which caused the program to always exit regardless of whether the coin was found or not. After working through the logic, the final solution uses Python's `for/else` syntax — the `else` block only runs if the loop completes without hitting a `break`, which means the coin was never found. This is a cleaner and more Pythonic approach than checking the length of a list afterward.

Another choice was to keep all functions flat at the top level of `project.py` rather than grouping them into a class. Since the project is a straightforward CLI tool with a linear flow, a class would have added unnecessary complexity without any real benefit.

For number formatting, `numerize` was chosen over manual formatting because it handles edge cases like very large or very small numbers cleanly and produces readable output like `19.6M` or `35.2B` without extra code.

---

## Setup

1. Clone the repository and navigate into the folder
2. Install dependencies:
```bash
pip install -r requirements.txt
```
3. Create a `.env` file and add your CoinCap API key:
```
COINCAP_API_KEY=your_api_key_here
```
4. Run the program:
```bash
python project.py
```

---

## Example Output

```
Enter the coin: bitcoin

Fetching data....🔄

╒═══════════════════════╤══════════════╕
│ Rank                  │ 1            │
│ Price                 │ $102345.68   │
│ Circulating Supply    │ 19.6M        │
│ Max Supply            │ 21.0M        │
│ Volume (USD)          │ 35.2B        │
│ 24h Change            │ 2.346%       │
╘═══════════════════════╧══════════════╛

If the user wants he/she can also she the top 5 coins currently in the market and can also compare two desired Coins.
```