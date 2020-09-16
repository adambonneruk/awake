""" wiggle the mouse and prevent screen lock/sleep"""
import tkinter as tk
import time
import ctypes

#Set Constants
mouse_event = ctypes.windll.user32.mouse_event
MOUSEEVENTF_MOVE = 0x0001

# Create the Window
window = tk.Tk()
window.wm_attributes("-topmost", 1)
window.title("Wiggle")
#window.iconbitmap("./icon/icon.ico")
#window.geometry("256x64")

#Display Message
lbl_wiggle = tk.Label(window, text="Wiggling the Mouse!")
lbl_wiggle.pack()


#Execute Main Loop
def mouse_wiggle():
    """move the cursor 1px right, down, left and up again every minute"""
    mouse_event(MOUSEEVENTF_MOVE, 1, 0, 0, 0)
    time.sleep(.25)
    mouse_event(MOUSEEVENTF_MOVE, 0, 1, 0, 0)
    time.sleep(.25)
    mouse_event(MOUSEEVENTF_MOVE, -1, 0, 0, 0)
    time.sleep(.25)
    mouse_event(MOUSEEVENTF_MOVE, 0, -1, 0, 0)
    lbl_wiggle.after(1, mouse_wiggle)

# Start the Window Main Loop
mouse_wiggle()
window.mainloop()
