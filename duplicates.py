# Problem link -> https://www.hackerrank.com/challenges/merge-the-tools/problem?isFullScreen=true

def merge_the_tools(string, k):
    skip = 0
    lst = []
    frm = 0
    to = k
    
    for i in range(int(len(string) / k)):
        unique = ""
        lst = string[frm:to]
        for j in lst:
            if j not in unique:
                unique += j
        print(unique)
        frm = to
        to = to + k
        
        

