#!/usr/bin/env python3
from merchant import flagfish

from Crypto.Cipher import AES as SEA
from Crypto.Util.Padding import pad as package_fish, unpad as unpackage_fish
from os import urandom as magic_oooh
from random import SystemRandom
import bcrypt as blowfish
from hashlib import sha256 as shafish

rng = SystemRandom()

iv = magic_oooh(16)
key = magic_oooh(16)
aes = SEA.new(key, SEA.MODE_CBC, iv=iv)
magidiced = aes.encrypt(package_fish(flagfish, 16))

print("You walk up to the apparatus, worryingly observing.")
print("Eventually, a magidiced flagfish falls out.")
print((iv + magidiced).hex())

while True:
    try:
        encrypted = bytes.fromhex(input())
        iv = encrypted[:16]
        encrypted = encrypted[16:]

        aes = SEA.new(key, SEA.MODE_CBC, iv=iv)
        decrypted = aes.decrypt(encrypted)
        plaintext = unpackage_fish(decrypted, 16)

        # :see_no_evil:
        if rng.random() < 0.2:
            print(b"It's a lucky day!".encode())
            print(key)

        print(
            blowfish.hashpw(
                magic_oooh(16) + encrypted + magic_oooh(16),
                blowfish.gensalt()).hex()[32:96])

    except KeyboardInterrupt:
        print("goodbye!")
        break

    except Exception as e:
        "ono!"
        print(shafish(magic_oooh(16) + encrypted + magic_oooh(16)).hexdigest())
