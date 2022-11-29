#!/usr/bin/python3
def uppercase(str):

    for ch in str:
        ascii = ord(ch)
        if 96 < ascii < 123:
            print(f"{chr(ascii - 32)}", end='')
        else:
            print(f"{ch}", end='')
    print()
