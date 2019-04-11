import Encryption1
import Sifan_tools


def period_finder(N, a):
    r = 1
    while True:
        a_to_r = Encryption1.fastPower(a, r, N)
        if a_to_r == 1:
            return r
        # print("a^r = {}^{} = {}".format(a, r, a_to_r) )
        r += 1


test_N = 8081081
# test_N = 21
#
# flag = True
# while flag:
#     # generate a
#     test_a = Sifan_tools.sifan_random(2, test_N)
#     print("This is the a: ",test_a)
#     # test_a = 2
#     if Encryption1.gcd(test_N, test_a) == 1:
#         test_r = period_finder(test_N, test_a)
#         print("This is the r: ",test_r)
#         if test_r % 2 == 0:
#             print()
#             print("Wow, we find the r: ", test_r)
#             flag = False
#             break
#         else:
#             print("The r here is odd.")
#
#
#

print(period_finder(test_N, 2))




# b = Encryption1.fastPower(test_a, test_r//2, test_N)
# print(b)
# non_trivial_list = []
# non_trivial_list.append(Encryption1.gcd(b + 1, test_N))
# non_trivial_list.append(Encryption1.gcd(b - 1, test_N))
# print(non_trivial_list)
