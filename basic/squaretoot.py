import math
import random
number = 144

answer = int(math.sqrt(number))

def sqrt_guess():

    while True:

        guess = int(input(f"The number is {number}, guess the square-root: "))

        if guess == answer:
            print("Correct, you made it!")
            return False
        else:
            print("Wrong, try again!")

sqrt_guess()