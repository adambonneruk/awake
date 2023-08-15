""" make.py is a tool script used to...
	(1) compile the solution with PyInstaller
    (2) package this with NSIS
"""

import os

print("make.py: compile and package installer")
# compile solution, overwrite existing files (in build/dist folders) using predefined .spec file
print("\n----------------------\npyinstaller src/awake.spec --noconfirm")
os.system("pyinstaller src/awake.spec --noconfirm")

# use nsis to build standard windows looking installer (and uninstaller)
print("\n----------------------\nmakensis installer/awake.nsi")
os.system("makensis installer/awake.nsi")