import binance

public = public_key_omitted
secret = secret_key_omitted

# tmp = binance.check_apikey()
# apikey_public = tmp[0]
# apikey_secret = tmp[1]
# del tmp

# binance.validate_apikey(apikey_public, apikey_secret)


print("Validating API keys........")
try:
  tmp = binance.validate_apikey(public, secret)
  if tmp != True:
    print("\n...OK!\n")
  else:
    print("\nFAILED\n")
except:
  print("\nSomething went wrong... Try again\n")