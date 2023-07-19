# Problem link -> https://www.hackerrank.com/challenges/word-order/problem?isFullScreen=true

# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
word_dict = {}
for i in range(n):
    word = input()
    if word not in word_dict:
        word_dict[word] = 1
    else:
        word_dict[word] =  word_dict[word] + 1

print(len(word_dict))
string = ""
for word in word_dict:
    string += str(word_dict[word]) + " "
print(string)
