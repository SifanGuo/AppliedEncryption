import Encryption1

"""This script will solve the addition of different Points or some number multiply Points inside Elliptic Curve Y^2 = X^3 + AX + B"""

"""So, I decide to read A & B & p before the definition of functions."""


file_input = open("ECElGamalinput.txt", "r")

A = int(file_input.readline())
B = int(file_input.readline())
p = int(file_input.readline())


G = file_input.readline().rstrip().split(",")
# print(G)
xG = int(G[0])
yG = int(G[1])

# print(xG,yG)

C1 = file_input.readline().rstrip().split(",")

xC1 = int(C1[0])
yC1 = int(C1[1])


C2 = file_input.readline().rstrip().split(",")

xC2 = int(C2[0])
yC2 = int(C2[1])

a = int(file_input.readline())


def ecPPaddition(x, y):
    # The cubic function here is y=X^3 + A*X^2 + B
    slope = ((3 * (x  ** 2) + A) * Encryption1.InverseCalculator(2 * y, p) ) % p
    # intercept = y - slope * x
    x3 = (Encryption1.fastPower(slope, 2, p) - 2 * x ) % p
    y3 = (slope * (x - x3) - y) % p
    if y3 == 0:
        y3 = p

    return x3, y3


def ecPQaddition(x1, y1, x2, y2):
    if y1 == "infinity":
        return x2, y2
    if y2 == "infinity":
        return x1, y1
    if x2 == x1 and y1 != y2:
        return "N.A.", "infinity"
    slope = ((y2 - y1) * Encryption1.InverseCalculator(x2 - x1, p) ) % p
    # intercept = y1 - slope * x1
    x3 = (Encryption1.fastPower(slope, 2, p) - x1 - x2) % p
    y3 = (slope * (x1 - x3) - y1 ) % p
    if y3 == 0:
        y3 = p

    return x3, y3


def fastAdding(a, xG, yG):
    binary_a = Encryption1.int2bin(a)
    # print(type(binary_a))
    # print(len(binary_a))

    x_now = xG
    y_now = yG

    x_ans = "infinity"
    y_ans = "infinity"
    while a > 0:
        if a % 2 == 1:
            x_ans, y_ans = ecPQaddition(x_now, y_now, x_ans, y_ans)
        x_now, y_now = ecPPaddition(x_now, y_now)
        a //= 2

    return x_ans, y_ans


def ElGamal_Alice_generate():
    """This function use the a input in the beginning"""
    xQa, yQa = fastAdding(a, xG, yG)
    print(xQa, yQa)
    return xQa, yQa


def ElGamal_Bob(xQa, yQa, xM, yM):
    """This function will calculate the C1 and C2"""
    xC1, yC1 = fastAdding(k, xG, yG)
    xkQa, ykQa = fastAdding(k, xQa, yQa)
    xC2, yC2 = ecPQaddition(xkQa, ykQa, xM, yM)
    return [(xC1, yC1), (xC2, yC2)]


def ElGamal_Alice_decrypt(xC1, yC1, xC2, yC2):
    """This function will decrypt the message"""
    x_aC1, y_aC1 = fastAdding(a, xC1, yC1)

    """Using (x_aC1, -y_aC1) to do the substraction"""
    xM, yM = ecPQaddition(xC2, yC2, x_aC1, -y_aC1)
    message = Encryption1.int2msg(xM)
    # print(message)
    return message


message = ElGamal_Alice_decrypt(xC1, yC1, xC2, yC2)
print(message)
