#!/usr/bin/python3
for i in range(0, 99):
    if i < 9:
        zero = 0
    else:
        zero = ""
    print(f"{zero}{i}, ", end="")
print("99")
