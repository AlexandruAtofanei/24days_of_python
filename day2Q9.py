'''
Write a program that accepts sequence of lines as input and prints the lines after making all characters in the sentence capitalized.
Suppose the following input is supplied to the program:
Hello world
Practice makes perfect

Then, the output should be:
HELLO WORLD
PRACTICE MAKES PERFECT
'''
# 1
lst = []
while True:
    inp = input()
    if len(inp) == 0:
        break
    lst.append(inp)
for element in lst:
    print(element.upper())

# 2


def user_input():
    while True:
        s = input()
        if not s:
            return
        yield s


for line in map(str.upper, user_input()):
    print(line)


# 3
def inputs():
    while True:
        string = input()
        if not string:
            return
        yield string


print(*(line.upper() for line in inputs()), sep='\n')
