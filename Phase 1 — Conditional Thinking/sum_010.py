"""
Question - 
Take a day number (1–7) and print the corresponding day name.

hint - We'll assume Monday = 1 and Sunday = 7.

match case syntax -> 
match variable:
    case value1:
        # Code to execute
    case value2:
        # Code to execute
    case _:
        # Default case

match — checks the value of a variable.
case — matches a specific value.
_ — the default case if nothing else matches.
"""
try :
    day = int(input("Enter Day Number (1-7):\t "))
    match day:
        case 1:
            print("Monday")
        case 2:
            print("Tuesday")
        case 3:
            print("Wednesday")
        case 4:
            print("Thursday")
        case 5:
            print("Friday")
        case 6:
            print("Saturday")
        case 7:
            print("Sunday")
        case _:
            print("invalid day number !")
except ValueError:
    print("Enter Numeric Value Only !!")








