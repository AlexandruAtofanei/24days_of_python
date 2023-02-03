'''
Write a program which can compute the factorial of a given numbers.The results should be printed in a comma-separated sequence on a single line.
Suppose the following input is supplied to the program: 8 Then, the output should be:40320
'''

# Using for loop
from functools import reduce

number = int(input())
result = number
for x in range(1, number):
    result = result*x
print(result)


# Using while loop
y = 1
result = number
while y < number:
    result = result * y
    y += 1
print(result)


# Using while loop2
y = 1
result = number
while result:
    y = y * result
    result -= 1
print(y)


# Using lambda
print(factorial := reduce(lambda n1, n2: n1*n2, range(1, number+1)))
