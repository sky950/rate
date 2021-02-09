#olny line notify

import time
import urllib.request as request
from bs4 import BeautifulSoup as sp
import requests

# LineNotify
def lineNotifyMessage(token, msg):
    headers = {
        "Authorization": "Bearer " + token,
        "Content-Type" : "application/x-www-form-urlencoded"
    }

    payload = {'message': msg }
    r = requests.post("https://notify-api.line.me/api/notify", headers = headers, params = payload)
    return r.status_code

def message(mes):
    if __name__ == "__main__":
        token = 'S2IDSvkKjnIPE0W35wpCao7gyFZREVR7XpM941eJTWv'
        message = ("\n"+mes)
        lineNotifyMessage(token, message)

#standard
i=0
def standard(gold_in,note):
    global i
    global st
    if i==0:
        i+=1
        st=gold_in
        #message(note)
    else:
        if gold_in == st:
            st=gold_in
        else:
            st=gold_in
            message(note)

#function
j=0
while j==0:
    local_time = time.ctime(time.time())
    url="https://rate.bot.com.tw/gold?Lang=zh-TW"
    with request.urlopen(url) as response :
        data=response.read().decode("utf-8")
    root=sp(data,"html.parser")
    gold_in=root.find_all("td")[5].text.replace("回售","").strip()
    gold_out=root.find_all("td")[2].text.replace("買進","").strip()
    s1=("\n                 Gold"+"\n        銀行買進: "+gold_in+"\n        銀行賣出: "+gold_out)
    note=local_time+s1
    standard(gold_in,note)
    time.sleep(1)