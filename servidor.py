import argparse
from ast import arg
from email import parser
import io
import os
import sys
from http.server import *
import socket

from requests import request


# Classe handler
class Handler: 
    def post(self):
        pass

    def header(self):
        pass

    def get(self):
        pass

    # Requests a GET for the index
    def get_index(self, html_file_name, conn):
        html = open(html_file_name)
        content = html.read()
        request = 'HTTP/1.0 200 OK \n\n' + content
        conn.sendall(request.encode())
        html.close()

# Opens a socket for listening.
def serve(ip):
    SERVER_HOST = ip
    SERVER_PORT = 9999 # Porta escolhida
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # AF_INET - IPv4; SOCK_STREAM - TCP
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind((SERVER_HOST, SERVER_PORT))
    server_socket.listen(1)
    print('Listening on port %s ...' %SERVER_PORT)

    handler = Handler()

    while True:
        conn, addr = server_socket.accept()
        req = conn.recv(2048).decode()
        print(req)
        handler.get_index("index.html", conn)
        close(server_socket)


# Closes a socket.
def close(socket):
    socket.close

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-b')
    arguments = parser.parse_args()
    addr = arguments.b
    print("ip: " + addr)

    serve(addr)

if __name__ == '__main__':
    main()