## Accepts a list of strings as an argument and returns the longest string in the list.

string_list = ["daniel", "lynn", "zoe", "seven", "dictionary", "establishment"]


def longest(length):
    longest_len = len(string_list[0])
    index = 0
    string = ''
    for str in string_list:  ## Loop iterate through the list.
        
        current_len = len(str)  ## Get lenght of current string.
    
        if current_len > longest_len:  ## If length of current string > last longest string,
            longest_len = current_len  ## longest string = current string.
            string = string_list[index]  ##Save value of longest string.
        index += 1
    return string  ## Return last longest string.


print(f'\n{longest(string_list)}\n')  ## Print longest string.