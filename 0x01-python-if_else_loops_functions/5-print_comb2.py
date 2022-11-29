#!/usr/bin/python3
for num in range(0, 99):
    if num < 10:
        print("0", end='')
    print(f"{num}", end=', ')
print("99")
