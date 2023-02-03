'''
With a given integral number n, write a program to generate a dictionary that contains (i, i x i)
such that is an integral number between 1 and n (both included). 
and then the program should print the dictionary.Suppose the following input is supplied to the program: 8
Then, the output should be:
{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}
'''

# Using For loop
number = int(input())
simple_dict = {}
for k in range(1, number+1):
    simple_dict[k] = k*k
print(simple_dict)


# Using while loop
simple_dict2 = {}
x = 1
while x <= number:
    simple_dict2[x] = x**2
    x += 1
print(simple_dict2)


# Using dict comprehension
print(result := {k: k**2 for k in range(1, number+1)})


# using
print(dict(enumerate([k*k for k in range(1, number+1)], 1)))
