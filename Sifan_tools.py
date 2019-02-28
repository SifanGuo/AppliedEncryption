import time
from hashlib import sha256

# This code is taken directly from the textbook. exercise 1.25 at the back of chapter 1
def fastPower(g,x,p):
    a = g
    b = 1
    while x>0:
        if x%2 == 1:
            b = (b*a)%p
        a = (a*a)%p
        x = x//2
    return b

# define the function to calculate the gcd
# input is the two numbers
# output is two lists, 1st one is the list of remainder, 2nd one is the list of quotient
def gcd(a, b):
    # initialize the list
    remainder_list = []
    quotient_list = []
    # make sure the remainders are in decreasing order
    if a > b:
        remainder_list.append(a)
        remainder_list.append(b)
    else:
        remainder_list.append(b)
        remainder_list.append(a)

    # calculate the current remainder
    current_remainder = remainder_list[0] % remainder_list[1]
    current_quotient = remainder_list[0] // remainder_list[1]

    # append the current remainder and the quotient
    remainder_list.append(current_remainder)
    quotient_list.append(current_quotient)

    # initialize the variable for this while loop
    current_index = 1
    while current_remainder != 0:
        # calculate the current remainder and the quotient
        current_remainder = remainder_list[current_index] % remainder_list[current_index + 1]
        current_quotient = remainder_list[current_index] // remainder_list[current_index + 1]
        # print(current_quotient)     # used in debugging

        # append the current remainder and the quotient
        remainder_list.append(current_remainder)
        quotient_list.append(current_quotient)

        # go to next remainder
        current_index += 1
    # print("The gcd is ", remainder_list[-2])
    # return remainder_list, quotient_list
    return remainder_list[-2]


# define the main function for this assignment
# input is a,b (a is g, b is p)
# output is the inverse or None when gcd is not 1
def extended_euclidean(a, b):

    # call the gcd function to get the remainder_list and quotient_list
    # initialize the list
    remainder_list = []
    quotient_list = []
    # make sure the remainders are in decreasing order
    if a > b:
        remainder_list.append(a)
        remainder_list.append(b)
    else:
        remainder_list.append(b)
        remainder_list.append(a)

    # calculate the current remainder
    current_remainder = remainder_list[0] % remainder_list[1]
    current_quotient = remainder_list[0] // remainder_list[1]

    # append the current remainder and the quotient
    remainder_list.append(current_remainder)
    quotient_list.append(current_quotient)

    # initialize the variable for this while loop
    current_index = 1
    while current_remainder != 0:
        # calculate the current remainder and the quotient
        current_remainder = remainder_list[current_index] % remainder_list[current_index + 1]
        current_quotient = remainder_list[current_index] // remainder_list[current_index + 1]
        # print(current_quotient)     # used in debugging

        # append the current remainder and the quotient
        remainder_list.append(current_remainder)
        quotient_list.append(current_quotient)

        # go to next remainder
        current_index += 1
    # print("The gcd is ", remainder_list[-2])

    gcd_of_ab = remainder_list[-2]

    if gcd_of_ab != 1:
        print("\nWhen g = {} and p = {}, there is no inverse "
              "because the Greatest Common Divisor of them is {}".format(a, b, gcd_of_ab))
        return

# else, the following will be executed
    # initialize the first two values for u_list and v_list
    u_list = [0, 1]
    v_list = [1, 0]

    # for every quotient, we can restore the u and v and remainder
    for index, quotient in enumerate(quotient_list):
        current_u = -quotient * u_list[index + 1] + u_list[index]
        current_v = -quotient * v_list[index + 1] + v_list[index]

        # append the values to the list
        u_list.append(current_u)
        v_list.append(current_v)

        # the first two remainders are the a and b, so the index plus 2
        # print("{} * {} + {} * {} = {}".format(current_u, a, current_v, b, remainder_list[index+2]))


    # the last one is when remainder equals 0
    # and we need to return the Greatest Common Divisor
    # that's the second last one of the lists
    response = u_list[-2]
    if u_list[-2] < 0:
        response = u_list[-2] + b
    return response


def baby_step_giant_step(g, p, h):
    """ this function hopefully will solve the Discrete Log Problem"""
    # 1st Step: calculate the N
    n = int(p ** 0.5) + 1
    # print(n)

    # 2nd Step: Make a list of Baby Steps
    # baby_list = []
    # instead of using a list, why not use a dict to improve efficiency
    baby_dict = {}
    for i in range(n):
        current_baby_step = fastPower(g, i, p)
        # print(current_baby_step)   # check every step
        # baby_list.append(current_baby_step)
        # using dict format
        baby_dict[current_baby_step] = i

    # print("The baby list is:\n", baby_list)   # check the list

    # 3rd Step: Make a list of Giant Steps
    giant_list = []
    for j in range(n):
        g_inverse = extended_euclidean(g, p)
        current_giant_step = (h * fastPower(g_inverse, j*n, p)) % p

        # if current_giant_step in baby_list:
        if current_giant_step in baby_dict:
            # baby_index = baby_list.index(current_giant_step)
            baby_index = baby_dict[current_giant_step]
            # print("The baby index is: ", baby_index)
            giant_index = j
            # print("The giant index is: ", giant_index)
            return baby_index + giant_index * n

        giant_list.append(current_giant_step)

    print("If the script doesn't return, you'll see the giant list:\n", giant_list)


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
