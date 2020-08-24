## Accepts a list of numbers as an argument and returns a new list that includes only the even numbers.


number_list = [11, 20,42, 97, 23, 10]  ##  Define a list of numbers for input.
even_list = []  ## Define a new list for the even numbers "even_list".

## Define a function that takes the list as an argument.
def get_evens(list):

    for number in list:  ##  Loop that iterates through the list.

        if number % 2 == 0:  ## Check to see if current number is even.
            even_list.append(number)  ## If its even, append to the new list.

    return even_list

print(get_evens(number_list))



    
        
        

    

