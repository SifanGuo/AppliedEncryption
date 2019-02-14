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


def advanced_chinese_remainder(g, m_x_dict):
    """This is Sifan's advanced CRT implementation, cuz
    the simple version only solves 2 congruences.

    input is g and a dict whose keys are modulus and values are remainders """
    # 1st step: calculate the total product of modulus
    total_modulus_product = 1    # initial value
    # loop the keys of the dictionary
    for modulus in m_x_dict:
        total_modulus_product *= modulus

    # use a list to store the possible x
    x_list = []
    # loop the keys and values of the dictionary
    for modulus, value in m_x_dict.items():
        current_modulus_product = total_modulus_product / modulus
        # if current one meets the criteria
        if current_modulus_product % modulus == value:
            x_list.append(current_modulus_product)
            break
        else:
            inverse_current_modulus_product = 
            x_list.append(current_modulus_product * inverse_current_modulus_product * value)
    # finally, we calculate the sum of the possible X
    response = 0
    for possible_x in x_list:
        response += possible_x

    # Almost forget to mod this
    response %= total_modulus_product
    return response


# Read lines from input file
input_file_name = "POHLIGinput.txt"
test_input_file = open(input_file_name, "r")

test_p = int(test_input_file.readline())
test_g = int(test_input_file.readline())
test_h = int(test_input_file.readline())

# close the file
test_input_file.close()

# the keys are p, the values are e
pe_dict = get_prime_power(11251)
print(pe_dict)


"""
in each of the following cases.
(a) p = 433, g = 7, a = 166.
(b) p = 746497, g = 10, a = 243278.
(c) p = 41022299, g = 2, a = 39183497. (Hint. p = 2· 29^5 + 1.)
(d) p = 1291799, g = 17, a = 192988. (Hint. p − 1 has a factor of 709.)
"""
