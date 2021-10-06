import tkinter
import subprocess
import ctypes
from random import randint

ctypes.windll.user32.ShowWindow( ctypes.windll.kernel32.GetConsoleWindow(), 6 )
top = tkinter.Tk()

def helloCallBack():
   yt_links=["fFBQlNEll1E","nnsApEHFuaA","QJ_EcgbMKZg","YAD0s9_kbU4","JdSpuTi9d8A"]
   rand_num=randint(0,len(yt_links)-1)
   command = "cmd /c start chrome https://www.youtube.com/embed/"+yt_links[rand_num]+"?autoplay=1 --new-window"
   subprocess.Popen(command, shell=True)

B = tkinter.Button(top, text ="Press to Start", command = helloCallBack)

top.geometry('250x119+1116+578')
top.attributes('-topmost',True)
B.place(x=85, y=50)
top.mainloop()
