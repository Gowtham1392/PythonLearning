# Problem link -> https://www.hackerrank.com/challenges/text-wrap/problem?isFullScreen=true



def wrap(string, max_width):
    final_string = ""
    start = 0
    end = max_width
    for i in range(int(len(string) / max_width)):
        final_string += string[start:end] + "\n"
        start = end
        end = end + max_width
    final_string += string[start:]
    return final_string

