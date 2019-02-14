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

    # loop the quotient until it reaches p
    current_quotient = 3
    while  current_quotient <= p:
        while p % current_quotient == 0:
            if current_quotient not in num_counts:
                num_counts[current_quotient] = 1
            else:
                num_counts[current_quotient] += 1
            p = p / current_quotient
        current_quotient += 2
    # print(num_counts)
    return num_counts


print("Input your test number:", end="")
test_num = int(input())
print(get_factors(test_num))
