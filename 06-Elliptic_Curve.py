import Encryption1
import Sifan_tools

"""This script will solve the addition of different Points or some number multiply Points inside Elliptic Curve Y^2 = X^3 + AX + B"""

"""So, I decide to read A & B & p before the definition of functions."""

user_input = input('''Please Enter S/s for ECMultiplyinput, otherwise the script will automatically do Multiplication or Addition based on the input.\n''')

subtraction_flag = False

if user_input in ["S","s"]:
    input_file = open("ECSubtractinput.txt","r")
    subtraction_flag = True
else:
    input_file = open("ECAddinput.txt","r")
    # input_file = open("ECMultiplyinput.txt","r")

A = int(input_file.readline())
B = int(input_file.readline())
p = int(input_file.readline())


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


def fastAdding(a, Gx, Gy):
    binary_a = Encryption1.int2bin(a)
    # print(type(binary_a))
    # print(len(binary_a))

    x_now = Gx
    y_now = Gy

    x_ans = "infinity"
    y_ans = "infinity"
    while a > 0:
        if a % 2 == 1:
            x_ans, y_ans = ecPQaddition(x_now, y_now, x_ans, y_ans)
        x_now, y_now = ecPPaddition(x_now, y_now)
        a //= 2

    return x_ans, y_ans


# here we need to strip the \n in the right
line4 = input_file.readline().rstrip().split(",")

xp, yp = int(line4[0]), int(line4[1])

# here we need to strip the \n in the right
line5 = input_file.readline().rstrip().split(",")

if len(line5) == 1:
    # in this case, we have integer a
    print("The Command is to calculate a * Point P")
    a = int(line5[0])
    print("Here is the answer for {}*({}, {}) = ?\n".format(a, xp, yp))
    print(fastAdding(a, xp, yp))
else:
    # in this case, we have a Point Q to be added
    if subtraction_flag:
        print("\nWe are now doing substraction.")
        # in this case, we have a Point Q
        print("The Command is to calculate Point P - Point Q")
        xq, yq = int(line5[0]), int(line5[1])
        print("Here is the answer for ({}, {}) - ({}, {}) = ?\n".format(xp, yp, xq, yq))
        print(ecPQaddition(xp, yp, xq, -yq))

    else:
        # in this case, we have a Point Q to be substracted
        print("\nThe Command is to calculate Point P + Point Q")
        xq, yq = int(line5[0]), int(line5[1])
        print("Here is the answer for ({}, {}) + ({}, {}) = ?\n".format(xp, yp, xq, yq))
        print(ecPQaddition(xp, yp, xq, yq))

input_file.close()
