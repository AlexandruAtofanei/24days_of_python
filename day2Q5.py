"""
Define a class which has at least two methods:
getString: to get a string from console input
printString: to print the string in upper case.
Also please include simple test function to test the class methods.
"""


class IOstring():
    @classmethod
    def getString(self):
        self.i = input()

    @classmethod
    def printString(self):
        self.o = print(self.i.upper())


check = IOstring()
check.getString()
check.printString()
