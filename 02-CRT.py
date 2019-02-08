import Encryption1
import time


def chinese_remainder(g, p, q, h):
    """Hopefully, I can find the answer."""
    # 1st step: g mod p, g mod q
    p_remainder = g % p
    print("{} % {} = {}".format(g, p, p_remainder))
    q_remainder = g % q
    print("{} % {} = {}".format(g, q, q_remainder))

    # 2st step: reduce the exponent
    p_reduce_exponent = h % (p - 1)
    print("{} % {} = {}".format(h, p - 1, p_reduce_exponent))
    q_reduce_exponent = h % (q - 1)
    print("{} % {} = {}".format(h, q - 1, q_reduce_exponent))

    # 3rd step: we must have small numbers right now, and let's calculate
    ans_p = Encryption1.fastPower(p_remainder, p_reduce_exponent, p)
    print("{} ^ {} mod ({}) = {}".format(p_remainder, p_reduce_exponent, p, ans_p))
    # ans_q = q_remainder ** q_reduce_exponent % q
    ans_q = Encryption1.fastPower(q_remainder, q_reduce_exponent, q)
    print("{} ^ {} mod ({}) = {}".format(q_remainder, q_reduce_exponent, q, ans_q))

    # 4th step: the inverse of them
    p_inverse_mod_q = Encryption1.InverseCalculator(p, q)
    print("P's inverse mod Q is ", p_inverse_mod_q)
    q_inverse_mod_p = Encryption1.InverseCalculator(q, p)
    print("Q's inverse mod P is ", q_inverse_mod_p)

    # 5th step: times inverse and addition
    response = (q * q_inverse_mod_p * ans_p + p * p_inverse_mod_q * ans_q ) % (p * q)

    return response


test_g = 123456789987654321
# test_p = int("259,710,707,236,440,222,310,364,888,187,746,544,221".replace(",", ""))
test_p = 259710707236440222310364888187746544221
# test_q = int("294,079,600,011,598,890,845,685,212,763,117,812,459".replace(",", ""))
test_q = 294079600011598890845685212763117812459
test_h = 1123581321345589144

print("Now, I'm starting calculating the answer using CRT.")
start_time1 = time.process_time()
print("Current CPU time is {}".format(start_time1))
print("The answer is ", chinese_remainder(test_g, test_p, test_q, test_h))
end_time1 = time.process_time()

print("Current CPU time is {}".format(end_time1))
print("The time cost of CRT is ", end_time1 - start_time1)

print("\n\nNow, I'm calculating the answer using fast powering.")
# print("I'm not dead nor sleeping, I'm calculating!")
start_time2 = time.process_time()
print("Current CPU time is {}".format(start_time2))
print("The answer is ", Encryption1.fastPower(test_g, test_h, test_p * test_q))
end_time2 = time.process_time()
print("Current CPU time is {}".format(end_time2))

print("The time cost of fast powering is ", end_time2 - start_time2)

print("Let's give up using normal calculation method")
# start_time3 = time.process_time()
# print(test_g ** test_h % (test_p * test_q))
# end_time3 = time.process_time()
#
# print("The time cost of normal calculation is ", end_time3 - start_time3)
