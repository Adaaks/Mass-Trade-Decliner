# Imports required modules to run the program

import requests
import configparser
import os

# Gets cookie from config.ini

config = configparser.ConfigParser()
config.read_file(open(r"Config.ini"))
cookie = str(config.get("auth","cookie"))

config.read_file(open(r"Config.ini"))

# Authenticates into roblox so it can send post requests/get requests
session = requests.Session()
session.cookies[".ROBLOSECURITY"] = cookie

req = session.post(
    url="https://auth.roblox.com/"
)

if "X-CSRF-Token" in req.headers:  
    session.headers["X-CSRF-Token"] = req.headers["X-CSRF-Token"]  


req2 = session.post(
    url="https://auth.roblox.com/"
)

# Variables for inbounds and outbounds
totaltrades = 0
totaltrades3 = 0

# Function for clearing inbounds

def inbounds():
    while True:
        try:
            def program():
                global totaltrades
                global progress
                progress = 0
                
                # Gets the amount of trades to clean
                count = session.get("https://trades.roblox.com/v1/trades/Inbound/count")
                count2 = count.json()
                totaltrades = count2['count']
                
                # Gets trade ids
                Recent = session.get("https://trades.roblox.com/v1/trades/Inbound?sortOrder=Desc&limit=10")
                Recent2 = Recent.json()
                trade = Recent2['data'][0]['id']
                
                # Declines  the trade ids
                post1 = session.post(f"https://trades.roblox.com/v1/trades/{trade}/decline")
                progress += 1
                print(f"Deleted: {progress}/{totaltrades}")
                # Restarts as a result of while true
            program()
            
        # If there is an IndexError, it will stop the program, because this means the trades have all been cleaned
        except:
            if progress == totaltrades:
                print("[SUCCESS] Declined all your INBOUND trades")
                print("")
                inputs()

# Function for clearing outbounds

def outbounds():
     while True:
        try:
            def program2():
                global totaltrades3
                global progress2
                progress2 = 0
                
                # Gets the amount of trades to clean
                count = session.get("https://trades.roblox.com/v1/trades/Outbounds/count")
                count2 = count.json()
                totaltrades3 = count2['count']
                
                # Gets trade ids
                Recent = session.get("https://trades.roblox.com/v1/trades/Inbound?sortOrder=Desc&limit=10")
                Recent2 = Recent.json()
                trade = Recent2['data'][0]['id']
                
                # Declines  the trade ids
                post1 = session.post(f"https://trades.roblox.com/v1/trades/{trade}/decline")
                progress2 += 1
                print(f"Deleted: {progress2}/{totaltrades}")
                # Restarts as a result of while true
            program2()
            
        # If there is an IndexError, it will stop the program, because this means the trades have all been cleaned
        except:
            if progress2 == totaltrades3:
                print("[SUCCESS] Declined all your OUTBOUND trades")
                print("")
                inputs()
                
# Function for inputting method
def inputs():
    print("[1] Inbounds\n[2] Outbounds\n")
    ask = int(input("Method: "))

    if ask == 1:
        inbounds()
    elif ask == 2:
        outbounds()
    elif ask > 2:
        print("[ERROR] You must enter either 1 or 2")
        inputs()
    else:
        print("[ERROR] You must enter either 1 or 2")
        inputs()

# Enables program
inputs()
    
