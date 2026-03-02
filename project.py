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

load_dotenv() #looks for the .env file

console = Console()

def main():
    # ASCII Art Header
    console.print(Panel.fit(
        "[bold cyan]🚀 CRYPTOPULSE TERMINAL[/bold cyan]\n[dim]Live Market Data Engine[/dim]",
        border_style="blue"
    ))

    coin_input = input("\nEnter coin name or symbol (e.g., bitcoin, BTC): ").lower().strip()
    
    if coin_input.isdigit():
         sys.exit("[bold red]Error:[/] Invalid Input")

    with console.status("[bold green]Fetching live data...") as status:
        url = "https://rest.coincap.io/v3/assets?apiKey=353debcd0dbc55a8a2f151d3c6984de7d5b0a7cadb17d42a054ebf7ed3f2038b"# Use v2 for better reliability
        try:
            response = requests.get(url)
            data = response.json()["data"]
        except Exception as e:
            sys.exit(f"[bold red]API Error:[/] {e}")

    coin_data = None
    for item in data:
        if coin_input == item["id"].lower() or coin_input == item["symbol"].lower():
            coin_data = item
            break
    
    if not coin_data:
        sys.exit("[bold red]Error:[/] Couldn't find the coin!")

    display_dashboard(coin_data)

def display_dashboard(coin):

    name = f"[bold yellow]{coin['name']} ({coin['symbol']})[/]"
    price = f"[bold green]${float(coin['priceUsd']):,.2f}[/]"
    
   
    change_val = float(coin['changePercent24Hr'])
    change_color = "[bold green]" if change_val > 0 else "[bold red]"
    change_str = f"{change_color}{change_val:+.2f}%[/]"

    # 2. Create the Statistics Table
    table = Table(title=f"Market Stats for {coin['name']}", title_style="bold magenta", border_style="bright_blue")
    
    table.add_column("Metric", style="cyan", no_wrap=True)
    table.add_column("Value", justify="right", style="white")

    table.add_row("Rank", f"#{coin['rank']}")
    table.add_row("Price", price)
    table.add_row("24h Change", change_str)
    table.add_row("Market Cap", f"${numerize.numerize(float(coin['marketCapUsd']))}")
    table.add_row("Volume (24h)", f"${numerize.numerize(float(coin['volumeUsd24Hr']))}")
    
    
    supply = numerize.numerize(float(coin['supply']))
    max_supply = numerize.numerize(float(coin['maxSupply'])) if coin['maxSupply'] else "N/A"
    table.add_row("Circulating Supply", f"{supply} / {max_supply}")

    
    console.print(table)
    console.print(Align.center(f"[dim]Data provided by CoinCap API • Last updated: Just now[/dim]"))

if __name__ == "__main__":
    main()