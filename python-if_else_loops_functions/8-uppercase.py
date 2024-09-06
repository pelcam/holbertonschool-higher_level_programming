#!/usr/bin/python3
def uppercase(str):
    for char in str:
        if ord(char) >= ord('a') and ord(char) <= ord('z'):
            upper_char = chr(ord(char) - 32)
        else:
            upper_char = char
        print("{}".format(upper_char), end="")
    print()
