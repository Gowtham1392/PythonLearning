# Problem link -> https://www.hackerrank.com/challenges/python-mutations/problem?isFullScreen=true

def mutate_string(string, position, character):
    new_str = string[:position] + character + string[position + 1:]
    return new_str

