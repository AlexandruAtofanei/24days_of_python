'''Question:
Write a program, which will find all such numbers between 1000 and 3000 (both included) 
such that each digit of the number is an even number.
The numbers obtained should be printed in a comma-separated sequence on a single line.

Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.
'''

# 1
from functools import reduce
lst = []
for nr in range(1000, 3001):
    if nr % 2 == 0:
        lst.append(str(nr))
    else:
        pass
print(','.join(lst))


# 2
lst = []

for i in range(1000, 3001):
    flag = 1
    for j in str(i):          # every integer number i is converted into string
        if ord(j) % 2 != 0:     # ord returns ASCII value and j is every digit of i
            flag = 0          # flag becomes zero if any odd digit found
    if flag == 1:
        lst.append(str(i))    # i is stored in list as string
print(",".join(lst))


# 3
def check(element):
    # all returns True if all digits i is even in element
    return all(ord(i) % 2 == 0 for i in element)


# creates list of all given numbers with string data type
lst = [str(i) for i in range(1000, 3001)]
# filter removes element from list if check condition fails
lst = list(filter(check, lst))
print(",".join(lst))


# 4
lst = [str(i) for i in range(1000, 3001)]
# using lambda to define function inside filter function
lst = list(filter(lambda i: all(ord(j) % 2 == 0 for j in i), lst))
print(",".join(lst))


# 5
# map() digits of each number with lambda function and check if all() of them even
# str(num) gives us opportunity to iterate through number by map() and join()
print(','.join([str(num) for num in range(1000, 3001)
      if all(map(lambda num: int(num) % 2 == 0, str(num)))]))


# 6
# using reduce to check if the number has only even digits or not
def is_even_and(bool_to_compare, num_as_char):
    return int(num_as_char) % 2 == 0 and bool_to_compare


print(*(i for i in range(1000, 3001) if reduce(is_even_and, str(i), True)), sep=',')
