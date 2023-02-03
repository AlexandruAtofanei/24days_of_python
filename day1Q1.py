'''
Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5, 
between 2000 and 3200 (both included).The numbers obtained should be printed in a comma-separated sequence on a single line.
'''

# using list comprehension
list = [str(x) for x in range(2000, 3201) if x % 7 == 0 and x % 5 != 0]
print(','.join(list))


# Using for loop, but this ends in ",", to recheck
for number in range(2000, 3201):
    if number % 7 == 0 and number % 5 != 0:
        print(number, end=',')
print('\b')

# using generators and list comprehension
print(*(i for i in range(2000, 3201) if i % 7 == 0 and i % 5 != 0), sep=",")
