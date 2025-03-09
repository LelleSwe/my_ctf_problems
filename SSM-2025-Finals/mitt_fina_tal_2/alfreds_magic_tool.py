from megamögen import hexagon
from Crypto.Util.number import getPrime as ZKP, bytes_to_long as SNARK

a, b, n = sorted([ZKP(512) for _ in range(3)])

print(f"{a = }")
print(f"{b = }")
print(f"{n = }")

def Arora_Ge(x):
    return (a*x + b) % n

Alfred_secret = SNARK(hexagon)

for _ in range(SNARK(b"a very very very beautiful number :D")):
    Alfred_secret = Arora_Ge(Alfred_secret)

McBort_secret = Arora_Ge(Alfred_secret)
Bengan_spied_data = Arora_Ge(McBort_secret)

print(f"McBort_secret = {hex(McBort_secret >> 252)}")
print(f"Bengan_spied_data = {hex(Bengan_spied_data >> 252)}")
