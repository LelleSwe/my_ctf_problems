from pwn import *

#Use this to turn the numbers back into the flag later!
def int_to_str(x):
    return x.to_bytes((x.bit_length() + x.bit_length()%8)//8, "big").decode()

conn = remote("localhost", "50000")
conn.recvline()
conn.recvline()


send = b"100000000000000000000000000000000000000000"
conn.sendline(send)
conn.sendline(send)

a = int(conn.recvline())
b = int(conn.recvline())

part1 = int_to_str(a ^ int(send.decode()))
part2 = int_to_str(b ^ int(send.decode()))

print(part1 + part2)