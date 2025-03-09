from pwn import *
from time import time
from string import printable

conn = remote("LOCALHOST", "50000")

#Dialoge skip
print(conn.recvline())
print(conn.recvline())

encrypted_ = conn.recvline().decode()
print(f"{encrypted_ = }")
encrypted = bytearray(bytes.fromhex(encrypted_))

blocks = []
while len(encrypted) > 0:
    blocks.append(encrypted[:16])
    encrypted = encrypted[16:]

print(f"encrypted = {blocks}")

#Get rid of some stranger printables
#like newline and stuff
chars = printable.replace("\\", "").encode()[:-6]
print(chars)

def check_padding(iv, enc, tries = 10):
    ipt = 0
    for _ in range(tries):
        ipt += 1
        send = (bytes(iv) + bytes(enc)).hex().encode()
        #print(enc)
        start = time()
        conn.sendline(send)
        recv = conn.recvline()
        #print(recv, end="")

        end = time()
        #print(((end - start) * 1000), end - start > 0.1, ipt)
        if end - start > 0.1:
            return True
    return False

plaintexts = []

assert check_padding(blocks[-2], blocks[-1])

#POA all ciphertext blocks + 1 iv in AES
for block_idx in range(len(blocks) - 1):
    iv = blocks[block_idx][:]
    enc = blocks[block_idx + 1][:]
    
    #Find amount of starting padding
    start_index = 0
    if check_padding(iv, enc):
        for start_index in range(16):
            iv[15 - start_index] ^= 1
            attempt = check_padding(iv, enc)
        
            #print(attempt)
            #print((bytes(iv) + bytes(enc)).hex().encode())
            #conn.interactive()
        
            iv[15 - start_index] ^= 1
            if attempt:
                start_index = start_index
                print(f"start padding: {start_index}")
                
                #Prep the padding correctly for the bruting step
                for switch_idx in range(start_index + 1):
                    iv[15 - start_index + switch_idx] ^= (start_index)
                    iv[15 - start_index + switch_idx] ^= (start_index + 1)
                break
        else:
            print("""ono! 2""")
            exit()

    #Iterate over all bytes 1 - 16 in the block, 
    # in reverse
    for index in range(start_index, 16):
        iv[15 - index] ^= (index + 1)
        #if start_index > 0:
        #    print([a^b for a, b in zip(iv, blocks[block_idx])])

        #Brute force individual character
        for char in chars:
            #print(f"\rAttempting char {chr(char)}", end="")
            iv[15 - index] ^= char


            attempt = check_padding(iv, enc)
            if attempt:
                break
            else:
                iv[15 - index] ^= char
        #In case no char is valid
        #simply exit. The attack has
        #failed.
        else:
            print("\nono!")
            print(block_idx, index)
            exit()
        
        print(f"Found char for index {index}")
        #print(f"{b"".join([(a^b).to_bytes(1, "big") for a,b in zip(iv, blocks[block_idx])])}")
        #print(f"{iv = }")

        #Switch all padding for next step
        for switch_idx in range(index + 1):
            #print(f"{iv = }")
            iv[15 - index + switch_idx] ^= (index + 1)
            iv[15 - index + switch_idx] ^= (index + 2)
            #print(f"{iv = }")

    #Theoretically each byte in plaintext with current
    #iv should be padding, so by removing padding
    #we transform iv into plaintext
    for i in range(16):
        iv[i] ^= 17

    print(f"{b"".join([(a^b).to_bytes(1, "big") for a,b in zip(iv, blocks[block_idx])])}")
    
    #Make sure we got 0-bytes by sending a 1 for last pos
    iv[-1] ^= 1
    assert check_padding(iv, enc)
    iv[-1] ^= 1
    
    #XORing with original iv since decrypted is msg ^ iv
    for i in range(len(iv)):
        iv[i] ^= blocks[block_idx][i]

    plaintexts.append(iv)

conn.close()
#Check message
from Crypto.Util.Padding import unpad
print(unpad(b"".join(map(bytes, plaintexts)), 16).decode())