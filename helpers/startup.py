import methods.binance as binance
import requests
import io

###### Simply checks if Binance API server is responding correctly ######
def start():
  print("\n\nInitializing........\n")
  print("\nContacting Binance API Servers........")
  if(binance.check_status() == 0):
    print("\n...OK!")
  else:
    print("\nFAILED")
    print("Exiting application........\n")
    quit()

###### Simply checks if API Keys are stored locally in .txt file #######
def apikey_file_check():
  print("\nChecking for API keys........")
  try:
    tmp = binance.check_apikey()
    print("\n...OK!")
    return tmp
  except:
    print("\nFAILED")
    print("Exiting application........\n")
    quit()

###### Sends GET request to user-authenticated "Trading Status" API Endpoint, thereby validating API Keys ######
def apikey_validation(apikey_public, apikey_secret):
  print("\nValidating API keys........")
  try:
    tmp = binance.validate_apikey(apikey_public, apikey_secret)
    if tmp != 0:
      print("\n...OK!\n")
    else:
      print("\nFAILED")
      print("Exiting application........\n")
      del tmp
      quit()
    del tmp
  except:
    print("\nSomething went wrong... Try again")
    print("Exiting application........\n")
    quit()