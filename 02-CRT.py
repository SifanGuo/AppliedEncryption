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


# test_g = 123456789987654321
# # test_p = int("259,710,707,236,440,222,310,364,888,187,746,544,221".replace(",", ""))
# test_p = 259710707236440222310364888187746544221
# # test_q = int("294,079,600,011,598,890,845,685,212,763,117,812,459".replace(",", ""))
# test_q = 294079600011598890845685212763117812459
# test_h = 1123581321345589144

# This is the other test case
test_g = 123456789987654321132435324653465346523451234123498765432113243532465346534652345123412349876543211324353246534653465234512341234987654321132435324653465346523451234123409218980194941195591504909210950881275246551
# test_p = int("259,710,707,236,440,222,310,364,888,187,746,544,221".replace(",", ""))
test_p = 32317006071311007300714876688669951960444102669715484032130345427524655138867890893197201411522913463688717960921898019494119559150490921095088152386448283120630877367300996091750197750389652106796057638384067568276792218642619756161838094338476170470581645852036305042887575891541065808607552399123930385521914333389668342420684974786564569494856176035326322058077805659331026192708460314150258592864177116725943603718461857357598351152301645904403697613233287231227125684710820209725157101726931323469678542580656697935045997268352998638215525166389647960126939249806625440700685819469589938384356951833568218188663
# test_q = int("294,079,600,011,598,890,845,685,212,763,117,812,459".replace(",", ""))
test_q = 32317006071311007300714876688669951960444102669715484032130345427524655138867890893197201411522913463688717960921898019494119559150490921095088152386448283120630877367300996091750197750389652106796057638384067568276792218642619756161838094338476170470581645852036305042887575891541065808607552399123930385521914333389668342420684974786564569494856176035326322058077805659331026192708460314150258592864177116725943603718461857357598351152334063994785580370721665417662212881203104945914551140008147396357886767669820042828793708588252247031092071155540224751031064253209884099238184688246467489498721336450133889385773
test_h = 11235813213455891442130345427524655138867890893197201411522913463688717960921898019494119559150490921095088127524655138867890893197201411522913463688717960921898019494119559150490921095088152752465513886789089319720141152291346368871796092189801949411955915049092109508815852036305042887575891541065852036305042887575891541065852036305042887575891541065852036305042887575891541065

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
