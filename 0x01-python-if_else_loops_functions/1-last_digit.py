#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    lastdigit = number % -10
else:
    lastdigit = number % 10
message = "Last digit of "
if(lastdigit > 5):
    print("{} {} is {} and is greater than 5".format(message, number, lastdigit))
elif(lastdigit == 0):
    print("{} {} is {} and is 0".format(message, number, lastdigit))
else:
    print("{} {} is {} and is less than 6 and not 0".format(message, number, lastdigit))
