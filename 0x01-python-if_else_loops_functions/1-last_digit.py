#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
digit = number % 10
if number < 0:
    digit = (number * -1) % 10
    digit = digit * -1
if digit > 5:
    str = "and is greater than 5 "
elif digit <= 6 and digit != 0:
    str = "and is less than 6 and not 0"
elif digit = 0:
    str = "and is 0"
print(f"last digit of {number} is {digit} {str}")
