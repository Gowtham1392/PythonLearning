# Problem link -> https://www.hackerrank.com/challenges/nested-list/problem?isFullScreen=true

# Solution

from operator import itemgetter
if __name__ == '__main__':
    finalList = []
    for _ in range(int(input())):
        finalList.append([input(), float(input())])

finalList.sort(key = itemgetter(1))

mark_list = list(set([marks[1] for marks in finalList]))

sorted_mark = sorted(mark_list)

name_list = [names[0] for names in finalList if sorted_mark[1] == names[1]]

print("\n".join(sorted(name_list)))
