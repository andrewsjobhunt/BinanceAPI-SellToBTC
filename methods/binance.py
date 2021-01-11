import json
import time
import hmac
import hashlib
import requests
import math
from pathlib import Path

def _url(path):
  return 'https://api.binance.com' + path

def _path():
  return(Path(__file__).parent)

def truncate(number, digits) -> float:
    stepper = 10.0 ** digits
    return math.trunc(stepper * number) / stepper

# Simple request with no apikey
def check_status():
  response = requests.get(_url('/wapi/v3/systemStatus.html'))
  response_dict = json.loads(response.text)
  return response_dict['status']

# File checking to see if apikey exists
def check_apikey():
  try:
    txt = open(_path() / '../keys.txt', "r")
  except:
    return 1
  tmp = txt.read().splitlines()
  txt.close()
  return tmp
  
# We have to integrate apikey info, validate by making req w/ apikey
def validate_apikey(apikey_public, apikey_secret):
  time_now = str(int(time.time() * 1000))
  signature_builder = 'timestamp=' + time_now + '&recvWindow=8000'

# We have to convert all str into bytes for HMAC hash
  apikey_secret_h = apikey_secret.encode()
  signature_builder_h = signature_builder.encode()

  h = hmac.new(apikey_secret_h, signature_builder_h, hashlib.sha256)

  response = requests.get(_url('/wapi/v3/apiTradingStatus.html'), 
  params={'timestamp': time_now, 
          'recvWindow': '8000',
          'signature': h.hexdigest()
          },
  headers={'X-MBX-APIKEY': apikey_public},)

  if response.ok:
    return json.loads(response.text)
  else:
    return 0


def get_binance_info():
  response = requests.get('https://www.binance.com/api/v1/exchangeInfo')
  return json.loads(response.text)


# Return entire json object - can filter here later
def get_coins(apikey_public, apikey_secret):
  time_now = str(int(time.time() * 1000))
  signature_builder = 'timestamp=' + time_now + '&recvWindow=8000'

  apikey_secret_h = apikey_secret.encode()
  signature_builder_h = signature_builder.encode()

  h = hmac.new(apikey_secret_h, signature_builder_h, hashlib.sha256)

  response = requests.get(_url('/sapi/v1/capital/config/getall'),
  params={'timestamp': time_now, 
          'recvWindow': '8000',
          'signature': h.hexdigest()
          },
  headers={'X-MBX-APIKEY': apikey_public},)

  if response.ok:
    return json.loads(response.text)
  else:
    return 0

# Simple price request with no apikey
def coin_price(coin_ticker):
  response = requests.get(_url('/api/v3/avgPrice'),
  params={'symbol': coin_ticker})

  return json.loads(response.text)


# TRADE RELATED METHODS START HERE

def check_fees(apikey_public, apikey_secret):
  time_now = str(int(time.time() * 1000))
  signature_builder = 'timestamp=' + time_now + '&recvWindow=8000'

  apikey_secret_h = apikey_secret.encode()
  signature_builder_h = signature_builder.encode()

  h = hmac.new(apikey_secret_h, signature_builder_h, hashlib.sha256)

  response = requests.get(_url('/wapi/v3/tradeFee.html'),
  params={'timestamp': time_now, 
          'recvWindow': '8000',
          'signature': h.hexdigest()
          },
  headers={'X-MBX-APIKEY': apikey_public},)

  return json.loads(response.text)


def trade_sell(coin_ticker, quantity, apikey_public, apikey_secret):
  time_now = str(int(time.time() * 1000))
  coin_ticker = coin_ticker + 'BTC'

  signature_builder = 'timestamp=' + time_now + '&recvWindow=8000' + '&symbol=' + coin_ticker + '&side=SELL' + '&type=MARKET' + '&quantity=' + str(quantity)

  apikey_secret_h = apikey_secret.encode()
  signature_builder_h = signature_builder.encode()

  h = hmac.new(apikey_secret_h, signature_builder_h, hashlib.sha256)

  response = requests.post(_url('/api/v3/order'),
  params={'timestamp': time_now,
          'recvWindow': '8000',
          'symbol': coin_ticker,
          'side': 'SELL',
          'type': 'MARKET',
          'quantity': quantity,
          'signature': h.hexdigest()},
  headers={'X-MBX-APIKEY': apikey_public},)

  if(response.ok):
    return json.loads(response.text)
  else:
    print(json.loads(response.text))
    return 0

def trade_buy(coin_ticker, quoteOrderQty, apikey_public, apikey_secret):
  time_now = str(int(time.time() * 1000))
  coin_ticker = coin_ticker + 'BTC'

  signature_builder = 'timestamp=' + time_now + '&recvWindow=8000' + '&symbol=' + coin_ticker + '&side=BUY' + '&type=MARKET' + '&quoteOrderQty=' + str(quoteOrderQty)

  apikey_secret_h = apikey_secret.encode()
  signature_builder_h = signature_builder.encode()

  h = hmac.new(apikey_secret_h, signature_builder_h, hashlib.sha256)

  response = requests.post(_url('/api/v3/order'),
  params={'timestamp': time_now,
          'recvWindow': '8000',
          'symbol': coin_ticker,
          'side': 'BUY',
          'type': 'MARKET',
          'quoteOrderQty': quoteOrderQty,
          'signature': h.hexdigest()},
  headers={'X-MBX-APIKEY': apikey_public},)

  if(response.ok):
    return json.loads(response.text)
  else:
    print(json.loads(response.text))
    return 0