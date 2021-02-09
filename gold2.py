import tkinter
import time
import urllib.request as request
from bs4 import BeautifulSoup as sp
import winsound
import requests

#createNewWindow
def createNewWindow(note):
    newWindow = tkinter.Toplevel(win)
    newWindow.title("notice")
    newWindow.geometry("250x110+700+300")
    newWindow.resizable(0,0)
    newWindow.attributes("-topmost", 1)
    label = tkinter.Label(newWindow,fg="red",text = note,font="MyriadPro-Bold 16")
    label.pack()

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

#attributes
win=tkinter.Tk()
win.title("Rate")
win.geometry("200x110+1300+20")
win.resizable(0,0)
win.iconbitmap("D:\\FFOutput\\gold.ico")
win.config(bg="#FFD306")

#ba 1 def
def topmost(self):
    s_value = s.get()
    win.attributes("-topmost", s_value)
#ba 1
s = tkinter.Scale(orient=tkinter.HORIZONTAL, width=3, length=60)
s.config(from_=0, to=1)
s.config(showvalue=0, tickinterval=0, resolution=1, digits=0)
#s.config(label="topmost")
s.set(0)
s.config(command=topmost)
s.place(anchor=tkinter.SW, x=120,y=110)

#ba 2 def
def ba(self):
    t_value = 1-t.get()/1000
    win.attributes("-alpha", t_value)
#ba 2
t = tkinter.Scale(orient=tkinter.HORIZONTAL,width=3, length=100)
t.config(from_=0, to=900)
t.config(showvalue=0, digits=0)
#s.config(label="Transparency")
t.set(0)
t.config(command=ba)
t.pack()

#standard
i=0
def standard(gold_in,note):
    global i
    global st
    if i==0:
        i+=1
        st=gold_in
    else:
        if gold_in == st:
            st=gold_in
        else:
            duration = 1000 # millisecond
            freq = 440 # Hz
            winsound.Beep(freq, duration)
            st=gold_in
            createNewWindow(note)
            message(note)

#update function
def update():
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
    lb.config(text=note)
    lb.after(325,update)

#label
lb=tkinter.Label(bg="#FFD306",fg="black",text="",font="MyriadPro-Bold 12")

lb.pack()

update()

win.mainloop()