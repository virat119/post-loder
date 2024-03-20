import requests
import mechanize
import getpass
import json
import random
import time
from datetime import datetime
from bs4 import BeautifulSoup 
from colorama import Fore, Style
from rich.panel import Panel
from platform import system
import os, platform, binascii, sys, _socket, ssl, certifi, zlib, json, uuid
from os import system as sh
from time import sleep


logo = r'''

 
##   ##   ######  ######     ###     # ##### 
##   ##     ##     ##  ##   ## ##   ## ## ## 
##   ##     ##     ##  ##  ##   ##     ##    
 ## ##      ##     #####   ##   ##     ##    
 ## ##      ##     ## ##   #######     ##    
  ###       ##     ## ##   ##   ##     ##    
  ###     ######  #### ##  ##   ##    ####   
                                             

--------------------------------------------------------------  
      𝐖𝐄𝐋𝐂0𝐌𝐄 𝐓0 LEGENDX RULEX
--------------------------------------------------------------                                                                                
       𝐓𝐇𝐈𝐒 𝐈𝐒 𝐓00𝐋 𝐂𝐑𝐄𝐀𝐓𝐄𝐃 𝐁𝐘 : :  VIRAT ROY
--------------------------------------------------------------  
        𝐌𝐔𝐋𝐓𝐈 𝐈𝐃𝐒 𝐌𝐔𝐋𝐓𝐈 𝐏𝐀𝐆𝐄 𝐖𝐀𝐋𝐋𝐒 𝐌𝐔𝐋𝐓𝐈 𝐅𝐈𝐋𝐄 𝐋0𝐃𝐄𝐑 𝐓00𝐋
--------------------------------------------------------------                            
'''
# Print the logo
print(Fore.CYAN + logo +  Style.RESET_ALL)


    
# Prompt Password 
def pas():
    print('\u001b[37m' + '---------------------------------------------------')
    password = input("𝐏𝐚𝐬𝐬𝐰𝐨𝐫𝐝 : ") 
    print('--------------------------------------------')
    mmm = requests.get('https://pastebin.com/raw/esQjEWVY').text

    if mmm not in password:
        print('[-] <==> Incorrect Password!')
        sys.exit()
        
pas()

# Prompt for cookies file
cookies_file = input("ENTER token FILE PATH : ")
print('--------------------------------------------')

# Read access token IDs from file
with open(tokens_file, 'r') as f:
    access_tokens = f.read().splitlines()

# Prompt for the number of user IDs
num_user_ids = int(input("HOW MANY POSTS YOU WANT FOR LOADER : "))
print('--------------------------------------------')

# Define the user IDs and message files
user_messages = {}
haters_name = {} 

# Prompt for user IDs and message files
for i in range(num_user_ids):
    user_id = input(f"ENTER POST ID #{i+1} : ")
    print('--------------------------------------------')
    hater_name = input(f"ENTER HATER NAME FOR POST ID {user_id} : ")
    print('--------------------------------------------')
    haters_name[user_id] = hater_name
    message_file = input(f"ENTER MESSAGES FILE /NP FOR {user_id} : ")
    print('--------------------------------------------')
    user_messages[user_id] = message_file




# Prompt for delay time in messages
delay_time = int(input("ENTER DELAY/TIME (in seconds) FOR MESSAGES : "))
print('--------------------------------------------')

# Prompt for delay before repeating the process
repeat_delay = int(input("ENTER DELAY/TIME (in seconds) BEFORE REPEATING THE PROCESS : "))
print('--------------------------------------------')

# Get profile name using an access tokens
def get_profile_name(access_tokens):
    url = f'https://graph.facebook.com/v17.0/me?access_tokens={access_tokens}'
    response = requests.get(url)
    data = response.json()
    if 'name' in data:
        return data['name']
    return None

# Function to send a message to a user's inbox conversation using an access tokens
def send_message(access_tokens, user_id, message):
    url = "https://graph.facebook.com/v15.0/{}/comments".format(user_id)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Linux; Android 8.0.0; Samsung Galaxy S9 Build/OPR6.170623.017; wv) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.125 Mobile Safari/537.36',
        'Referer': 'https://www.facebook.com/',
        'Authorization': f'Bearer {access_tokens}'
    }
    data = {'message': hater_name + ' ' + message}

response = requests.post(url, headers=headers, data=data)
        if response.status_code == 200:
        current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        print(f'{Fore.BLUE}[{current_time}] {Fore.YELLOW}Comment sent successfully to user ID {user_id}: {Fore.GREEN}{hater_name + message}')
        return True
    else:
        current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        print(f'{Fore.BLUE}[{current_time}] {Fore.RED}Error sending comment to user ID {user_id}: {Fore.RED}{hater_name + message}')
        print(f'{Fore.RED}[{current_time}] Response content: {Fore.RED}{response.content.decode()}')
        return False

# Main loop to send messages
while True:
    total_successful_messages = 0
    total_unsuccessful_messages = 0

    # Iterate over the access tokens
    for i, access_cookies in enumerate(access_tokens):
        try:
            # Login using the access tokens and get the profile name
            profile_name = get_profile_name(access_tokens)
            if not profile_name:
                continue

            profile_number = i + 1
            access_tokens_id = access_tokens[:4] + '********'

            # Print the profile information
            print(f'{Fore.YELLOW}Profile {profile_number} (ID: {access_tokens_id}): {profile_name}')
            print('--------------------------------------------')

            # Iterate over the user IDs and messages
            for user_id, message_file in user_messages.items():
            	
                # Read messages from the message file for the current user ID
                with open(message_file, 'r') as f:
                    messages = f.read().splitlines()

                # Shuffle the messages for the current user
                
                # Get the hater name for the current user ID
                hater_name = haters_name[user_id]


                # Get the messages count for the current user
                messages_count = len(messages)

                # Get the current message index for the user ID
                message_index = i % messages_count

                # Get the message for the current index
                message = messages[message_index]

                if send_message(access_token, user_id, message):
                    total_successful_messages += 1
                else:
                    total_unsuccessful_messages+= 1

                time.sleep(delay_time)  # Delay between each message
            # Print Facebook ID, message, and current date/time after message is sent
            current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            print(f'{Fore.MAGENTA}Facebook ID: {user_id}')
            print('--------------------------------------------')
            print('Virat ka lund ID Ready To Send Comment')
            print('--------------------------------------------')

        except requests.exceptions.RequestException as e:
            current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            print(f'{Fore.RED}[{current_time}] Internet disconnected. Reconnecting in 10 seconds...{Style.RESET_ALL}')
            time.sleep(10)

        except Exception as e:
            current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            print(f'{Fore.RED}[{current_time}] An error occurred: {str(e)}{Style.RESET_ALL}')
            continue

    print('--------------------------------------------')
    print('All comments sent. Waiting before repeating the process...')
    print('--------------------------------------------')
    time.sleep(delay_time)  # Delay before repeating the process
