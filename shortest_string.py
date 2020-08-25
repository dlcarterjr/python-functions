## Accepts a list of strings as an argument and returns the shortest string in the list.

string_list = ["daniel", "lynn", "zoe", "seven", "dictionary", "establishment"]


def shortest(length):
    shortest_len = len(string_list[0])
    index = 0
    string = ''
    for str in string_list:  ## Loop iterate through the list.
        
        current_len = len(str)  ## Get lenght of current string.
    
        if current_len < shortest_len:  ## If length of current string < last smallest string,
            shortest_len = current_len  ## last smallest string = current string.
            string = string_list[index]  ## Save value of shortest string.
        index += 1
    return string  ## Return last smallest string.


print(f'\n{shortest(string_list)}\n')  ## Print smallest string.