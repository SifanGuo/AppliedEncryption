import Sifan_tools


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


def advanced_chinese_remainder(m_x_dict):
    """This is Sifan's advanced CRT implementation, cuz
    the simple version only solves 2 congruences.

    input is g and a dict whose keys are modulus and values are remainders """
    # 1st step: calculate the total product of modulus
    total_modulus_product = 1    # initial value
    # loop the keys of the dictionary
    for modulus in m_x_dict:
        total_modulus_product *= modulus

    # print(m_x_dict)
    # print(total_modulus_product)
    # use a list to store the possible x
    x_list = []
    # loop the keys and values of the dictionary
    for modulus, remainder in m_x_dict.items():
        # print(modulus)
        # print(remainder)
        current_modulus_product = total_modulus_product // modulus
        # if current one meets the criteria


        inverse_current_modulus_product = Sifan_BsGs_Inverse.extended_euclidean(current_modulus_product % modulus, modulus)
        # print(Sifan_BsGs_Inverse.extended_euclidean(3, 4))
        # print(inverse_current_modulus_product)
        x_list.append(current_modulus_product * inverse_current_modulus_product * remainder)
        # print(x_list)
    # finally, we calculate the sum of the possible X
    response = 0
    for possible_x in x_list:
        response += possible_x

    # Almost forget to mod this
    response %= total_modulus_product
    # print(response)
    return response


# Read lines from input file
input_file_name = "POHLIGinput.txt"
test_input_file = open(input_file_name, "r")

test_p = int(test_input_file.readline())
test_g = int(test_input_file.readline())
test_h = int(test_input_file.readline())

# close the file
test_input_file.close()


"""
in each of the following cases.
(a) p = 433, g = 7, a = 166.
(b) p = 746497, g = 10, a = 243278.
(c) p = 41022299, g = 2, a = 39183497. (Hint. p = 2· 29^5 + 1.)
(d) p = 1291799, g = 17, a = 192988. (Hint. p − 1 has a factor of 709.)
"""

# the keys are p, the values are e
pe_dict = get_prime_power(test_p)
# print(pe_dict)

# The Big N is p-1
N = test_p - 1

# keys are modulus; values are remainders
m_x_dict = {}
for q, e in pe_dict.items():
    current_g = Sifan_BsGs_Inverse.fastPower(test_g, N / (q ** e), test_p)
    # print("current_g", current_g)
    # print("q^e", q**e)
    current_h = Sifan_BsGs_Inverse.fastPower(test_h, N / (q ** e), test_p)
    # print("current_h", current_h)
    m_x_dict[q**e] = Sifan_BsGs_Inverse.baby_step_giant_step(current_g, test_p, current_h) % (q**e)

# print(m_x_dict)

final_answer = advanced_chinese_remainder(m_x_dict)

# finally we have the answer to Pohlig Hellman
print("The answer x of {}^x = {} (mod {}) is {}".format(test_g, test_h, test_p, final_answer))
print("If you don't believe me, you can use fastPower algorithem to test. (Please don't use regular calculation for memory's sake unless you have a good one.)")
