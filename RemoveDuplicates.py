class RemoveDuplicates:
    def print_unique(self, numbers):
        uniques = []
        for number in numbers:
            if number not in uniques:
                uniques.append(number)
        print(uniques)


    def using_set(self, numbers):
        uniques = set(numbers)
        print(uniques)

numbers = [3, 7, 9, 0, 0, 8, 7, 1, 10, 4, 7]
remove_duplicates = RemoveDuplicates()
#remove_duplicates.print_unique(numbers)
remove_duplicates.using_set(numbers)