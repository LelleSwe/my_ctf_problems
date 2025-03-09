from sage.all import *
from Crypto.Util.number import getPrime, bytes_to_long, long_to_bytes

a = 10213605335725869902199980943719559376078628344855139518695966294719573727981927244963105128635490914256580609241170785118512847758809339974175050307467513
b = 12226132017457881660841089359898059192854266582734983086780718452790707778384380923987519151891666439949218431538364623553026728617906929652414303678393771
n = 12340305166878273300795406894482315943207820146367671832805850102046679320850362513916978404952722625260673688257802170159773812457930952612322418140710389
y1 = 0xe78777e4ea55952f1be574b1297d6ce94db078893351bbf894d1706fbbc924bd5
y2 = 0x26ba6329f1253cac77ce14a86eb81fd7d7ebcce967234434b21753a4da1d39045

offset = n.bit_length() - y1.bit_length()
M = [[0 for _ in range(3)] for _ in range(3)]
M[0][0] = a * 2**offset * y1 + b - 2**offset * y2
M[1][0] = a
M[2][0] = n

M[0][1] = 2**(n.bit_length() * 2)

M[1][2] = 1

#print(matrix(M))
B, L = matrix(ZZ, M).LLL(transformation=True)

#print("M")
#for mm in M:
#    print([w.bit_length() for w in mm])
#print(B)
#for bb in B:
#    print([w.bit_length() for w in bb])
#print("L")
#for ll in L:
#    print([w.bit_length() for w in ll])
#print(B)
#print(L)

def iLCG(x, p):
    M = matrix(GF(n), [[a, b], [0, 1]])
    return ((M**(-p)) * vector((x, 1)))[0]

def LCG(x, p):
    M = matrix(GF(n), [[a, b], [0, 1]])
    return ((M**p) * vector((x, 1)))[0]

assert iLCG(LCG(17, 1234), 1234) == 17

for i in range(L.nrows()):
    if L[i][0] == 1:
        y2p = abs(B[i][0])
        break

print(f"y2->y1 = {hex(iLCG(y2p + y2*2**offset, 1))}")
print(f"y1 = {hex(y1)}")

print(long_to_bytes(int(iLCG(y2p + y2*2**offset, bytes_to_long(b"a very very very beautiful number :D") + 2))))