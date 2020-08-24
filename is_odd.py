## Accepts a number from the user and determines if it odd.



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

    return not (is_even)  ## Return's the opposite is_even value.

  ## Print formatted output string.
if (check_even(num)) == True:
     print(f'\n{num} IS an odd number.\n')   
    
else:
    print(f'\n{num} IS NOT an odd number.\n')