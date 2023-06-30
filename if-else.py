# problem link -> https://www.hackerrank.com/challenges/py-if-else/problem?isFullScreen=true

# Solution

N = int(input())

if N % 2 == 0:
    if N > 2 and N < 5:
        print("Not Weird")
    elif N >= 6 and N <= 20:
        print("Weird")
    elif N > 20:
        print("Not Weird")
else:
    print("Weird")
