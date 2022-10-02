# CLI based amazon price tracker
# a-price-whole
# a-size-base-plus a-color-base a-text-normal
import os
import sys
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


Doc = {
    'track'  :  '''
    tracks specific product 
    command : track -p [01] productName
    -p : tracks price on Amazon / flipkart site
    [01] : 0 or 1 , 0 for amazon and 1 for flipkart 
    productName : product name
    example:
        track -p 0 --mobiles
''',
    'geturl'  : '''
    generates url for a specific product
    command : geturl [01] productName
    [01] : 0 or 1 , 0 for amazon and 1 for flipkart 

    example:
        geturl 0 mobiles

    
    ''',
    'cls' : '''
    literally cleans the screen :)
    '''

}

def InScreen() -> str:
    print(green+Intro+white) 

    print("\tWelcome to Amazon/flipkart Price Tracker")
    print(f"\t{red}Due to Amazon Server there is an issue getting the response, so instead use flipkart for price tracking...")

    print(f"{green} Commands:\n\t track :  tracks the price of a specific product\n\t man : provides manual for a command\n\t exit : to exit terminal\n\t cls : to clear the window")


InScreen()

user = input(f"{blue}Enter the username: {red}")

price = {}

def getUrl(search_terms, serviceName):
    if serviceName == "0":
        template = r"https://www.amazon.in/s?k={}&crid=37HXJZ6R06SO3ref=nb_sb_ss_ts-doa-p_2_6&ref=sr_pg_{{}}"
    elif serviceName == "1":
        template = "https://www.flipkart.com/search?q={}&otracker=start&as-show=on&as=off&page={{}}"

    #template = r"https://www.amazon.com/s?k={}&ref=nb_sb_noss_1"
    search = "+".join(search_terms)
    return template.format(search)



while (command := input(f"{blue}{user}@PC : {red}").lower()) != "exit":
    print(f"log {command.split()}")

    if "man" in command:
        print(white + Doc[command.split()[-1]] )

    elif "geturl" in command:
       
        search = command.split()[1:]
        print(getUrl(search[1:], search[0]))
        


    elif "track" in command.split() and  "-p" in command.split() and ("0" in  command.split() or "1" in command.split()):
        headers = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"}
       
        info = command.split()[2:]
        serviceName = info[0]


        
        
        a,b = "/", "\\"
        loading = "/"
        
        S_patterns = {
            # "1" for flipkart
            "1" :{
                "mainContentBox": ['div',{'class':'_1YokD2 _3Mn1Gg'}],
                "box":  ['div', {'class':'_1AtVbE col-12-12'}],
                "name": ['div', {'class':'_4rR01T'}],
                "price": ['div', {'class':'_30jeq3'}]
            },
            # "0" for amazon
            "0" : {
                "mainContentBox": ['span',{'class':'rush-component s-latency-cf-section'}],
                "box":  ['div', {'data-index':'1'}],
                "name": ['span', {'class':'a-size-medium a-color-base a-text-normal'}],
                "price": ['span', {'class':'a-price-whole'}]

            }

        }
        
        Prices = {
            "flipkart": {},
            "amazon": {}
        }
        

        
        for pagenum in range(1,10):
            #URL = f"https://www.flipkart.com/search?q=mobiles&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&as-pos=1&as-type=HISTORY&page={pagenum}"

            URL = getUrl(info[1:], serviceName).format(pagenum)
            
            
            r = requests.get(URL, headers)

            soup = BeautifulSoup(r.content, 'html5lib')
            
            
            table = soup.find(*S_patterns[serviceName]["mainContentBox"])
            if table == None:
                print("Something went wrong!!")
                break

            for product in table.findAll(*S_patterns[serviceName]["box"]):
                

                  name = product.find(*S_patterns[serviceName]["name"])
                  
                  price = product.find(*S_patterns[serviceName]["price"])
                  if (name != None ) and (price != None):
                    #print(f"{magenta}name :- {name.text} | price:- {price.text}")
                    if serviceName == "0":
                        Prices["amazon"][name.text] = price.text
                    elif serviceName == "1":
                        Prices["flipkart"][name.text] = price.text
                    
                  else:
                    print(f"{blue}[loading]:{red}{loading} \r\b" , end="")
                    loading = loading.replace(a, b)
                    a,b = b,a
                    break
        
            
        for name in Prices["flipkart"]:
            
            print(f"\t{yellow} name:- {name} \t price:-" ,(Prices["flipkart"])[name])
            
            

        

    elif command == "cls":
        os.system("CLS")
        InScreen()


    