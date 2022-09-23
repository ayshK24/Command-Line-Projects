# CLI based amazon price tracker

import os

import re
import requests
from bs4 import BeautifulSoup




# helps to show the ANSI colors in cmd outside the vscode 
os.system("")


# ANSI Color codes 
green = "\033[1;32m"
red = "\033[1;31m"
magenta = "\033[0;35m"
yellow = "\033[0;33m"
white = "\033[1;37m"
blue = "\033[0;34m"
Intro = '''
              _     
             | |    
__      _____| |__  
\ \ /\ / / _ \ '_ \ 
 \ V  V /  __/ |_) |
  \_/\_/ \___|_.__/ 

'''


Doc = '''
    command : track -p  --productName
    -p : tracks price on Amazon site
    --productName : product name
'''
print(green+Intro+white) 

print("\tWelcome to Amazon Price Tracker")

print(f"{green} Commands:\n\t track :  tracks the price of a specific product\n\t man : provides manual for a command\n\t exit : to exit terminal\n\t cls : to clear the window")


user = input(f"{blue}Enter the username: {red}")

price = {}
table = soup.find('div', attrs = {'id':'all_quotes'}) 

while (command := input(f"{blue}{user}@PC : {red}").lower()) != "exit":
    print(f"log {command}")
    if command == "man track":
        print(white + Doc )
    elif "track" in command.split() and  "-p" in command.split():
        productName = command.split()[-1][2:]

        URL = f"https://www.amazon.in//s?k={productName}"
        
        r = requests.get(URL)
        soup = BeautifulSoup(r.content, 'html5lib')
        for row in table.findAll({}):pass

    elif command == "cls":
        os.system("CLS")




    