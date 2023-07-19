# Problem link -> https://www.hackerrank.com/challenges/swap-case/problem?isFullScreen=true

def swap_case(s):
    final_string = ""
    for char in s:
        if char.isupper():
            final_string += char.lower()
        else:
            final_string += char.upper()
    return final_string

