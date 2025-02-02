class puts:
    def __init__(self):
        self.inp=""
    def getstring(self):
        self.inp = input("Enter a string: ")
    def printstring(self):
        print(self.inp.upper())

mystring = puts()

mystring.getstring()

mystring.printstring()