import binance

response = binance.coin_price('XRPUSDT')
print(response['price'])