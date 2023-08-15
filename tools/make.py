import os
os.system("pyinstaller src/awake.spec --noconfirm")
os.system("makensis installer/awake.nsi")