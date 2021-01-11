import json
import requests

def _url(path):
  return 'https://api.binance.com' + path

response = requests.get(_url('/wapi/v3/systemStatus.html'))

response_dict = json.loads(response.text)

print(response_dict['status'])

# return response_dict['status']

# for i in response_dict:
# 	print(i, response_dict[i])

# print(response.__dict__)
