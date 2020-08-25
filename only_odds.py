## Accepts a list of numbers as an argument and returns a new list that includes only the odd numbers.



number_list = [11, 20,42, 97, 23, 10]  ##  Define a list of numbers for input.
odd_list = []  ## Define a new list for the even numbers "odd_list".

## Define a function that takes the list as an argument.
def get_odds(list):

    for number in list:  ##  Loop that iterates through the list.

        if number % 2 != 0:  ## Check to see if current number is even.
            odd_list.append(number)  ## If its even, append to the new list.

    return odd_list

print(f'\n{get_odds(number_list)}\n')
