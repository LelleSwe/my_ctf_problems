#!/usr/bin/env python3
from flag import part1s, part2s

def flag_to_int(x):
    return int.from_bytes(x.encode(), byteorder="big")

#Use this to turn the numbers back into the flag later!
def int_to_flag(x):
    return x.to_bytes((x.bit_length() + 7)//8, "big").decode()

part1 = flag_to_int(part1s)
part2 = flag_to_int(part2s)

print("Welcome to the Flagxor encryption service!")
print("Please send your 2 secret numbers to encrypt:")
num1 = int(input())
num2 = int(input())

if num1 < part1 or num2 < part2:
    print("Too small! :(")
    exit(0)

encrypted1 = num1 ^ part1
encrypted2 = num2 ^ part2

print(encrypted1)
print(encrypted2)
