# Random Password Generator

import random

lower = 'abcdefghijklmnopqrstuvwxyz'
upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
number = '123456890'
symbol = ')(*&^%$#!{}[]|'

input = int(input("Enter the password number: "))
length = input

arr = lower + upper + number + symbol
result = "".join(random.sample(arr, length))
print(result)