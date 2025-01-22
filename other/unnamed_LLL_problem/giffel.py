from Crypto.Util import number

flag = number.bytes_to_long(open("./flag.txt", "rb").read().replace(b"\n", b""))
print(open("./flag.txt", "rb").read().replace(b"\n", b""))
#How many bits are in the flag?
from math import *
length = ceil(log2(flag))

#Det måste finnas en smartare lösning än detta... :thinking:
#Dock jag skulle ännu hällre få mycket korkadare lösningar uppvisade.
#Skicka gärna alla dina korkade lösningar för att göra om ett tal till en sekvens med bits till _ på Discord!
#(Jag har inte förvarnat dem)
def bit_o_byte(bauhaus):
    the_list = []

    random_increasing_variable = 0
    while bauhaus >> random_increasing_variable >= 1:
        if (bauhaus >> random_increasing_variable) & 1 == 1:
            the_list.append(1)
        else:
            the_list.append(0)
        random_increasing_variable += 1
    return the_list

#Produces a super increasing sequence of length jag skrev på engelska
def did_you_know_that_a_4chan_user_solved_an_open_math_problem(length):
    from random import randrange
    lsit = []
    jemeemgm_summering = 0
    for i in range(length):
        if i != 0:
            jemeemgm_summering += lsit[i-1]
        add = randrange(jemeemgm_summering + 1, 2*jemeemgm_summering + 17)
        lsit.append(add)
    return lsit

alfreds_lista = did_you_know_that_a_4chan_user_solved_an_open_math_problem(length)
flaggha = 0


def genererararrererare(listan):
    from random import randrange
    summering = 0
    for i in listan:
        summering += i
    men_reee = randrange(summering, summering*2)
    return men_reee

#behöver kanske något privat tal också? q, kanske?
pallkrage = genererararrererare(alfreds_lista)

def publik_nyckel(alfreds_lista, pallkrage):
    def odla_rabarber(pallkrage):
        #jag stal lite kod online, pallar inte komma på egen
        # Define a function 'gcd' to calculate the greatest common divisor (GCD) of two positive integers.
        def gcd(p, q):
            # Use Euclid's algorithm to find the GCD.
            while q != 0:
                p, q = q, p % q
            return p
        from random import randrange
        kanske = randrange(23, pallkrage)

        #titta!
        while gcd(kanske, pallkrage) != 1:
            kanske += 1
        return kanske

    rabarber = odla_rabarber(pallkrage)
    jag_ger_dig_denna_senare = []
    for ja in alfreds_lista:
        jag_ger_dig_denna_senare.append(ja*rabarber % pallkrage)
    return jag_ger_dig_denna_senare

collatz_conjecture = publik_nyckel(alfreds_lista, pallkrage)

#Jag tror jag konstruerar hemligheten här? :thonkoning:
for merkle, hellman in zip(collatz_conjecture, bit_o_byte(flag)):
    flaggha += merkle*hellman

def idk_how_to_write_lists_and_i_cant_be_bothered_googling(lsit, yaeh):
    yaeh.write("\n[")
    for i in range(len(lsit)-1):
        yaeh.write(str(lsit[i]) + ", ")
    yaeh.write(str(lsit[-1]) + "]")


with open("./output.txt", "w") as yaeh:
    idk_how_to_write_lists_and_i_cant_be_bothered_googling(did_you_know_that_a_4chan_user_solved_an_open_math_problem(17), yaeh)
    yaeh.write("\n" + str(flaggha))
    idk_how_to_write_lists_and_i_cant_be_bothered_googling(collatz_conjecture, yaeh)
