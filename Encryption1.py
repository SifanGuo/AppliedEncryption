# This script contains all the scripts from Applied Encryption 1 that you
# will need for Applied Encryption 2
# It would be good to understand how to do these functions by hand,
# but even if you don't, these functions will be all you need to move forward.

####################################################
# BINARY JUGGLING
###################################################

### These first 2 functions are the hyper-optimized pieces of code, and as such
### I do not expect you to be able to intuitively read what they are doing
### nor do I expect that any code you write will be this intricate

# convert binary string into alpha-numeric message
def bin2msg(binary):
    return ''.join(chr(int(binary[i*8:i*8+8],2)) for i in range(len(binary)//8))
# convert alpha-numeric message into a binary string
def msg2bin(message):
    return ''.join(['{0:08b}'.format(ord(i)) for i in message])
# convert binary string into a traditional decimal number
def bin2int(binary):
    return int(binary,2)
# convert traditional number into binary string
def int2bin(integer):
    binString = ''
    while integer:
        if integer % 2 == 1:
            binString = '1' + binString
        else:
            binString = '0' + binString
        integer //= 2
    while len(binString)%8 != 0:
        binString = '0' + binString
    return binString
# using above functions, convert alpha-numeric message into a number
def msg2int(message):
    return bin2int(msg2bin(message))
# using above functions, convert a number into an alpha-numeric message
def int2msg(integer):
    return bin2msg(int2bin(integer))
# Take a binary message and xor it with a binary key for both encryption and decryption
def xorbit(binary, key):
    ciphertext = ''
    for i in range(len(binary)):
        ciphertext = ciphertext + str(int(binary[i])^int(key[i%len(key)]))
    return ciphertext




#################################################
# MATH
#################################################

# Fast Powering Algorithm (Power by Squares)
# I highly recommend learning what this does on a conceptual level before analyzing this code
# This code is taken directly from the textbook. exercise 1.25 at the back of chapter 1
def fastPower(g,x,p):
    a = g
    b = 1
    while x>0:
        if x%2 == 1:
            b = (b*a)%p
        a = (a*a)%p
        x = x//2
    return b

# Euclidean Algorithm for finding greatest common divisor
def gcd(a,b):
    while b:
        a,b = b, a%b
    return a

# uses Fermatt's Little Theorem to calculate the inverse of g (mod p)
# as a reminder: the inverse of g is the number 'h'
# such that g*h = 1 (mod p)
def InverseCalculator(g,p):
    return fastPower(g,p-2,p)










