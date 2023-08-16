# awake
prevent the system from entering sleep or turning off the display

- [Background and Information](#background-and-information)
- [Usage](#usage)
- [Development](#development)
  - [Python venv and pip](#python-venv-and-pip)
  - [Compile](#compile)
- [Further Reading](#further-reading)
  - [Useful Links](#useful-links)
- [Contributing to this Project](#contributing-to-this-project)
- [Security Policy for this Project](#security-policy-for-this-project)

## Background and Information
This simple windows app keeps a machine/workstation from going idle. Oriignally this application pressed the Scroll Lock button twice every second to keep windows "awake". The recent version now uses a native windows call "```ES_DISPLAY_REQUIRED```" to keep the display on instead.

I built this tool to solve a problem, learn about ```tkinter```, ```pyautogui``` and python ```threading```. Displaying a basic GUI while a second thread takes care of the automation. Whilst the latest version is much more efficient/compact, you can still see that code in as recent as the [v0.4.0](https://github.com/adambonneruk/awake/tree/v0.4.0) tag.

## Usage
The App starts in the system tray (with the _Z_ icon).

![Running in the system tray](.screenshot/in-the-tray.png)

A right-click context menu allows you to "```Start/Pause```" the program (pausing will allow windows to sleep again, this is represented by ⏸ icon) or "```Quit```" and close the application.

![Start/Pause and Quit Menu while Paused](.screenshot/context-menu.png)

## Development

### Python venv and pip
```ps
# create a venv named venv
py -m venv venv

# run venv
venv/Scripts/Activate.ps1

# install pip prereqs
py -m pip install -r .\requirements.txt --trusted-host pypi.python.org --trusted-host files.pythonhosted.org --trusted-host pypi.org

# list pip installs inside the venv
pip freeze
```

### Compile
```ps
# compile manually
pyinstaller 'src/awake.spec' --noconfirm

package with nsis manually
makensis 'installer/awake.nsi'

# run both automatically
py 'tools/make.py'
```

## Further Reading
### Useful Links
- https://stackoverflow.com/questions/58273482/can-pyautogui-be-used-to-prevent-windows-screen-lock
- https://learn.microsoft.com/en-us/windows/win32/api/winbase/nf-winbase-setthreadexecutionstate
- [change icon dynamically in pystray](https://github.com/moses-palmer/pystray/issues/68)

## Contributing to this Project
This project welcomes contributions of all types. We ask that before you start work on a feature that you would like to contribute, please read the [Contributor's Guide](.github/CONTRIBUTING.md).

## Security Policy for this Project
This project seeks to build secure, versatile and robust portable software. If you find an issue, please report it following the [Security Policy](.github/SECURITY.md)