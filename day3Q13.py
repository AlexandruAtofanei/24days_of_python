'''
Write a program that accepts a sentence and calculate the number of letters and digits.
Suppose the following input is supplied to the program:
hello world! 123
Then, the output should be:

LETTERS 10
DIGITS 3
Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.
'''


# 1
from functools import reduce
import re
word = input()
letter, digit = 0, 0

for i in word:
    if ('a' <= i and i <= 'z') or ('A' <= i and i <= 'Z'):
        letter += 1
    if '0' <= i and i <= '9':
        digit += 1

print("LETTERS {0}\nDIGITS {1}".format(letter, digit))


# 2
word = input()
letter, digit = 0, 0

for i in word:
    if i.isalpha():  # returns True if alphabet
        letter += 1
    elif i.isnumeric():  # returns True if numeric
        digit += 1
# two different types of formating method is shown in both solution
print(f"LETTERS {letter}\nDIGITS {digit}")


# 3

input_string = input('> ')
print()
counter = {"LETTERS": len(re.findall(
    "[a-zA-Z]", input_string)), "NUMBERS": len(re.findall("[0-9]", input_string))}

print(counter)


# 4
# using reduce for to count
def count_letters_digits(counters, char_to_check):
    counters[0] += char_to_check.isalpha()
    counters[1] += char_to_check.isnumeric()
    return counters


print('LETTERS {0}\nDIGITS {1}'.format(
    *reduce(count_letters_digits, input(), [0, 0])))
