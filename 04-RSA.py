import Encryption1
import Sifan_tools
from hashlib import sha256
import time

# Test the hashlib function
# print(sha256("Sifan".encode("utf-8")).hexdigest())
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
    sha256_value = sha256(state.encode("utf-8")).hexdigest()
    # transform the hex value into decimal
    sha256_value_decimal = int(sha256_value, 16)
    # scale the number to meet users' requirement
    result = sha256_value_decimal % random_range + random_min

    # print("The current random number is ", result)
    return result



def prime_number_generation(min=63, max=64):
    while True:
        # generate random numbers which are 512 bits by default
        random_number = sifan_random(16**min, 16**max)
        # print(random_number)

        # rule out the even number
        if random_number % 2 == 0:
            random_number += 1

        # check the Primality using Fermat Primality Test
        # test 1000 numbers for each random numbers
        test_count = 0
        while test_count < 1000:
            test_num = sifan_random(2 , random_number)
            if Encryption1.fastPower(test_num, random_number - 1, random_number) != 1:
                break
            test_count += 1

        # whether the random_number pass the Fermat Primality Test
        if test_count == 1000:
            # print(random_number)
            return random_number
        # Otherwise, go to next random number


def key_generation(min=63, max=64):
    """This function will generate primes p, q, and another number e (not required to be prime I think), s.t. gcd(e, (p-1)*(q-1)).
    """
    p = prime_number_generation(min, max)
    q = prime_number_generation(min, max)



    # find an e s.t. gcd(e, (p-1)(q-1)) = 1
    e = (p - 1) * (q - 1) - 1
    while e > 0:
        if Encryption1.gcd(e, (p - 1) * (q - 1)) == 1:
            break
        # test smaller number
        e -= 2
    return p, q, e



def encryption(message, e, p, q):
    """This function will encrypt a string message which can be longer than P*Qself.
    If the message is short than P*Q, return a number.
    Else, return a list of numbers."""
    # every 8 bits is 1 Byte and that's one character in ascii
    chunk_size = len(Encryption1.int2bin(p*q)) // 8 - 1

    # Here is for short message, we will return a single c
    if len(message) <= chunk_size:
        decimal_message = Encryption1.msg2int(message)
        # calculate the c
        c = Encryption1.fastPower(decimal_message, e, p*q)
        # print(type(c))
        return c


    # for instance, if p*q is 512 bits, then it's 64 Bytes
    # and the length of each chunk is 63 (64 - 1)
    # print(chunk_size)

    else:
        # initialize a list
        c_list = []
        # In order to take inputs which are longer than p*q
        # Split message into Chunks
        # using the method from stackoverflow in one line
        # https://stackoverflow.com/questions/9475241/split-string-every-nth-character

        chunks = [message[i : i + chunk_size] for i in range(0, len(message), chunk_size)]

        # print(chunks)

        # Sifan's method
        # for i in range(len(message) // chunk_size):
        #     right_index = (i + 1) * chunk_size
        #
        #     # get the right index
        #     if right_index > len(message):
        #         # in case the length can be divided
        #         right_index = len(message)
        #
        #     # print(right_index)
        #     chunks.append(message[i * chunk_size : right_index])
        #     print(chunks)

        for chunk in chunks:
            decimal_message = Encryption1.msg2int(chunk)
            # calculate the c
            c_list.append(Encryption1.fastPower(decimal_message, e, p*q))
            # print("Your message is longer than p*q.")
            # print(chunk)
            # print()
            # print(c_list)
        return c_list


def decryption(c, e, p, q):
    """This function will decrypt the c or c_list with e, p, q"""
    if type(c) is int:
        # calculate the inverse of e mod (p-1)*(q-1)
        d = Sifan_tools.extended_euclidean(e, (p-1)*(q-1))
        decimal_m = Encryption1.fastPower(c, d, p * q)
        m = Encryption1.int2msg(decimal_m)
        return m
    # Otherwise, that's a list
    else:
        m = ""
        for chunk in c:
            d = Sifan_tools.extended_euclidean(e, (p-1)*(q-1))
            decimal_m = Encryption1.fastPower(chunk, d, p * q)
            chunk_m = Encryption1.int2msg(decimal_m)
            # print(chunk_m)
            # print()
            m += chunk_m
        # print(m)
        return m


test_message = "\n\tGood Job!\t I'm using this long sentence as my test case.\n\tThis is the second line of the message~\n so far, it fails to support Chinese characters.\n\tThis is the end of the test message, farewell~"
# print(type(test_message))
# print(len(test_message))
# read input from file RSAinput.txt
RSAinput = open("RSAinput.txt", "r")
test_p = int(RSAinput.readline())
test_q = int(RSAinput.readline())
test_e = int(RSAinput.readline())

RSAinput.close()   # close the file in use

# test_p = 1492909219
# test_q = 2568337697
# test_e = 2709929475300581585
# test_e = key_generation(test_p, test_q)
test_c = encryption(test_message, test_e, test_p, test_q)
print("This is the c or the list of c AKA encrypted message\n", test_c)

result = decryption(test_c, test_e, test_p, test_q)
print("This is the decryption of c or the list of c\n", result)


user_message = input("\nWanna try RSA encryption using my p q and e? Input your message here:")
p, q, e = key_generation()
print("Here is my p: ", p)
print("Here is my q: ", q)
print("Here is my e: ", e)

c = encryption(user_message, e, p, q)
print("\nThis is the c or the list of c AKA encrypted message\n", c)

user_result = decryption(c, e, p, q)
print("\nThis is the decryption of c or the list of c\n", user_result)
