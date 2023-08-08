"""awake: a small utility to keep a windows machine from going asleep"""
import threading, time, logging, pyautogui
from pyautogui import press
from pystray import MenuItem as item
import pystray
from PIL import Image
import tkinter as tk
import os

# Enabled/Disable Debug Mode
DEBUGMODE = False
if DEBUGMODE:
    logging.basicConfig(format='%(message)s', level=logging.DEBUG)
    logging.debug("DEBUG MODE ACTIVE")

# Global Varibles
tick = 0.4 # is 400ms
toggling = True # we start the program actively toggling

def thread_toggle_scrolllock():
    """handles launching of a second thread"""
    global toggling, tick
    logging.debug("2nd Thread Start")
    pyautogui.FAILSAFE = False # fixes thread dying when cursor corner of screen
    while getattr(threading.current_thread(), "do_run", True):
        if toggling:
            for _ in range(0, 2): #always do it twice, so scrollock returns to original state
                time.sleep(tick) 
                logging.debug("toggling: " + str(toggling))
                press('scrolllock')
        else:
            time.sleep(tick*2) # double the normal tick as we arnt in that twice for loop
            logging.debug("toggling: " + str(toggling))
    logging.debug("2nd Thread Stop")

def main():
    """main gui thread"""
    global toggling

    # set the base directory for executable portability
    basedir = os.path.dirname(__file__)

    # Create the Window
    window = tk.Tk()
    window.wm_attributes("-topmost", 1) #always on top
    window.resizable(0, 0) #no maximise button
    window.title("Stay Awake, Don't Sleep!")
    window.iconbitmap(os.path.join(basedir, "assets\\awake.ico"))
    window.geometry("512x256")

    # Add an Image
    img = tk.PhotoImage(file=os.path.join(basedir, "assets\\ZZZZ.png"))
    img_label = tk.Label(window, image=img)
    img_label.pack()

    # Launch Second (Scroll Lock Button Pressing) Thread
    logging.debug("toggling: " + str(toggling))
    thread = threading.Thread(target=thread_toggle_scrolllock)
    thread.start()

    # Functions used for tray icon code
    def quit_window(icon, item):
        icon.stop()
        window.destroy()

    def show_window(icon, item):
        icon.stop()
        window.after(0,window.deiconify)

    def stop_or_start():
        logging.debug("pause functionality trigger")
        global toggling
        toggling = not toggling # flip true to false or vice-versa

    def withdraw_window():
        window.withdraw()
        image = Image.open(os.path.join(basedir, "assets\\awake-icon-64.png"))
        menu = (item('Show', show_window), item("Start/Stop", stop_or_start), item('Quit', quit_window))
        icon = pystray.Icon("name", image, "Stay Awake, Don't Sleep!", menu)
        icon.run()

    #Close to Tray
    window.protocol("WM_DELETE_WINDOW", withdraw_window)

    #Start in Tray
    withdraw_window()

    #Main tkinter window loop
    window.mainloop()

    #Kill Second Thread
    toggling = False
    logging.debug(toggling)
    thread.do_run = False
    thread.join()

if __name__ == "__main__":
    main()
