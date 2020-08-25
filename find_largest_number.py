## Accepts a list of numbers as an argument and returns the largest number on list.
number_list = [10, 4, 35340, -3, 16, 75, 82, 0]


def largest(list):  ## Define function that returns largest number.
    large_number = -9999999999999999  ## Must set intial check number to lowest possible.

## Loop interate trough the list.
    for number in number_list:  ## Check if current number is largeer than last large number (large_number).
        
        if number > large_number:  ## If it is, assign current number to large_number.
        
            large_number = number
    return large_number


print(f'\n{largest(number_list)}\n')