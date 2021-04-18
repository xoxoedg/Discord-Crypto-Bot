import requests
from bot_auth_token import COIN_MARKET_AUTH_TOKEN


binance_base_endpoint = "https://api.binance.com"
market_data_endpoint = f"{binance_base_endpoint}/api/v3/ticker/24hr"

market_coin_market_data_endpoint = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest"


def get_bid_price(coin):
    """API Request to Binance API"""
    crypto_data = {"symbol": coin}
    response = requests.get(url=market_data_endpoint, params=crypto_data)
    return response

#def get_bid_price_coin_market():
#    """API Request to Coin Markt API"""
#    parameters = {"symbol": "HAPIUSD"}
#    coin_market_headers = {
#                           "X-CMC_PRO_API_KEY": COIN_MARKET_AUTH_TOKEN,
#                           }
#    response = requests.get(url=market_data_endpoint,params=parameters, headers=coin_market_headers)
#    return response



