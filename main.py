import sys
import requests
import methods.binance as binance
import helpers.startup as startup
import helpers.menu as menu
import math
import io

def main():

  startup.start()
  tmp = startup.apikey_file_check() # Checking and loading in ApiKeys
  apikey_public = tmp[0]
  apikey_secret = tmp[1]
  pct_dict = {}
  del tmp
  startup.apikey_validation(apikey_public, apikey_secret)
  
  while(True):
    menu_choice = menu.print_menu()
    if(menu_choice == 1):
      menu.get_balance(apikey_public, apikey_secret)
    elif(menu_choice == 2):
      pct_dict = menu.sell_balance(apikey_public, apikey_secret)
      for i in pct_dict:
        print("\n" + i + " ")
        if i == "btc_total":
          print("" + str(pct_dict[i] * 100))
        else:
          print("" + str(pct_dict[i] * 100) + " percent")
      try:
        with open("portfolio_split.txt", "a") as writer:
          for j in pct_dict:
            writer.write(j)
            writer.write('\n')
            writer.write(str(pct_dict[j]))
            writer.write('\n')
      except:
        print("\n\n### Error")
 
    elif(menu_choice == 3):
      if(not pct_dict):
        try:
          with open("portfolio_split.txt", "r") as reader:
            split = 0
            i = ""
            lines = reader.read().splitlines()
            for line in lines:
              if (split % 2 == 0):
                i = line
              else:
                pct_dict[i] = float(line)
              split = split + 1
        except:
          print("An error has occured.")
        print("You may have to sell your balance first")
      menu.buy_balance(pct_dict, apikey_public, apikey_secret)
      f = open('portfolio_split.txt', 'r+')
      f.seek(0)
      g = open('portfolio_split_log.txt', 'a+')
      g.write(f.read())

      f.truncate(0)
      f.close()
      print("Exiting applicaiton now........\n")
      quit()
    elif(menu_choice == 0):
      print("\nExiting program...\n")
      quit()
    else:
      print("****************************************")
      print("* Your input was not a valid selection *")
      print("* Please try again.                    *")
      print("****************************************\n\n")

if __name__ == '__main__':
  main()
