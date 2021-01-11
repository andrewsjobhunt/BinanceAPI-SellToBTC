import binance
import json

public = public_key_omitted
secret = secret_key_omitted

response = binance.get_coins(public, secret)

tmp = 0
file1 = open("file1.txt", "w+")
for i in response:
  for j in response[tmp]:
    print(tmp)
    print(j)
    print(response[tmp][j])
    file1.writelines(response[tmp][j])
    file1.writelines("\n")
  tmp += 1
file1.close()