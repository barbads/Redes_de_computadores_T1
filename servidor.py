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
    def __init__(self):
        self.headers = ""
        self.html_file = ""
        
    def parseHeader(self, req):
        # Transforma a requisicao vinda do browser em uma LISTA DE STRINGS.
        self.headers = req.split('\n')
        print(self.html_file)

        # O Primeiro elemento da lista eh exatamente a requisicao GET, no formato especificado
        # na RFC de HTTP. 
        self.html_file = self.headers[0].split(" ")[1]

    def post(self):
        pass

    def removebar(self, file):
        self.html_file = file.replace('/', '')

    def get(self, conn):
        html = open(self.html_file)
        content = html.read()

        #Resposta da requisicao
        request = 'HTTP/1.0 200 OK \n\n' + content
        print(request.encode())
        conn.sendall(request.encode())

        html.close()

    # Requests a GET for the index
    def get_index(self, html_file_name, conn):
        html = open(html_file_name)
        content = html.read()
        request = 'HTTP/1.0 200 OK \n\n' + content
        print(request.encode())
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

        handler.parseHeader(req)

        # Caso seja uma requisicao para a pagina
        # inicial.
        if (handler.html_file == '/'):        
            handler.get_index("index.html", conn)
        else:
            handler.removebar(handler.html_file)
            handler.get(conn)

        close(server_socket)

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