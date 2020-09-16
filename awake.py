"""tbc"""
import time
import tkinter as tk
from pyautogui import press

#Seup Constants
TIMES = 5

#Create the Window
window = tk.Tk()
window.wm_attributes("-topmost", 1)
window.title("Wiggle")
#window.iconbitmap("./icon/icon.ico")
window.geometry("256x64")

"""def toggle_scrollock(times):
    doubletimes = times * 2
    for _ in range(0, doubletimes):
        press('scrolllock')
        time.sleep(0.4) ##400ms
    window.after(60000, toggle_scrollock(5))"""

def queue_toggle():
    window.after(5000, press('scrolllock'))

queue_toggle()
window.mainloop()
