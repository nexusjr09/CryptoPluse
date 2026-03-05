import requests
import os
import sys
from numerize import numerize
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.align import Align
from rich import print as rprint
from dotenv import load_dotenv

load_dotenv()
console = Console()


def main():
    console.print(Panel.fit(
        "[bold cyan]🚀 CRYPTOPULSE TERMINAL[/bold cyan]\n[dim]Live Market Data Engine[/dim]",
        border_style="blue"
    ))

    coin_input = get_user_input()
    if coin_input is None:
        sys.exit("[bold red]Error:[/] Invalid Input")

    api_key = os.getenv("COINCAP_API_KEY")
    if not api_key:
        sys.exit("[bold red]Error:[/] API key not found. Set COINCAP_API_KEY in .env file.")

    coin_data = fetch_coin_data(coin_input, api_key)
    if coin_data is None:
        sys.exit("[bold red]Error:[/] Couldn't find the coin!")

    display_dashboard(coin_data)


def get_user_input():
    """Prompt user for coin name/symbol and validate."""
    coin_input = input("\nEnter coin name or symbol (e.g., bitcoin, BTC): ").lower().strip()
    if not coin_input or coin_input.isdigit():
        return None
    return coin_input


def fetch_coin_data(coin_input, api_key):
    """Fetch all assets from CoinCap API and search for the given coin."""
    url = f"https://rest.coincap.io/v3/assets?apiKey={api_key}"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()["data"]
    except Exception as e:
        print(f"[bold red]API Error:[/] {e}")
        return None

    for item in data:
        if coin_input == item["id"].lower() or coin_input == item["symbol"].lower():
            return item
    return None


def format_coin_data(coin):
    """Format coin data for display (returns a dict with formatted strings)."""
    price = f"${float(coin['priceUsd']):,.2f}"
    change_val = float(coin['changePercent24Hr'])
    change_color = "[bold green]" if change_val > 0 else "[bold red]"
    change_str = f"{change_color}{change_val:+.2f}%[/]"
    market_cap = f"${numerize.numerize(float(coin['marketCapUsd']))}"
    volume = f"${numerize.numerize(float(coin['volumeUsd24Hr']))}"
    supply = numerize.numerize(float(coin['supply']))
    max_supply = numerize.numerize(float(coin['maxSupply'])) if coin['maxSupply'] else "N/A"
    supply_str = f"{supply} / {max_supply}"

    return {
        "name": f"[bold yellow]{coin['name']} ({coin['symbol']})[/]",
        "rank": f"#{coin['rank']}",
        "price": price,
        "change": change_str,
        "market_cap": market_cap,
        "volume": volume,
        "supply": supply_str
    }


def display_dashboard(coin):
    """Render a Rich table with coin statistics."""
    formatted = format_coin_data(coin)

    table = Table(title=f"Market Stats for {coin['name']}", title_style="bold magenta", border_style="bright_blue")
    table.add_column("Metric", style="cyan", no_wrap=True)
    table.add_column("Value", justify="right", style="white")

    table.add_row("Rank", formatted["rank"])
    table.add_row("Price", formatted["price"])
    table.add_row("24h Change", formatted["change"])
    table.add_row("Market Cap", formatted["market_cap"])
    table.add_row("Volume (24h)", formatted["volume"])
    table.add_row("Circulating Supply", formatted["supply"])

    console.print(table)
    console.print(Align.center(f"[dim]Data provided by CoinCap API • Last updated: Just now[/dim]"))


if __name__ == "__main__":
    main()