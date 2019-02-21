# This script would implement Extended Euclidean Algorithm to solve the inverse of g modulo p


# define the function to read from file
# input is the filename
# output is the number lists
def read_numbers(input_file_name="input.txt"):
    p_list = []
    g_list = []

    # open file
    with open(input_file_name, 'r') as number_inputs:
        # read lines
        first_line = number_inputs.readline()
        second_line = number_inputs.readline()

        # split the lines
        first_line_number_list = first_line.split()
        second_line_number_list = second_line.split()

        # just in case the file is not valid
        if len(first_line_number_list) != len(second_line_number_list):
            print("The input file is not valid!")
            print("There should be the same amount of numbers from these two lines.")
            # in this case, I prefer returning two empty lists
            # instead of returning part of them
            return [], []

        # convert the format from str to int
        for number in first_line_number_list:
            p_list.append(int(number))
        # convert the format from str to int
        for number in second_line_number_list:
            g_list.append(int(number))

    # although the sample input consists of only one value per line
    # I think it's better to return a list
    return p_list, g_list


# define the function to calculate the gcd
# input is the two numbers
# output is two lists, 1st one is the list of remainder, 2nd one is the list of quotient

# define the main function for this assignment
# input is a,b
# output is u, v and gcd(a,b)
def extended_euclidean(a, b):
    # initialize the first two values for u_list and v_list
    u_list = [0, 1]
    v_list = [1, 0]

    # get the remainder_list and quotient_list
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


    # for every quotient, we can restore the u and v and remainder
    for index, quotient in enumerate(quotient_list):
        current_u = -quotient * u_list[index + 1] + u_list[index]
        current_v = -quotient * v_list[index + 1] + v_list[index]

        # append the values to the list
        u_list.append(current_u)
        v_list.append(current_v)

        # the first two remainders are the a and b, so the index plus 2
        print("{} * {} + {} * {} = {}".format(current_u, a, current_v, b, remainder_list[index+2]))

    # the last one is when remainder equals 0
    # and we need to return the Greatest Common Divisor
    # that's the second last one of the lists
    return u_list[-2], v_list[-2], remainder_list[-2]


# used in debugging
# print(gcd(1180, 482))
# p_value_list, g_value_list = read_numbers()
#
# for index, p_value in enumerate(p_value_list):
#     g_value = g_value_list[index]  # the corresponding value
#     # call the function to get the u v and the gcd of the equation
#     # u * g_value + v * p_value = gcd (g_value, p_value )
#     u_solution, v_solution, gcd_of_ab = extended_euclidean(g_value, p_value)
#
#     print("\n\nYour input numbers are {} and {}.".format(g_value, p_value))
#     print("Here is the equation:")
#     print("{} * {} + {} * {} = {}".format(u_solution, g_value, v_solution, p_value, gcd_of_ab))
#     print("The u here is ", u_solution)
#     print("The v here is ", v_solution)
#
#     if gcd_of_ab != 1:
#         print("\nWhen g = {} and p = {}, there is no inverse "
#               "because the Greatest Common Divisor of them is {}".format(g_value, p_value, gcd_of_ab))
#         # print("{} * {} % {} = {}".format(g_value, u_solution, p_value, g_value * u_solution % p_value))
#
#     else:
#         print("The inverse of {} modulo {} is {}".format(g_value, p_value, u_solution))
#         print("{} * {} % {} = {}".format(g_value, u_solution, p_value, g_value*u_solution%p_value))

# P = 1492909219
# Q = 2568337697
# e_value = 2709929475300581585
# mod_value = P*Q


# Here is the test case
e_value = 33
mod_value = 40

# call the function to get the u v and the gcd of the equation
# u * g_value + v * p_value = gcd (g_value, p_value )
u_solution, v_solution, gcd_of_ab = extended_euclidean(e_value, mod_value)

print("\n\nYour input numbers are {} and {}.".format(e_value, mod_value))
print("Here is the equation:")
print("{} * {} + {} * {} = {}".format(u_solution, e_value, v_solution, mod_value, gcd_of_ab))
print("The u here is ", u_solution)
print("The v here is ", v_solution)

if gcd_of_ab != 1:
    print("\nWhen g = {} and p = {}, there is no inverse "
          "because the Greatest Common Divisor of them is {}".format(e_value, mod_value, gcd_of_ab))
    # print("{} * {} % {} = {}".format(g_value, u_solution, p_value, g_value * u_solution % p_value))

else:
    print("The inverse of {} modulo {} is {}".format(e_value, mod_value, u_solution))
    print("{} * {} % {} = {}".format(e_value, u_solution, mod_value, e_value*u_solution%mod_value))
