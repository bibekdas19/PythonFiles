import requests

params = (
    ('symbol', 'BTCUSD'),
)

response = requests.get('https://api.bybit.com/v2/public/orderBook/L2', params=params)
r=response.json()
print("The asset price is +"r['result'][0]['price'])
