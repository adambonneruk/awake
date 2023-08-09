# awake
prevent the system from entering sleep or turning off the display

- [Background and Information](#background-and-information)
- [Usage](#usage)
- [Development](#development)
  - [Python venv and pip](#python-venv-and-pip)
  - [Compile](#compile)
- [Further Reading](#further-reading)
  - [Useful Links](#useful-links)

## Background and Information
This simple windows app keeps a machine/workstation from going idle. Oriignally this application pressed the Scroll Lock button twice every second to keep windows "awake". The recent version now uses a native windows call "```ES_DISPLAY_REQUIRED```" to keep the display on instead.

I built this tool to solve a problem, learn about ```tkinter```, ```pyautogui``` and python ```threading```. Displaying a basic GUI while a second thread takes care of the automation. You can still see that code in as recent as the [v0.4.0](https://github.com/adambonneruk/awake/tree/v0.4.0) tag.

## Usage
The App starts in the system tray (with the [Z] icon).

![Running in the Windows 10 System Tray](.screenshot/in-the-tray.png)

A right-click context menu allowing you to "```Show```" the main GUI  (below) or "```Quit```" and close the application. The GUI close cross again minimises to the system tray.

![Running awake.pyw on Windows 10](.screenshot/stay-awake-dont-sleep.png)

## Development

### Python venv and pip
```ps
# create a venv named venv
py -m venv venv

# run venv
venv/Scripts/Activate.ps1

# install pip prereqs
py -m pip install -r .\requirements.txt --trusted-host pypi.python.org --trusted-host files.pythonhosted.org --trusted-host pypi.org
```

### Compile
```ps
# run manually
pyinstaller "src/awake.spec" --noconfirm

# run automatically
py "tools/make.py"
```

## Further Reading
### Useful Links
- https://stackoverflow.com/questions/58273482/can-pyautogui-be-used-to-prevent-windows-screen-lock
- https://learn.microsoft.com/en-us/windows/win32/api/winbase/nf-winbase-setthreadexecutionstate
