import requests
import json
import time

def get_crypto_data():
    url = 'https://api.coingecko.com/api/v3/coins/markets'
    params = {
        'vs_currency': 'usd',
        'order': 'market_cap_desc',
        'per_page': 10,
        'page': 1,
        'sparkline': False,
        'price_change_percentage': '1h,24h,7d'
    }
    response = requests.get(url, params=params)
    data = response.json()
    return data

def print_crypto_data(data):
    print("Cryptocurrency Market Data:")
    print("Name\tPrice\t1h\t24h\t7d")
    for coin in data:
        name = coin['name']
        price = coin['current_price']
        price_change_percentage_1h = coin['price_change_percentage_1h_in_currency']
        price_change_percentage_24h = coin['price_change_percentage_24h_in_currency']
        price_change_percentage_7d = coin['price_change_percentage_7d_in_currency']
        print(f"{name}\t{price:.2f}\t{price_change_percentage_1h:.2f}%\t{price_change_percentage_24h:.2f}%\t{price_change_percentage_7d:.2f}%")

if __name__ == "__main__":
    while True:
        data = get_crypto_data()
        print_crypto_data(data)
        time.sleep(60)
