import time
import math
import matplotlib.pyplot as plt
from collections import Counter


def msg2bin(message):
    return ''.join(['{0:08b}'.format(ord(x)) for x in message])


def bin2int(binary):
    return int(binary, 2)


def msg2int(message):
    return bin2int(msg2bin(message))


# Initialize the K_list for MD5
K_list = []
for i in range(64):
    K_list.append(hex((int(2**32 * abs(math.sin(i + 1)))) & 0xffffffff))
# print(K_list)
# print(type(K_list[1]))


# rotate the values for the MD5 function
def left_rotate(x, n):
    return ((x << n) | (x >> (32 - n))) & 0xffffffff


# define the main function for md5
def md5(input_m=str(time.perf_counter())):
    # specifies the per-round shift amounts
    shift_amount = [7, 12, 17, 22] * 4 + [5, 9, 14, 20] * 4 + [4, 11, 16, 23] * 4 + [6, 10, 15, 21] * 4
    # print(shift_amount)
    # Initialize the variables
    a0 = 0x67452301
    b0 = 0xefcdab89
    c0 = 0x98badcfe
    d0 = 0x10325476
    # print(type(d0))
    # print(int("0x10325476",16))
    # print(d0)

    # get the binary form of this message
    binary_m = msg2bin(input_m)
    # store the original length of the message
    original_bits_length = len(input_m)
    # format the length into 64-bits
    original_length_in_64bits = '{0:064b}'.format(original_bits_length)

    # print(original_bits_length)
    # print(original_length_in_64bits)
    # print(len(original_length_in_64bits))   # test this, it should be 64
    # print(binary_m)
    # print(type(binary_m))

    # Add A "1" in front of the
    binary_m += "1"

    # print(binary_m)
    # print(len(binary_m))
    # print(type(binary_m))

    # Padding with zeros
    while (len(binary_m) + 64) % 512 != 0:
        binary_m += "0"

    # append the original length in 64-bit format
    binary_m += original_length_in_64bits

    # print(binary_m)
    # print(len(binary_m))
    # print(type(binary_m))

    # Calculate the number of chunks
    chunk_num = len(binary_m) // 512
    # print(chunk_num)

    # Loop for every chunk
    for index in range(chunk_num):
        # Separate the binary into 512-bit chunks
        current_chunk = binary_m[index: index+512]

        # print(current_chunk)
        # print(len(current_chunk))  # test this, the output should be 512

        # break the chunk into sixteen 32-bit words M_list[g], 0 ≤ g ≤ 15
        M_list = [current_chunk[m: m+32] for m in range(16)]
        # print(M_list)
        # print(len(M_list))
        # print(len(M_list[1]))

        # Initialize hash value for this chunk
        A = a0
        B = b0
        C = c0
        D = d0
        # Main Loop
        for j in range(64):
            if 0 <= j < 16:
                F = ((B & C) | ((~B) & D)) & 0xffffffff
                g = j
            elif 16 <= j < 32:
                F = ((D & B) | ((~D) & C)) & 0xffffffff
                g = (5 * j + 1) % 16
            elif 32 <= j < 48:
                F = (B ^ C ^ D) & 0xffffffff
                g = (3 * j + 5) % 16
            elif 48 <= j < 64:
                F = (C ^ (B | (~D))) & 0xffffffff
                g = (7 * j) % 16

            F = (F + A + int(K_list[j], 16) + int(M_list[g], 2)) & 0xffffffff
            A = D
            D = C
            C = B
            B = (B + left_rotate(F, shift_amount[j])) & 0xffffffff

        # Add this chunk's hash to result so far
        # and trim the value to make sure it's eight digits
        a0 = (a0 + A) & 0xffffffff
        b0 = (b0 + B) & 0xffffffff
        c0 = (c0 + C) & 0xffffffff
        d0 = (d0 + D) & 0xffffffff

    md5_result = hex(a0)[2:] + hex(b0)[2:] + hex(c0)[2:] + hex(d0)[2:]
    # print(md5_result)
    # print(len(md5_result))
    return md5_result


# define the function to return random number
# two inputs, 1st is the min, 2nd is the max
# the output is an integer number between min and max, both are included
# e.g. input 1,4; output random number from 1,2,3,4
def sifan_random(random_min=1, random_max=10):
    # calculate the range
    random_range = random_max - random_min + 1
    # convert the into string
    state = str(time.perf_counter())
    print("\nThe current state is ", state)
    # using the current state as the seed
    md5_value = md5(state)
    # transform the hex value into decimal
    md5_value_decimal = int(md5_value, 16)
    # scale the number to meet users' requirement
    result = md5_value_decimal % random_range + random_min

    print("The current random number is ", result)
    return result



# test my function for 1000, 10000, 100000, 1000000 times
random_nums = []
test_times = 10000
for i in range(test_times):
    random_nums.append(sifan_random(1, 10))

# count each value in the list of random numbers
count_result = Counter(random_nums)
# print(count_result)
# print(count_result.keys())
# print(count_result.values())
key_list = []
count_list = []
# get the count results into two lists
for key, count in count_result.items():
    key_list.append(key)
    count_list.append(count)

# draw the results to show the distribution
plt.bar(key_list, count_list, fc='r')
plt.xlabel("The Random Number Value")
plt.ylabel("The Frequency")
plt.show()
# print(type(count_result))
