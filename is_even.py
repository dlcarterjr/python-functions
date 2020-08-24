## Gets a number value from the user and determines if its even.


## Accept user input.
while True:

    try:   
        num = int(input("\nEnter number to check: "))
        break

    except:
        ValueError
        print("\nPlease enter a WHOLE number.")


## Define function with input as parameter.
## Check if number is even.

def check_even(num):
    if num % 2 == 0:  ## If number is even, assign is_even = True.
        is_even = True
    else:
        is_even = False ## Else, assign is_even = False.

    return (is_even)  ## Return is_even vaule.

  ## Print formatted output string.
if (check_even(num)) == True:
     print(f'\n{num} IS an even number.\n')   
    
else:
    print(f'\n{num} IS NOT an even number.\n')


