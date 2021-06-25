"""foobar"""
import threading
import time
import logging
import tkinter as tk
from pyautogui import press

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
    window.title("Stay Awake!")
    window.iconbitmap("./icon/awake-icon.ico")
    window.geometry("256x256")

    #Add an Image
    img = tk.PhotoImage(file="img/background.png")
    img_label = tk.Label(window, image=img)
    img_label.pack()

    #Launch Second (Scroll Lock Button Pressing) Thread
    thread = threading.Thread(target=second_thread)
    thread.start()

    #Main tkinter window loop
    window.mainloop()

    #Kill Second Thread
    thread.do_run = False
    thread.join()

if __name__ == "__main__":
    main()
