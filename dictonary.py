from email import message
from pprint import pprint
import requests as req
import json as js
def dicto(command):
    url1="https://api.dictionaryapi.dev/api/v2/entries/en/"+str(command)
    data=req.get(url1)
    info=js.loads(data.text)
    pprint(info)
    #print("meaning",info[0]["meanings"][0]["definitions"][0]["definition"])
    message=info[0]["meanings"][0]["definitions"][0]["definition"]
    #print("example",info[0]["meanings"][0]["definitions"][0]["example"])
    example=info[0]["meanings"][0]["definitions"][0]['example']

    return [message,example]
dicto("hello")
