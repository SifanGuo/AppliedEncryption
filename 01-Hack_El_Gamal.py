import Encryption1


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
    print("Here is the secret key", a)
    c1_inverse = Encryption1.InverseCalculator(c1, p)
    decimal_message = (Encryption1.fastPower(c1_inverse, a, p) * c2) % p
    print("The decimal form of the message is ", decimal_message)
    string_message = Encryption1.int2msg(decimal_message)
    return string_message


test_p = 2147483647
test_g = 7814
test_A = 861678052
test_c1 = 444551209
test_c2 = 1427893323
lovely_message = hack_ElGamal(test_p, test_g, test_A, test_c1, test_c2)
print("Hahahaha, you get hacked!", lovely_message)
