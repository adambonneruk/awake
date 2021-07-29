"""foobar"""
import threading
import time
import logging
from pyautogui import press
from pystray import MenuItem as item
import pystray
from PIL import Image
import tkinter as tk

#Enabled/Disable Debug Mode
DEBUGMODE = False
if DEBUGMODE:
    logging.basicConfig(format='%(message)s', level=logging.DEBUG)
    logging.debug("DEBUG MODE ACTIVE")

def second_thread():
    """handles launching of a second thread"""
    logging.debug("2nd Thread Start")
    while getattr(threading.currentThread(), "do_run", True):
        for _ in range(0, 2): #always do it twice, so scrollock returns to original state
            press('scrolllock')
            time.sleep(0.4) ##400ms
    logging.debug("2nd Thread Stop")

def main():
    """main gui thread"""
    #Create the Window
    window = tk.Tk()
    window.wm_attributes("-topmost", 1) #always on top
    window.resizable(0, 0) #no maximise button
    window.title("Stay Awake, Don't Sleep!")
    window.iconbitmap("./icon/ZZZZ.ico")
    window.geometry("512x256")

    #Add an Image
    img = tk.PhotoImage(file="image/ZZZZ.png")
    img_label = tk.Label(window, image=img)
    img_label.pack()

    #Launch Second (Scroll Lock Button Pressing) Thread
    thread = threading.Thread(target=second_thread)
    thread.start()

    #Functions used for tray icon code
    def quit_window(icon, item):
        icon.stop()
        window.destroy()

    def show_window(icon, item):
        icon.stop()
        window.after(0,window.deiconify)

    def withdraw_window():
        window.withdraw()
        image = Image.open("./icon/Z.ico")
        menu = (item('Show', show_window), item('Quit', quit_window))
        icon = pystray.Icon("name", image, "Stay Awake, Don't Sleep!", menu)
        icon.run()

    #Close to Tray
    window.protocol("WM_DELETE_WINDOW", withdraw_window)

    #Start in Tray
    withdraw_window()

    #Main tkinter window loop
    window.mainloop()

    #Kill Second Thread
    thread.do_run = False
    thread.join()

if __name__ == "__main__":
    main()
