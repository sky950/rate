import tkinter
import time
import urllib.request as request
from bs4 import BeautifulSoup as sp

#attributes
win=tkinter.Tk()
win.title("Rate")
win.geometry("200x110+1300+100")
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

#ba 2 function
def ba(self):
    t_value = 1-t.get()/1000
    win.attributes("-alpha", t_value)
#ba 2
t = tkinter.Scale(orient=tkinter.HORIZONTAL,width=3, length=100)
t.config(from_=0, to=900)
t.config(showvalue=0, digits=0)
t.set(0)
t.config(command=ba)
t.pack()

#label
lb=tkinter.Label(bg="#FFD306",fg="black",text="",font="MyriadPro-Bold 12")
lb.pack()

#button function1
def update():
    local_time = time.ctime(time.time())
    url="https://rate.bot.com.tw/gold?Lang=zh-TW"
    with request.urlopen(url) as response :
        data=response.read().decode("utf-8")
    root=sp(data,"html.parser")
    goal_in=root.find_all("td")[5].text.replace("回售","").strip()
    goal_out=root.find_all("td")[2].text.replace("買進","").strip()
    s1=("\nGold"+"\n銀行買進: "+goal_in+"\n銀行賣出: "+goal_out)
    note=local_time+s1
    lb.config(text=note)

#button1
btn=tkinter.Button(text="Update",bg="white",font="MyriadPro-Bold 6")
btn.config(width=6)
btn.config(command=update)
btn.pack(side=tkinter.BOTTOM)

win.mainloop()
