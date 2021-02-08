import tkinter
import shutil
import time
from moviepy.editor import *
from pytube import YouTube

#win
win=tkinter.Tk()
win.title("Youtube MP3 Download")
win.geometry("400x180+500+200")
win.resizable(0,0)
win.iconbitmap("D:\\FFOutput\\1519855895061.ico")

#ba 1 def
def topmost(self):
    s_value = s.get()
    win.attributes("-topmost", s_value)
#ba 1
s = tkinter.Scale(orient=tkinter.HORIZONTAL, width=10, length=60)
s.config(from_=0, to=1)
s.config(showvalue=0, tickinterval=0, resolution=1, digits=0)
s.config(label="topmost")
s.set(0)
s.config(command=topmost)
s.place(anchor=tkinter.SE, x=400,y=180)

#label
lb=tkinter.Label(fg="black",text="Enter a YouTube link: ",font="繁黑體 16")
lb.pack()

#display
ib=tkinter.Label(fg="black",text="",font="繁黑體 18")
ib.place(x=50, y=60, width=300, height=20)

#entry
en=tkinter.Entry(bg="#BEBEBE",fg="black",font="繁黑體 14")
en.place(x=50, y=30, width=300, height=20)

#function
errors = 0
def download_files(url):
    global errors

    try:
        mp4 = YouTube(url).streams.get_highest_resolution().download()
        mp3 = mp4.split(".mp4", 1)[0] + '.mp3'

        video_clip = VideoFileClip(mp4)
        audio_clip = video_clip.audio
        audio_clip.write_audiofile(mp3)

        audio_clip.close()
        video_clip.close()

        os.remove(mp4)
        shutil.move(mp3, r"D:\\file")  # Replace this with your own output directory'

    except Exception:
        if errors < 3:
            errors += 1
            print(f"Something went wrong... Trying again! {errors}")
            download_files(url)
        else:
            note=("Could not download file.")
        ib.config(text=note)

def clear():
    en.delete(0, "end")
    ib.config(text="")

def get_mp3():
    url = en.get()
    start_time = time.time()

    print("Converting...")
    download_files(url)

    print(f"Time elapsed: {time.time() - start_time} seconds")
    ib.config(text="Done")





#button
btn=tkinter.Button(text="Download MP3 File",fg="black",font="繁黑體 16")
btn.config(command=get_mp3)
btn.place(x=110, y=100)

#clear
btn=tkinter.Button(text="clear URL",fg="black",font="繁黑體 16")
btn.config(command=clear)
btn.pack(side=tkinter.BOTTOM)

win.mainloop()