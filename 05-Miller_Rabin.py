import Encryption1
import Sifan_tools


def miller_factor(num):
    divisor = num
    howmany2 = 0
    while divisor % 2 == 0:
        howmany2 += 1
        divisor //= 2

    return howmany2, divisor


def miller_rabin_witness(a, k, q, p):
    """Is a a Miller Rabin witness for p, if so, p is a composite (return True). Otherwise, we return False"""
    if Sifan_tools.gcd(a, p) != 1:
        print("{} is Miller Rabin witness because gcd({},{}) = {}".format(a, a, p, Sifan_tools.gcd(a, p)))
        return True

    if Encryption1.fastPower(a, q, p) in [p - 1, 1]:
        return False

    for i in range(1, k):
        # then we test k-1 times
        if Encryption1.fastPower(a, (2**i) * q, p) == p - 1:
            return False

    return True


def primality_test(p):
    # get the k and q from p-1
    k, q = miller_factor(p - 1)
    # choose random a 1000 times to accept Miller Rabin test
    for i in range(1000):
        # generate random a
        a = Sifan_tools.sifan_random(2, p - 1)
        # print(a)
        # test whether a is Miller Rabin witness
        if miller_rabin_witness(a, k, q, p):
            # A Miller Rabin witness means p is not prime
            return False
    return True


def generate_prime_number():
    while True:
        # generate a random number and check it out
        test_p = Sifan_tools.sifan_random(2**63, 2**64)
        if test_p % 2 == 0:
            continue
        elif test_p % 3 == 0:
            continue
        elif test_p % 5 == 0:
            continue
        elif test_p % 7 == 0:
            continue
        else:
            if primality_test(test_p):
                print("This is the prime number that we generate:\n", test_p)
                return test_p


# print(miller_factor(2257-1))
generate_prime_number()
# print(miller_rabin_witness(3, 3, 21618441, 172947529))
