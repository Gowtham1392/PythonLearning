class Account:
    def __init__(self, acno, type):
        self.acno = acno
        self.type = type



class Crypto(Account):
    def print(self):
        print(f"Type is {self.type} Account")

class Normal(Account):
    def print(self):
        print(f"Type is {self.type} Account")


cr = Normal(1234, "Normal")
cr.print()