## Takes two inputs (name, subject) and outputs a string using those inputs.


name = input("\nEnter name: ")
subject = input("Enter favorite subject: ")

def madlib(name,subject):  ##  Define a function with two arguments (name, subject).

    ##  Provide default arguments incase inputs are ommitted.
    if name == "":
        name = "John"
    if subject  == "":
        subject = "math"

## Return a string using the two arguments.
    return f'{name}\'s favorite subject is {subject}.'
message = (madlib(name,subject))
print('\n',message,'\n')


