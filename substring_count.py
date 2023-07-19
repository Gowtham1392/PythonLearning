#Problem link -> https://www.hackerrank.com/challenges/find-a-string/problem?isFullScreen=true

def count_substring(string, sub_string):
    start_index = 0
    occ = 0
    for i in range(len(string)):
        index = string.find(sub_string,start_index)
        if(index != -1):
            occ = occ + 1
            start_index = index + 1
    return occ

