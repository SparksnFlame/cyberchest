#!/bin/python3

#Importing modules
import sys
from datetime import datetime as dt

#Sockets
import socket

HOST = "127.0.0.1"
PORT = "5555"

sckt = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #AF_INET IPV4, sock strem = port
sckt.connect(HOST, PORT)
