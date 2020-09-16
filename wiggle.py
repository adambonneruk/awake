import ctypes, time, datetime

mouse_event = ctypes.windll.user32.mouse_event
MOUSEEVENTF_MOVE = 0x0001
print("press ctrl-c to end mouse shaker")
try:
    while True:
        mouse_event(MOUSEEVENTF_MOVE,25,0,0,0)
        time.sleep(1)
        mouse_event(MOUSEEVENTF_MOVE,0,25,0,0)
        time.sleep(1)
        mouse_event(MOUSEEVENTF_MOVE,-25,0,0,0)
        time.sleep(1)
        mouse_event(MOUSEEVENTF_MOVE,0,-25,0,0)
        time.sleep(1)
except KeyboardInterrupt:
    pass
