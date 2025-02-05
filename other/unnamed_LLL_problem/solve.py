from sage.all import *
with open("output.txt") as f:
    f.readline()
    line1, line2 = f.readlines()[:2]

    public_key = eval(line2)

    encrypted = int(line1)

x = column_matrix(vector(public_key))

W = diagonal_matrix([2**64] + [1] * len(public_key) + [2**64])

M = block_matrix(
    [[ 2**64 * x         , 2 * identity_matrix(len(public_key)), 0 ],
     [ -2**64 * encrypted,     Matrix([-1] * len(public_key))  , 2**64 ]
     ])

B = M.LLL()

from Crypto.Util.number import long_to_bytes

for row in B:
    if row[0] != 0 or abs(row[-1]) != 2**64: 
        continue

    sol = list(row[1:-1])

    for i in range(len(sol)):
        sol[i] = int(sol[i] + 1) // 2

    print(
        long_to_bytes(
            sum(
                [x<<i for i, x in enumerate(sol)]
            )         
        )
    )