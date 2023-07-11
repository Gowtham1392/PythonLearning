class TryExcept:
    def validate_input(self):
        try:
            age = int(input("Enter the age: "))
            income = 10000
            print(income/age)
        except ValueError:
            print("Age should be a number")
        except ZeroDivisionError:
            print("Age cannot be 0")

obj = TryExcept()
obj.validate_input()







