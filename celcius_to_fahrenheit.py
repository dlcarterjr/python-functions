

## Get celcius temp from user.
while True:
    
    ## Error check for number.
    try:
        temp = float(input("\nEnter Celcius temp to convert to Farenheit: "))
        break
    except ValueError:
        print("Please enter a number.")

## Define function with input as parameter.
def conv_to_farh(temp):
    farh = (temp * (9/5)) + 32  ## Calculate conversion (F = (C * 9/5) + 32).
    return (farh)  ## Return the value

print(f'\nThe temp in Farenheit is {conv_to_farh(temp)} degrees.\n')  ## Print a formatted output string.






