import argparse
from ast import arg
from email import parser
import io
import os
import sys
from http.server import *
import socket


# Classe handler
class Handler(BaseHTTPRequestHandler): 
    def post(self):
        pass

    def header():
        pass

# Opens a socket for listening.
def serve(ip):
    SERVER_HOST = ip
    SERVER_PORT = 9999 #Porta escolhida
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind((SERVER_HOST, SERVER_PORT))
    server_socket.listen(1)
    print('Listening on port %s ...' % SERVER_PORT)

    while True:
        conn, addr = server_socket.accept()
        req = conn.recv(2048).decode()
        print(req)

# Closes a socket.
def close(socket):
    socket.close

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-b')
    arguments = parser.parse_args()
    addr = arguments.b
    print(addr)

    serve(addr)

if __name__ == '__main__':
    main()