from Crypto.Util import number
from pwn import *

conn = remote("127.0.0.1", "50000")
conn.recvline()

a = int(conn.recvline().decode()[4:])
b = int(conn.recvline().decode()[4:])
n = int(conn.recvline().decode()[4:])

def LCG(x):
    return (a*x + b) % n

def enc(x):
    return number.bytes_to_long(x.encode())

yes = enc("A whole new world...")

def iLCG(x):
    return ((x - b)*pow(a, -1, n)) % n

reverse = iLCG(iLCG(iLCG(yes)))

conn.sendline(str(reverse).encode())

flag = conn.recvline().decode()
print(flag)