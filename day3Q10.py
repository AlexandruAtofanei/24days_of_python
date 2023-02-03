'''
Write a program that accepts a sequence of whitespace separated words as input 
and prints the words after removing all duplicate words and sorting them alphanumerically.
Suppose the following input is supplied to the program:
hello world and practice makes perfect and hello world again
Then, the output should be:
again and hello makes perfect practice world
Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.We use set container to remove duplicated data automatically and then use sorted() to sort the data.
'''
# 1
inp = set(input().split())
print(' '.join(sorted(inp)))

# 2
word = input().split()

for i in word:
    # count function returns total repeatation of an element that is send as argument
    if word.count(i) > 1:
        word.remove(i)     # removes exactly one element per call

word.sort()
print(" ".join(word))


# 3
word = input().split()
# removal operation with comprehension method
[word.remove(i) for i in word if word.count(i) > 1]
word.sort()
print(" ".join(word))

# 4
# input string splits -> converting into set() to store unique
#  element -> converting into list to be able to apply sort
word = sorted(list(set(input().split())))
print(" ".join(word))


# 5
inp_string = input("Enter string: ").split()
out_string = []
for words in inp_string:
    if words not in out_string:
        out_string.append(words)
print(" ".join(sorted(out_string)))
