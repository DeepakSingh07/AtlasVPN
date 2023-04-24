import requests
import json
import time
import re
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])

# import threading

# Referral Link : https://go.atlasv.pn/29D2WYgiMLp3Eo2RA

def Banner():
    print('''
     █████╗ ████████╗██╗      █████╗ ███████╗   ██╗   ██╗██████╗ ███╗   ██╗
    ██╔══██╗╚══██╔══╝██║     ██╔══██╗██╔════╝   ██║   ██║██╔══██╗████╗  ██║
    ███████║   ██║   ██║     ███████║███████╗   ██║   ██║██████╔╝██╔██╗ ██║
    ██╔══██║   ██║   ██║     ██╔══██║╚════██║   ╚██╗ ██╔╝██╔═══╝ ██║╚██╗██║
    ██║  ██║   ██║   ███████╗██║  ██║███████║    ╚████╔╝ ██║     ██║ ╚████║
    ╚═╝  ╚═╝   ╚═╝   ╚══════╝╚═╝  ╚═╝╚══════╝     ╚═══╝  ╚═╝     ╚═╝  ╚═══╝
                    [+]  Developed by DE3P4K  [+]
    ''')

# proxies_list = []
# with open("proxies.txt", "r") as f:
#     proxies_list = f.read().splitlines()

i = 1
# for proxy in proxies_list:
#     proxy_dict = {
#         "https": proxy
#     }
os.system('cls')
Banner()
uuid = input("Enter referrer_uuid : ")
# Sample UUID : 91cc5edf-15e0-49c6-bf2e-88b7a131ee0d

while i<=11:
    if i==11:
        os.system('cls')
        Banner()
        print("DONE. Enjoy 70 Days Premium. :)")
        break
    try:

        # Generating Random Email using developermail.
        mailurl = 'https://www.developermail.com/api/v1/mailbox'
        mailheaders = {
            'accept': 'application/json'
        }

        mailresponse = requests.put(mailurl, headers=mailheaders)
        mailjson = json.loads(mailresponse.text)
        name = mailjson['result']['name']
        token = mailjson['result']['token']

        # Sending request using referral link
        url1 = "https://user.atlasvpn.com/v1/request/join"

        headers1 = {
            'Accept': '*/*',
            'Accept-Encoding' : 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
            'Access-Control-Request-Headers': 'content-type,x-client-id',
            'Origin': 'https://account.atlasvpn.com',
            'Referer': 'https://account.atlasvpn.com/',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-site',
            'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Mobile Safari/537.36 Edg/114.0.0.0'
        }

        res1 = requests.options(url=url1, headers=headers1)

        url2 = "https://user.atlasvpn.com/v1/request/join"

        headers2 = {
            'Accept': 'application/json, text/plain, */*',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
            'Content-Type': 'application/json;charset=UTF-8',
            'Dnt': '1',
            'Origin': 'https://account.atlasvpn.com',
            'Referer': 'https://account.atlasvpn.com/',
            'Sec-Ch-Ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Microsoft Edge";v="114"',
            'Sec-Ch-Ua-Mobile': '?1',
            'Sec-Ch-Ua-Platform': '"Android"',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-site',
            'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Mobile Safari/537.36 Edg/114.0.0.0',
            'X-Client-Id': 'Web'
        }

        data2 = {
            "email": f'{name}@developermail.com',
            "marketing_consent":False,
            "referrer_uuid":f"{uuid}",
            "referral_offer":"initial"
        }

        try:
            ## Opening Inbox
            res2 = requests.post(url=url2, headers=headers2, json=data2)
            inboxurl = f'https://www.developermail.com/api/v1/mailbox/{name}'
            inboxheaders = {
                'accept': 'application/json',
                'X-MailboxToken': f'{token}',
                'Content-Type': 'application/json'
            }

            time.sleep(3)
            
            ## Fetching Email from Inbox
            response = requests.get(inboxurl, headers=inboxheaders)
            jsonresponse = json.loads(response.text)
            if jsonresponse['result'] == []:
                pass
            else:
                msgid = jsonresponse['result'][0]
            
            ## Reading Message
            msgurl = f'https://www.developermail.com/api/v1/mailbox/{name}/messages'
            msgheaders = {
                'accept': 'application/json',
                'X-MailboxToken': f'{token}',
                'Content-Type': 'application/json'
            }

            msgdata = [ msgid ]
            msgres = requests.post(msgurl, headers=msgheaders, data=json.dumps(msgdata))
            match = re.search(r'https://account.atlasvpn.com/auth\?client=.*?(?=\s)', msgres.text)
            if match:
                link = match.group(0)
                link = link.replace('3D', '').replace('amp;', '').replace("=\\r", '').replace('\\n', '')
                # print(link)

                driver = webdriver.Chrome(options=options)
                driver.get(link)
                
                os.system('cls')
                Banner()
                print(f'Referral Count : {i}')

                # try:
                #     ## Writing activation links to Atlas.txt file
                #     with open('Atlas.txt', 'a') as f:
                #         f.write(f'{link}\n')
                # except Exception as e:
                #     print(f'Error: {e}')
            else:
                pass
        except:
            print("Couldn't Fetch Data. Check Req2")

    except:
        print("Couldn't Generate Mail. Check Req1")
    i = i+1
