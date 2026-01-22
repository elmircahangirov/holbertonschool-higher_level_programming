#!/usr/bin/python3
import random
number = random.randint(-10, 10)
if number > 0:
    print("This number is positive!")
elif number < 0:
    print("This number is negative!")
else:
    print("This number is zero!")
