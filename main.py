#Adi Faintuch
# 8/21/20

#IDEA: Make a program that takes in text, uses the online yoda translator,
# and sends the text for you in imessage

import requests
from py_imessage import imessage
from time import sleep
import urllib.parse
import json
import os

#os.system("/Applications/Messages.app/Contents/MacOS/Messages")
#os.system("^C")

err_message = "Too Many Requests: Rate limit of 5 requests per hour exceeded"


phone = input("Enter iPhone number: ")

text_to_translate = input("Enter text message: ")
url_encoded = urllib.parse.quote(text_to_translate)
url = "http://api.funtranslations.com/translate/yoda?text=" + url_encoded

x = requests.get(url);
dict = x.json()

if("error" in dict):
    print(dict["error"]["message"])
else:
    translated = dict["contents"]["translated"]
    guid = imessage.send(phone, translated)


#if not imessage.check_compatibility(phone):
    #print("Not an iPhone")

#guid = imessage.send(phone, translated)


# Let the recipient read the message
#sleep(5)
#resp = imessage.status(guid)

#print(f'Message was read at {resp.get("date_read")}')


#http://api.funtranslations.com/translate/yoda?text=hello
