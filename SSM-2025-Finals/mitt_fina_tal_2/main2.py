from sage.all import *
from megamögen import s
from Crypto.Util.number import getPrime, bytes_to_long

a, b, n = sorted([getPrime(512), getPrime(512), getPrime(512)])

# Solution is highly inconsistent based on parameter choice. With this I at least know the output is solveable.
a = 10213605335725869902199980943719559376078628344855139518695966294719573727981927244963105128635490914256580609241170785118512847758809339974175050307467513
b = 12226132017457881660841089359898059192854266582734983086780718452790707778384380923987519151891666439949218431538364623553026728617906929652414303678393771
n = 12340305166878273300795406894482315943207820146367671832805850102046679320850362513916978404952722625260673688257802170159773812457930952612322418140710389
assert a.bit_length() == 512
assert b.bit_length() == 512
assert n.bit_length() == 512
assert is_prime(a)
assert is_prime(b)
assert is_prime(n)

print(f"{a = }")
print(f"{b = }")
print(f"{n = }")

def LCG(x, p):
    M = matrix(GF(n), [[a, b], [0, 1]])
    return ((M**p) * vector((x, 1)))[0]

def LCG2(x):
    return (a*x + b) % n

assert LCG(7, 1) == LCG2(7)
assert LCG(3745, 1) == LCG2(3745)
assert LCG(74325325, 4) == LCG2(LCG2(LCG2(LCG2(74325325))))

yp = bytes_to_long(s) 
assert yp < n

yp = LCG(yp, bytes_to_long(b"a very very very beautiful number :D"))

y1 = LCG(yp, 1)
y2 = LCG(y1, 1)

print(f"y1 = {hex(y1 >> 252)}")
print(f"y2 = {hex(y2 >> 252)}")

#debug heheh
#print(f"y1 = {hex(y1)}")
#print(f"y2 = {hex(y2)}")
