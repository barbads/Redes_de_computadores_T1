import argparse
from ast import arg
from email import parser
import io
import os
import sys

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-b')
    arguments = parser.parse_args()
    print(arguments.b)

if __name__ == '__main__':
    main()