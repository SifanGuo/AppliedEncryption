For our first Assignment this semester, you will code Shanks algorithm.

The format of this assignment will be nearly identical to the final exercise we did in class this week. I will provide you variables from an Elgamal transmission, and you will crack Bob's message.

Your script should take variable from and input file called input.txt. The variables will be written on individual lines and will be ordered as follows:

line 1: p
line 2: g
line 3: Alice's public key A
line 4: Bob's variable: c1
line 5: Bob's variable: c2

Last semester we would output our final result to output.txt, but this semester you are welcome to simply print your decoded message.





Extra Credit:

Instead of using Fermatt's Little Theorem to calculate the inverse of a number in the above assignment, implement the extended euclidean algorithm detailed in chapter 1 (remark 1.22). The advantage of this method is that it works even when our modulus is not prime, which will be the case as we move closer to RSA. This will also make your work easier when we cover Chinese Remainder Theorem next week.

If you coded this last semester, you are free to re-use your code again here.
