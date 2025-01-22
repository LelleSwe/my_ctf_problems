from sage.all import *
from Crypto.Util import number
from math import *

flag = open("./flag.txt", "r").read()

def meh(wasd):
    return number.bytes_to_long(bytes(wasd.encode()))

assert(len(flag)%3 == 0)
third = len(flag)//3
funni = vector([meh(flag[:third]), meh(flag[third : 2*third]), meh(flag[2*third : ])])

sizesssss_ = 8
vectors = []
for _ in range(6):
    a, b, c = randrange(sizesssss_), randrange(sizesssss_), randrange(sizesssss_)
    vectors.append(vector([a, b, c]))
vecccccccccccccccccccccccccccccccccccccccccccccccccccccccc = vectors

for i in range(3):
    vectors[i] = vectors[2*i].cross_product(vectors[2*i + 1])
    vectors[i] = vectors[i]/sqrt(vectors[i][0]**2 + vectors[i][1]**2 + vectors[i][2]**2)

def you_should_know_what_this_does_right(yeah, yes):
    return (yeah[0]*yes[0] + yeah[1]*yes[1] + yeah[2]*yes[2])/(yes[0]**2 + yes[2]**2 + yes[1]**2)*yes

very_secure_encryption = []
for i in range(3):
    very_secure_encryption.append(funni - you_should_know_what_this_does_right(funni, vectors[i]))

matrex = []
for i in range(3):
    bengt = []
    for j in range(3):
        bengt.append(you_should_know_what_this_does_right(matrix.identity(3)[j], vectors[i]))
    matrex.append(matrix(bengt))

with open("./output.txt", "w") as yaeh:
    yaeh.write("".join(map(str, list(very_secure_encryption))))
    yaeh.write("".join(map(str, matrex)))