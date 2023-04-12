#!/usr/bin/python3

def read_file(filename=""):
    with open(filename, encoding='UTF8'):
        for line in filename:
            print(line, end='')
