import Encryption1
import time

def get_prime_power(p):
    """input is a prime number, so p-1 must be an even numberself.
    output is a dict showing the primes and their powers"""
    p = p - 1
    # using a dict to store the powers of every prime number
    num_counts = {}
    num_counts[2] = 0
    while p % 2 == 0:
        num_counts[2] += 1
        p = p / 2

    # loop the quotient until it reaches p
    current_quotient = 3
    while  current_quotient <= p:
        while p % current_quotient == 0:
            if current_quotient not in num_counts:
                num_counts[current_quotient] = 1
            else:
                num_counts[current_quotient] += 1
            p = p / current_quotient
        current_quotient += 2
    # print(num_counts)
    return num_counts


def chinese_remainder(g, p, q, h):
    """Hopefully, I can find the answer."""
    # 1st step: g mod p, g mod q
    p_remainder = g % p
    # print("{} % {} = {}".format(g, p, p_remainder))
    q_remainder = g % q
    # print("{} % {} = {}".format(g, q, q_remainder))

    # 2st step: reduce the exponent
    p_reduce_exponent = h % (p - 1)
    # print("{} % {} = {}".format(h, p - 1, p_reduce_exponent))
    q_reduce_exponent = h % (q - 1)
    # print("{} % {} = {}".format(h, q - 1, q_reduce_exponent))

    # 3rd step: we must have small numbers right now, and let's calculate
    ans_p = Encryption1.fastPower(p_remainder, p_reduce_exponent, p)
    # print("{} ^ {} mod ({}) = {}".format(p_remainder, p_reduce_exponent, p, ans_p))
    # ans_q = q_remainder ** q_reduce_exponent % q
    ans_q = Encryption1.fastPower(q_remainder, q_reduce_exponent, q)
    # print("{} ^ {} mod ({}) = {}".format(q_remainder, q_reduce_exponent, q, ans_q))

    # 4th step: the inverse of them
    p_inverse_mod_q = Encryption1.InverseCalculator(p, q)
    # print("P's inverse mod Q is ", p_inverse_mod_q)
    q_inverse_mod_p = Encryption1.InverseCalculator(q, p)
    # print("Q's inverse mod P is ", q_inverse_mod_p)

    # 5th step: times inverse and addition
    response = (q * q_inverse_mod_p * ans_p + p * p_inverse_mod_q * ans_q ) % (p * q)

    return response


get_prime_power(1291799)

"""
in each of the following cases.
(a) p = 433, g = 7, a = 166.
(b) p = 746497, g = 10, a = 243278.
(c) p = 41022299, g = 2, a = 39183497. (Hint. p = 2· 29^5 + 1.)
(d) p = 1291799, g = 17, a = 192988. (Hint. p − 1 has a factor of 709.)
"""
