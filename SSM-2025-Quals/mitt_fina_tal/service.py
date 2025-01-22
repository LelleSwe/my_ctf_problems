#!/usr/bin/env python3
from Crypto.Util import number
from flag import flag

def str_to_int(x):
    return number.bytes_to_long(x.encode())

print("I lost my beautiful number. Could you please help me find my beautiful number again?")

a, b, n = sorted([number.getPrime(22*8) for _ in range(3)])

print(f"a = {a}")
print(f"b = {b}")
print(f"n = {n}")

def LCG(x):
    return (a*x + b) % n

user = int(input())

if LCG(LCG(LCG(user))) == str_to_int("A whole new world..."):
    print(flag)
else:
    print("My beautiful number, where are you?")