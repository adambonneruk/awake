"""awake: prevent the system from entering sleep or turning off the display"""
import logging, pystray, os, ctypes
from pystray import MenuItem as item
from PIL import Image

DEBUGMODE = False
if DEBUGMODE:
    logging.basicConfig(format='%(message)s', level=logging.INFO) # PIL uses debug, info cleaner
    logging.info("DEBUGMODE = True")

def main():
    """The main() function creates a tray icon, and sets the execution state"""

    global awake_state
    awake_state = True
    logging.info("Awake State: " + str(awake_state))

    # 0x80000000 | ES_CONTINUOUS       | Informs the system that the state being set should remain in effect
    # 0x00000002 | ES_DISPLAY_REQUIRED | Forces the display to be on by resetting the display idle timer
    ctypes.windll.kernel32.SetThreadExecutionState(0x80000002)
    logging.info("SetThreadExecutionState: 0x80000002")

    # set the base directory for executable portability
    basedir = os.path.dirname(__file__)
    logging.info("Base Directory (for image loading) is: \"" + str(basedir) + "\"")

    # Functions used for tray icon code
    def stop(icon, item):
        """stop the icon, killing the process, this will trigger end of the program"""
        logging.info("Stop Program")
        icon.stop()

    def icon_for_state():
        """load different image path for icon based on awakeness state"""
        global awake_state
        if awake_state:
            return str(os.path.join(basedir, "assets\\awake-icon-64.png"))
        else:
            return str(os.path.join(basedir, "assets\\awake-icon-64-off.png"))

    def pause_awakeness(icon, item):
        """pause awakeness by changing awake_state and changing win32 thread execution state"""
        global awake_state
        awake_state = not(awake_state)
        logging.info("Awake State was: " + str(not(awake_state))+ ", is now: " + str(awake_state))

        if awake_state:
            icon.icon = Image.open(icon_for_state())
            ctypes.windll.kernel32.SetThreadExecutionState(0x80000002) #keep awake
            logging.info("SetThreadExecutionState: 0x80000002")
        else:
            icon.icon = Image.open(icon_for_state())
            ctypes.windll.kernel32.SetThreadExecutionState(0x80000000) # return to normal
            logging.info("SetThreadExecutionState: 0x80000000")

    def withdraw_window():
        """Run the application in the tray instead of a window, build the icon and menu"""
        image = Image.open(icon_for_state())
        menu = (item('Start/Pause', pause_awakeness), item('Quit', stop))
        icon = pystray.Icon("name", image, "prevent the system from entering sleep", menu)
        icon.run()

    withdraw_window() # withdraw the window (start in the tray)

    # now that the window_withdraw() has finished, close the program, tidy up
    ctypes.windll.kernel32.SetThreadExecutionState(0x80000000) # return to normal
    logging.info("SetThreadExecutionState: 0x80000000")

if __name__ == "__main__":
    main()
