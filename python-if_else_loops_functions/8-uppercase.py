#!/usr/bin/python3
def uppercase(s):
    for c in s:
        print(chr(ord(c) & 223), end='')
    print()
