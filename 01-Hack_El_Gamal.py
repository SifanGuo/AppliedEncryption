import Encryption1
import time

def baby_step_giant_step(g, p, h):
    """ this function hopefully will solve the Discrete Log Problem"""
    # 1st Step: calculate the N
    n = int(p ** 0.5) + 1
    # print(n)

    # 2nd Step: Make a list of Baby Steps
    baby_list = []
    for i in range(n):
        current_baby_step = Encryption1.fastPower(g, i, p)
        # print(current_baby_step)   # check every step
        baby_list.append(current_baby_step)

    # print("The baby list is:\n", baby_list)   # check the list

    # 3rd Step: Make a list of Giant Steps
    giant_list = []
    for j in range(n):
        g_inverse = Encryption1.InverseCalculator(g, p)
        current_giant_step = (h * Encryption1.fastPower(g_inverse, j*n, p)) % p

        if current_giant_step in baby_list:
            baby_index = baby_list.index(current_giant_step)
            # print("The baby index is: ", baby_index)
            giant_index = j
            # print("The giant index is: ", giant_index)
            return baby_index + giant_index * n

        giant_list.append(current_giant_step)

    print(giant_list)


def hack_ElGamal(p, g, A, c1, c2):
    """Hopefully, this script will hack El Gamal"""
    a = baby_step_giant_step(g, p, A)
    print("\nHere is the secret key (also known as Alice's private key)", a)
    print("In case we want to add this key to the rainbow table.")
    c1_inverse = Encryption1.InverseCalculator(c1, p)
    decimal_message = (Encryption1.fastPower(c1_inverse, a, p) * c2) % p
    print("The decimal form of the message is ", decimal_message)
    string_message = Encryption1.int2msg(decimal_message)
    return string_message


# Now, the show time
# Read lines from input.txt
input_file_name = "01-Hack_El_Gamal-input.txt"
test_input_file = open(input_file_name, "r")

test_p = int(test_input_file.readline())
test_g = int(test_input_file.readline())
test_A = int(test_input_file.readline())
test_c1 = int(test_input_file.readline())
test_c2 = int(test_input_file.readline())

# close the file
test_input_file.close()

print("We're trying to hack your message!")
start_time = time.process_time()   # get the start cpu time in seconds
print("Current CPU time is {} second(s)".format(start_time))

# call the function
lovely_message = hack_ElGamal(test_p, test_g, test_A, test_c1, test_c2)


end_time = time.process_time()    # get the end cpu time in seconds
print("\nYour message gets hacked. Current CPU time is {} second(s)".format(end_time))

print("The message is: ", lovely_message)
print("It's hacked within {} second(s)!".format(end_time - start_time))
