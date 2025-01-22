from time import time
from hashlib import sha256
hashes = dict()


start = time()
for i in range(2**32):
    inp = b"GIFFEL-" + str(i).encode()

    hashew = int(sha256(inp).hexdigest(), 16) >> 203
    if hashew in hashes:
        print("Collision found!")
        print(inp)
        print(hashes[hashew])
        print(f"Time taken: {time() - start} seconds")
        break
    hashes[hashew] = inp
    if i % 1000000 == 0: print(i)