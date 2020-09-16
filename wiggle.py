""" wiggle, small python program for windows used to wiggle the mouse and prevent screen lock/sleep
"""
import time
import ctypes

#Set Constants
mouse_event = ctypes.windll.user32.mouse_event
MOUSEEVENTF_MOVE = 0x0001

#Display Message
print("Wiggle, wiggle...")

#Execute Main Loop
try:
    while True:
        mouse_event(MOUSEEVENTF_MOVE, 32, 0, 0, 0)
        time.sleep(1)
        mouse_event(MOUSEEVENTF_MOVE, 0, 32, 0, 0)
        time.sleep(1)
        mouse_event(MOUSEEVENTF_MOVE, -32, 0, 0, 0)
        time.sleep(1)
        mouse_event(MOUSEEVENTF_MOVE, 0, -32, 0, 0)
        time.sleep(1)
except KeyboardInterrupt:
    pass
