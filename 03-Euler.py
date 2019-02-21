import Sifan_tools

def get_factors(p):
    """input is a number.
    output is a dict showing the primes and their powers"""
    # using a dict to store the powers of every prime number
    num_counts = {}
    if p % 2 == 0:
        num_counts[2] = 0
    while p % 2 == 0:
        num_counts[2] += 1
        p = p / 2

    # loop the quotient until it reaches the square root of p
    current_quotient = 3
    while  current_quotient <= p ** 0.5:
        while p % current_quotient == 0:
            current_remainder = p // current_quotient
            if current_remainder not in num_counts:
                num_counts[current_remainder] = 1
            else:
                num_counts[current_remainder] += 1

            if current_quotient not in num_counts:
                num_counts[current_quotient] = 1
            else:
                num_counts[current_quotient] += 1
            p = p / current_quotient
        current_quotient += 2
    # print(num_counts)
    return num_counts



def euler(p, q):
    g = Sifan_tools.gcd(p - 1, q - 1)
    # print(g)
    pq = p * q
    product_over_g = (p - 1) * (q - 1) // g
    print("This is the answer", product_over_g)
    print("But if you're not sure, I can calculate using fastPower.")
    for a in range(2,10):

        print("{} ^ {} = {} mod {}".format(a, product_over_g, Sifan_tools.fastPower(2, product_over_g, pq), pq))


# test_p = int(input())
# test_q = int(input())

# test_pq = int(input())
test_pq = 2754056308062191369829499027839080282032904501335240494863011176478816681562817959929612699397380172288278842183715230695899883935507881086649976607452679
# forget it, the large PQ is not designed to be breaked
factors_dict = get_factors(850)
print(factors_dict)
# for factor, count in factors_dict.items():
#     print(factor)
#     print()
# euler(test_p, test_q)
