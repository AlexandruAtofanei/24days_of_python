'''
Write a program that calculates and prints the value according to the given formula:
Q = Square root of [(2 _ C _ D)/H]
Following are the fixed values of C and H:
C is 50. H is 30.
D is the variable whose values should be input to your program in a comma-separated sequence.
For example Let us assume the following comma separated input sequence is given to the program:
100,150,180
The output of the program should be:
18,22,24
'''

from math import sqrt


c, h = 50, 30
input_list = input().split(',')
result = []

# Using a for loop
for d in input_list:
    result.append(str(round(sqrt(2*c*int(d)/h))))
print(','.join(result))

# Using list comprehension
result = [str(round(sqrt(2*c*int(d)/h))) for d in input_list]
print(','.join(result))


# Using map and lambda
print(','.join(map(lambda d: str(round(sqrt(2*c*int(d)/h))), input_list)))


# Using generator
print(*((round(sqrt(2*c*int(d)/h))) for d in input_list), sep=',')
