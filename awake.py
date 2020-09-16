"""foobar"""
import threading
import time
import logging
import tkinter as tk
from pyautogui import press
from key_state import is_scrolllock

#Enabled/Disable Debug Mode
DEBUGMODE = True
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
    #Original Scroll Lock State
    logging.debug("Starting Scrol Lock Position: %s", str(is_scrolllock()))

    #Create the Window
    window = tk.Tk()
    window.wm_attributes("-topmost", 1) #always on top
    window.resizable(0, 0) #no maximise button
    window.title("Keep Awake")
    window.iconbitmap("./icon/awake-icon.ico")
    window.geometry("256x64")

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
