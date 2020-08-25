## Accepts a list of numbers as an argument and returns the smallest number on list.
number_list = [10, 4, 35340, -3, 16, 75, 82, 0]


def smallest(list):  ## Define function that returns smallest number.
    small_number = number_list[0]  ## Must set intial check number to first number in list.

## Loop interate trough the list.
    for number in number_list:  ## Check if current number is smaller than last small number (small_number).
        
        if number < small_number:  ## If it is, assign current number to small_number.
        
            small_number = number
    return small_number


print(f'\n{smallest(number_list)}\n')