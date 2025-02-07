class testClass:
    def getString(self):
        self.userName = input()
    def printString(self):
        print(self.userName.upper())
u = testClass()

u.getString()
u.printString()