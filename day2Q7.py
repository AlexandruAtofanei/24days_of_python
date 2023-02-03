'''
_Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional array. 
The element value in the i-th row and j-th column of the array should be i _ j.*
Note: i=0,1.., X-1; j=0,1, Y-1. Suppose the following inputs are given to the program: 3,5
Then, the output of the program should be:
[[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]]
'''

# 1st try
x, y = input().split(',')
x = int(x)
y = int(y)

lst_2nd = [0]*x
for row in range(x):
    lst_2nd[row] = [row] * y
    for col in range(y):
        lst_2nd[row][col] = row*col
print(lst_2nd)


# 2nd try -> not good, need to check
x, y = map(int, input().split(','))
lst_2nd = [[0]*y]*x
for col in range(y):
    for row in range(x):
        # print(row)
        # print(col)
        lst_2nd[row][col] = row*col
print(lst_2nd)


# variant 3
x, y = map(int, input().split(','))
lst_2nd = []
for row in range(x):
    temp = []
    for col in range(y):
        temp.append(row * col)
    lst_2nd.append(temp)
print(lst_2nd)


# Using comprehension
x, y = map(int, input().split(','))
lst = [[row*col for col in range(y)] for row in range(x)]
print(lst)
