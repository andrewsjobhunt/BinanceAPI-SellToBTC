import binance
import json

public = public_key_omitted
secret = secret_key_omitted

response = binance.get_coins(public, secret)

tmp = 0
file1 = open("file1.txt", "w+")
for i in response:
  # print(response[tmp])
  if(response[tmp]['free'] != '0' or 
    response[tmp]['freeze'] != '0' or 
    response[tmp]['locked'] != '0'):
    print('Coin: ' + response[tmp]['coin'])
    print('Free: ' + response[tmp]['free'])
    print('Freeze: ' + response[tmp]['freeze'])
    print('Locked: ' + response[tmp]['locked'])
    print("\n")
    file1.writelines("Coin: ")
    file1.writelines(response[tmp]['coin'])
    file1.writelines("\nFree: ")
    file1.writelines(response[tmp]['free'])
    file1.writelines("\nFreeze: ")
    file1.writelines(response[tmp]['freeze'])
    file1.writelines("\nLocked: ")
    file1.writelines(response[tmp]['locked'])
    file1.writelines("\n\n")
  tmp += 1
file1.close()