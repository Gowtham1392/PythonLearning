class TwoDList:
    def print_twod_list(self, matrix):
        matrix[0][1] = 20
        print(matrix)
        for row in matrix:
            for item in row:
                print(item)


matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
list_obj = TwoDList()
list_obj.print_twod_list(matrix)
print("Matrix val after method call",matrix)

