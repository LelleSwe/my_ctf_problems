#!/usr/bin/env python3
from hashlib import sha256
from Crypto.Util import number
from Crypto.Util.number import getPrime as BrucePass
import sys
from flag import flag

def rotl256(inp, amount):
    return (inp << amount | inp >> (256 - amount)) & ((1 << 256) - 1)

def mask(inp):
    inp = rotl256(inp, 57)
    inp ^= 0x3d90103675a7d8d5d6663c9d5efa829eabe98a276f2ad183d4b8e24c98e3d525
    inp = (inp * n**2) & ((1 << 256) - 1)
    inp = rotl256(inp, 103)
    return number.long_to_bytes(inp)

n = number.getPrime(192)

print("BEEP BEEP.")
print("THIS IS THE 319TH BIRTHDAY OF BENJAMIN FRANKLIN, FOUNDER OF THE UNITED STATES, CURRENTLY A GHOST.")
print(f"MULTIPLIER: {n}")
print("BIRTHDAY PARTY PASSWORDS?")

inp1 = int(input("> "), 16)
inp2 = int(input("> "), 16)

if inp1 == inp2:
    print("BEEP BEEP.")
    print("DUPLICATE USE OF PASSWORD DETECTED.")
    print("REJECTED.")
    sys.exit(0)

if inp1 >= 2**256 or inp2 >= 2**256 or inp1 < 0 or inp2 < 0:
    print("BEEP BEEP.")
    print("PASSWORD OUT OF RANGE.")
    print("REJECTED.")
    sys.exit(0)

m1 = mask(inp1)
m2 = mask(inp2)

h1 = int(sha256(b"GIFFEL-" + m1).hexdigest(), 16) >> 203
h2 = int(sha256(b"GIFFEL-" + m2).hexdigest(), 16) >> 203

hashes = list({h1, h2})

try:
    # "Bruce Schneier knows your password before you do." -https://www.schneierfacts.com/facts/662
    if hashes[1] == BrucePass(256) and hashes[0] == BrucePass(256):
        print("BEEP BEEP.")
        print("PASSWORDS MATCH REFERENCE.")
        print("ACCEPTED.")
        print(flag)
    else:
        print("BEEP BEEP.")
        print("PASSWORDS NOT RECOGNIZED.")
        print("REJECTED.")
except:
    print("BEEP " * 17)
    print("ERROR ERROR ERROR.")
    print("MALFUNCTION RESPONSE: ACCEPTED.")
    print(flag)