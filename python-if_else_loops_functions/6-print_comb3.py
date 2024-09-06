#!/usr/bin/python3
for i in range(0, 90):
    dizain = i//10
    lastdigit = i % 10
    if lastdigit == 0:
        i += (3 + dizain)
    if i < 89:
        print("{:02d}, ".format(i), end="")
    else:
        print("{:02d}".format(i))
