import binance
import json

public = public_key_omitted
secret = secret_key_omitted

print("\nPreloading coins and values, this may take some time........")
binance_info_dict = binance.get_binance_info()['symbols']

def search(symbol):
    for i in binance_info_dict:
        if(i['symbol'] == symbol):
            return i
# tmp = 0
# for i in binance_info_dict:
#     if(binance_info_dict[tmp]['symbol'] == 'ETHBTC'):
#         print(binance_info_dict[tmp])
#     tmp += 1
result = search('ETHBTC')

print(result['filters'][2]['stepSize'])

# WHAT ARE WE DOING

# WE ARE GETTING RESULT WHICH HAS A DICT OF STUFF

# NEED KEY = FILTERS

# FILTERS IS A LIST OF DICTS again


# print(result)


# ethbtc = next((item for item in binance_info_dict if item['symbol'] == "ETHBTC"), None)



# ethbtc = filter(lambda coin: coin['symbol'] == 'ETHBTC', binance_info_dict)
# print(ethbtc)

# print(binance_info_dict[ethbtc])

# I AM STUMPED

# STEP SIZE IS KILLING MY TRADES

# THE ONLY WAY TO RETRIEVE STEP SIZE IS FROM EXCHANGEINFO
# WHICH IS JSON DICT OF A LOT OF SHIT

# SO ???

# FILTER? OR SOMETHING ELSE.........

# TBC



# binance_info_dict['symbols'][response[tmp]['coin'] + 'BTC']


# We want to filter through the coins that we have
# Then remove any 0 balances
# Add non-tradeable assets to new dict, remove from old dict




