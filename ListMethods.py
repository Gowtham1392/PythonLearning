class ListMethods:
    def append_number(self, numbers):
        numbers.append(12)
        print(numbers)
        print(numbers.count(7))
        numbers.sort()
        print("After sorting->",numbers)


    def insert_number(self, numbers):
        numbers.insert(0,20)
        print(numbers)
        numbers.reverse()
        print("After reversing->", numbers)


    def remove_number(self, numbers):
        numbers.remove(1)
        print(numbers)

numbers = [3, 4, 7, 10, 1, 6, 7]
list_object = ListMethods()
list_object.append_number(numbers)
list_object.insert_number(numbers)
list_object.remove_number(numbers)


