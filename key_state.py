"""get windows key states usin win32 api"""
import time
from win32api import GetKeyState
from win32con import VK_SCROLL

def is_scrolllock():
    """Returns Boolean Value for Scroll Local On or Off"""
    time.sleep(0.25) #introduced delay of working with win api lag
    return bool(GetKeyState(VK_SCROLL) == 1)