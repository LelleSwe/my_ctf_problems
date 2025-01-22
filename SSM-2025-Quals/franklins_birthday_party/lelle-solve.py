from hashlib import sha256

input1 = b"83033972"
input2 = b"21893836"

assert int(sha256(b"GIFFEL-" + input1).hexdigest(), 16) >> 203 == int(sha256(b"GIFFEL-" + input2).hexdigest(), 16) >> 203

from pwn import *
from Crypto.Util.number import long_to_bytes, bytes_to_long

conn = remote("franklins-birthday-party.ctfchall.se", 50000, ssl=True)

conn.recvuntil(b": ")
n = int(conn.recvline().decode())
print(f"{n = }")
conn.recvline()

def rotl256(inp, amount):
    return (inp << amount | inp >> (256 - amount)) & ((1 << 256) - 1)

def convert(inp):
    inp = bytes_to_long(inp)
    inp = rotl256(inp, 256 - 103)
    inp = (inp * pow(n, -2, 2**256)) % 2**256
    inp ^= 0x3d90103675a7d8d5d6663c9d5efa829eabe98a276f2ad183d4b8e24c98e3d525
    inp = rotl256(inp, 256 - 57)
    return hex(inp)[2:]

inp1 = convert(input1)
inp2 = convert(input2)

conn.sendline(inp1)
conn.sendline(inp2)

conn.interactive()