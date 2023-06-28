from datetime import datetime
class FirstClass:
    def first_method(self):
        name = input("Enter the name:")
        year_of_birth = int(input("Enter year of birth:"))
        current_year = datetime.now().year
        age = current_year - year_of_birth
        print(f"Age is {age}")


firstClass = FirstClass()
firstClass.first_method()
