import requests

binance_base_endpoint = "https://api.binance.com"
market_data_endpoint = f"{binance_base_endpoint}/api/v3/ticker/24hr"

def get_bid_price(coin):
    crypto_data = {"symbol": coin}
    response = requests.get(url=market_data_endpoint, params=crypto_data)
    return response




