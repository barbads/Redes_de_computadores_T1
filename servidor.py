import argparse
from ast import arg
from email import parser
import io
from ipaddress import ip_address
import os
import sys
from http.server import *
from turtle import end_fill

# Classe handler
class Handler(BaseHTTPRequestHandler): 
    def post(self):
        pass

    def header():
        pass

def serve(ip):
    SERVER_HOST = ip
    SERVER_PORT = 9999 #Porta escolhida

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-b')
    arguments = parser.parse_args()
    ip_addr = arguments.b
    print(ip_address)

if __name__ == '__main__':
    main()