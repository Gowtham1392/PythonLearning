from datetime import datetime
from random import randint


class FirstClass:
    # Output practice
    def intro(self):
        name = input("Enter the name:")
        year_of_birth = int(input("Enter year of birth:"))
        current_year = datetime.now().year
        age = current_year - year_of_birth
        print(f"Age is {age}")

    # About Lists
    def lists(self):
        list1 = ["Tokyo", "London", "LA", "Paris", "Zurich"]
        print(list1[-1])
        print(list1[1:])
        print(list1[:3])
        list2 = list1[:]
        print(list2)
        list2[3] = "Chennai"
        print(list2)

    # List practice
    def largest_number(self,list_of_numbers):
        largest_number = list_of_numbers[0]
        for number in list_of_numbers:
            if number > largest_number:
                largest_number = number
        print("largest number on the list", largest_number)


firstClass = FirstClass()
#firstClass.intro()
#firstClass.lists()
size = int(input("Enter the size of the list: "))
list_of_numbers = []
for i in range(size):
    list_of_numbers.append(randint(0, 100))
print("List=> ", list_of_numbers)
firstClass.largest_number(list_of_numbers)
