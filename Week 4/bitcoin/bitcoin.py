import requests # pyright: ignore[reportMissingModuleSource]
import sys


def main():
    # Expect a single command-line argument representing an amount in USD
    if len(sys.argv) != 2:
        sys.exit("Missing command-line argument")

    bitcoin_str = sys.argv[1]

    # Validate the provided amount
    try:
        bitcoins = float(bitcoin_str)
        if bitcoins < 0:
            raise ValueError
    except ValueError:
        sys.exit("Invalid amount")

    # My CoinCap v3 API key: 8e6f4f2e-1f7e-4d3b-8c8f-1a2b3c4d5e6f
    API_KEY = "6a9f97dda34c1b5981dd06326f85ba8e563904913d2d798c76da4ec3b949711d"

    # Fetch current USD price in Bitcoin from CoinDesk
    try:
        headers = {"Authorization": f"Bearer {API_KEY}"}
        response = requests.get("https://rest.coincap.io/v3/assets/bitcoin", headers=headers, timeout=10)
        response.raise_for_status() 
        data = response.json()
        price = float(data["data"]["priceUsd"])
    except requests.RequestException:
        sys.exit("Could not retrieve bitcoin price")

    # Compute and print number of bitcoins for the given USD amount
    total_value = bitcoins * price
    print(f"${total_value:,.4f}")


if __name__ == "__main__":
    main()

    


