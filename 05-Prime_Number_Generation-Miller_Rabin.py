import time
from hashlib import sha512
import Encryption1
import Sifan_tools


# define the function to return random number
# two inputs, 1st is the min, 2nd is the max
# the output is an integer number between min and max, both are included
# e.g. input 1,4; output random numbers from 1,2,3,4
def sifan_random(random_min=1, random_max=10):
    # calculate the range
    random_range = random_max - random_min + 1
    # convert the into string
    state = str(time.perf_counter())
    # print("\nThe current state is ", state)
    # using the current state as the seed
    sha256_value = sha512(state.encode("utf-8")).hexdigest()
    # transform the hex value into decimal
    sha256_value_decimal = int(sha256_value, 16)
    # scale the number to meet users' requirement
    result = sha256_value_decimal % random_range + random_min

    # print("The current random number is ", result)
    return result



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
        # test the gcd and I try to rule out the small prime numbers
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
        a = sifan_random(2, p - 1)
        # print(a)
        # test whether a is Miller Rabin witness
        if miller_rabin_witness(a, k, q, p):
            # A Miller Rabin witness means p is not prime
            return False
    return True


def generate_prime_number(num_bit):
    while True:
        # generate a random number and check it out
        test_p = sifan_random(2**num_bit, 2**(num_bit + 1))
        if test_p % 2 == 0:
            continue
        elif test_p % 3 == 0:
            continue
        elif test_p % 5 == 0:
            continue
        elif test_p % 7 == 0:
            continue
        elif test_p % 11 == 0:
            continue
        elif test_p % 13 == 0:
            continue
        elif test_p % 17 == 0:
            continue
        elif test_p % 19 == 0:
            continue

        else:
            if primality_test(test_p):
                print("This is the prime number that we generate:\n", test_p)
                return test_p

# test miller_factor function
# print(miller_factor(2257-1))
# print(miller_rabin_witness(3, 3, 21618441, 172947529))
with open("PNGinput.txt", "r") as file:
    number_bit = int(file.readline())
    # print(number_bit)
    generate_prime_number(number_bit)
