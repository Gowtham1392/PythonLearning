class Account:
    def __init__(self, accno, name):
        self.accno = accno
        self.type = name

    def print_accdetails(self):
        pprint(f"Account No: {self.accno} and Type: {self.name}")


class Standard:
    def __init__(self, balance, limit):
        self.balance = balance
        self.limit = limit
        


    def show_details(self):
        print(f"Account balance is {self.balance} and limit is {self.limit}")

class Crypto:
    def __init__(self, balance, limit):
        self.balance = balance
        self.limit = limit


    def show_details(self):
        print(f"Account balance is {self.balance} and limit is {self.limit}")

class Validate:
    def validate_limit(self):
