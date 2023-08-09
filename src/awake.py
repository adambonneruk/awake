"""awake: prevent the system from entering sleep or turning off the display"""
import logging, pystray, os, ctypes
import tkinter as tk
from pystray import MenuItem as item
from PIL import Image

DEBUGMODE = True
if DEBUGMODE:
    logging.basicConfig(format='%(message)s', level=logging.DEBUG)
    logging.debug("DEBUGMODE = True")

def main():
    """The main() function creates a window, a tray icon, and sets the execution state"""

    # 0x80000000 | ES_CONTINUOUS       | Informs the system that the state being set should remain in effect
    # 0x00000002 | ES_DISPLAY_REQUIRED | Forces the display to be on by resetting the display idle timer
    ctypes.windll.kernel32.SetThreadExecutionState(0x80000002)
    logging.debug("SetThreadExecutionState = 0x80000002")

    # set the base directory for executable portability
    basedir = os.path.dirname(__file__)

    # create a window and load an image file
    window = tk.Tk()
    window.wm_attributes("-topmost", 1) #always on top
    window.resizable(0, 0) #no maximise button
    window.title("Awake")
    window.iconbitmap(os.path.join(basedir, "assets\\awake.ico"))
    window.geometry("512x256")
    img = tk.PhotoImage(file=os.path.join(basedir, "assets\\ZZZZ.png"))
    img_label = tk.Label(window, image=img)
    img_label.pack()

    # Functions used for tray icon code
    def quit_window(icon, item):
        """Stop the window, kill the process, this will trigger end of window.mainloop()"""
        icon.stop()
        window.destroy()

    def show_window(icon, item):
        """Stop the tray icon/menu and relaunch the window"""
        icon.stop()
        window.after(0,window.deiconify)

    def withdraw_window():
        """Run the application in the tray instead of a window, build the icon and menu"""
        window.withdraw()
        image = Image.open(os.path.join(basedir, "assets\\awake-icon-64.png"))
        menu = (item('Show', show_window), item('Quit', quit_window))
        icon = pystray.Icon("name", image, "prevent the system from entering sleep", menu)
        icon.run()

    window.protocol("WM_DELETE_WINDOW", withdraw_window) # withdraw window instead of exit on close
    withdraw_window() # withdraw the window (start in the tray)
    window.mainloop() # start the main tkinter loop

    # now that the window.mainloop() has finished, close the program
    ctypes.windll.kernel32.SetThreadExecutionState(0x80000000) # return to normal
    logging.debug("SetThreadExecutionState = 0x80000000")

if __name__ == "__main__":
    main()
