import Encryption1
import Sifan_tools

def key_generation(p, q):
    """This function will generate e, s.t. gcd(e, (p-1)*(q-1)).
    Currently, I don't generate p and q"""
    # find an e s.t. gcd(e, (p-1)(q-1)) = 1
    e = (p - 1) * (q - 1) - 1
    while e > 0:
        if Encryption1.gcd(e, (p - 1) * (q - 1)) == 1:
            break
        # test smaller number
        e -= 2
    return e



def encryption(message, e, p, q):
    """This function will encrypt a string message"""
    decimal_message = Encryption1.msg2int(message)

    # calculate the c
    c = Encryption1.fastPower(decimal_message, e, p*q)
    return c


def decryption(c, e, p, q):
    """This function will decrypt the c with e, p, q"""
    # calculate the inverse of e mod (p-1)*(q-1)
    d = Sifan_tools.extended_euclidean(e, (p-1)*(q-1))
    decimal_m = Encryption1.fastPower(c, d, p * q)
    m = Encryption1.int2msg(decimal_m)
    return m


test_message = "Eucli"
test_p = 1492909219
test_q = 2568337697
test_e = 2709929475300581585
# test_e = key_generation(test_p, test_q)
test_c = encryption(test_message, test_e, test_p, test_q)

result = decryption(test_c, test_e, test_p, test_q)

print(test_e)
print(result)
