import Encryption1
import Sifan_tools


def checkans(x, y, p):
    if Encryption1.fastPower(y, 2, p) == Encryption1.fastPower(x, 3, p) + 7:
        print("Yes")


test_x = 55066263022277343669578718895168534326250603453777594175500187360389116729240

test_y = 32670510020758816978083085130507043184471273380659243275938904335757337482424

# test_p = 2**256 - 2**32 - 2**9 - 2**8 - 2**7 - 2**6 - 2**4 - 1
test_p = 115792089237316195423570985008687907853269984665640564039457584007908834671663


test_a = 55179115824979878594564946684576670362812219109178118526265814188406326272077

checkans(test_x, test_y, test_p)


def ecPPaddition(p, x, y):
    slope = ((3 * (x  ** 2)) * Encryption1.InverseCalculator(2 * y, p) ) % p
    # intercept = y - slope * x
    x3 = (Encryption1.fastPower(slope, 2, p) - 2 * x ) % p
    y3 = (slope * (x - x3) - y) % p


    return x3, y3


def ecPQaddition(p, x1, y1, x2, y2):
    if y1 == "infinity":
        return x2, y2
    if y2 == "infinity":
        return x1, y1

    slope = ((y2 - y1) * Encryption1.InverseCalculator(x2 - x1, p) ) % p
    # intercept = y1 - slope * x1
    x3 = (Encryption1.fastPower(slope, 2, p) - x1 - x2) % p
    y3 = (slope * (x1 - x3) - y1 ) % p


    return x3, y3


def fastAdding(p, a, Gx, Gy):
    binary_a = Encryption1.int2bin(a)
    print(type(binary_a))
    print(len(binary_a))

    x_now = Gx
    y_now = Gy

    x_ans = "infinity"
    y_ans = "infinity"
    while a > 0:
        if a % 2 == 1:
            x_ans, y_ans = ecPQaddition(p, x_now, y_now, x_ans, y_ans)
        x_now, y_now = ecPPaddition(p, x_now, y_now)
        a //= 2

    return x_ans, y_ans



agx, agy = fastAdding(test_p, test_a, test_x, test_y)
# print(fastAdding(13, 2, 9, 7))
print(agx, agy)
