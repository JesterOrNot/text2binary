#!/usr/bin/python3

from sys import argv

def char2bin(char):
    return str(bin(ord(char)))[2:]

def text2bin(text):
    return " ".join(list(map(char2bin, text)))

def main():
    with open(argv[1], "r") as file:
        content = file.read()
    with open(argv[1].split(".")[0] + ".bin", "w+") as file:
        file.write(text2bin(content))

if __name__ == "__main__":
    main()
