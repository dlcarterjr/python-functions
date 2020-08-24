## Converts user input Farenheit temp to Celcius.

## Get Farenheit temp from user.
while True:
    
    ## Error check for a number.
    try:
        temp = float(input("\nEnter Farenheit temp to convert to Celcius: "))
        break
    except ValueError:
        print("\nPlease enter a number.")

## Define function with input as parameter.
def conv_to_celc(temp):
    celc = (temp - 32) * (5/9)  ## Calculate conversion (C = (F - 32) * (5/9)).
    return (celc)  ## Return the value

print(f'\nThe temp in Celcius is {conv_to_celc(temp):.2f} degrees.\n')  ## Print a formatted output string.
