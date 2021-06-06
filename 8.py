import requests

headers = {
    'Content-Type': 'application/json',
}

data = {
  '{"api_key":"{hCnMaQ0LC0BnzEB2I6}","side"': '"Buy","symbol"="BTCUSD","order_type":"Market","qty":10,"time_in_force":"GoodTillCancel","timestamp":{1622796853},"sign":"{a9c0164fbbb6d019971ac24dcdab352533158a30608551d380f2ed8a1895b056221fd9482ab1b16d6779a98a9496e1ec807dde48ad6be3f482bf5c36168a832d}"}'
}

response = requests.post('https://api.bybit.com/v2/private/order/create', headers=headers, data=data)
