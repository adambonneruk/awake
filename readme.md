# ```awake``` (in Python) ![](img/32.png)

## Background
Simple python application (with gui) used to keep stop windows going idle; thereby triggering lockscreen/sleep. While running it presses the scroll lock key (_virtually_) roughly twice a second. Using threads this can happen "in the background" while the tk GUI executes in realtime.

What would you want to use this application for? I have no idea! ```;-)```

## Install Guide
How to configure ``awake``` in your environment:
```powershell
choco install python -y
#restart after installing python
pip install pyautogui
py awake.pyw
```

## Screenshot
```awake``` looks like this when running in Windows 10:

![](img/screenshot.png)

