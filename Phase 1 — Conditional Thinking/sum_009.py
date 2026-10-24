"""
Question - 
Check if one of two given numbers is a multiple of the other.
Hint — Understand the meaning
A number is a multiple of another number if dividing it by that number leaves a remainder of 0.

For example:
- 10 and 5 → 10 is a multiple of 5.
- 12 and 4 → 12 is a multiple of 4.
- 7 and 3 → Neither is a multiple of the other.

Important edge case: What happens if either number is 0? Dividing by zero causes an error, so think about how you'll handle that.
means -  0 % 10 --gives--> 0
but     10 % 0 --gives--> error 
"""
try :
    num1 , num2 = map(int,input("Enter Two Number to check the multiple :\t").split())
    if num1 == 0 or num2 == 0:
        print("Cannot check multiples when either number is zero")
    elif num1 % num2 == 0:
        print(f"{num1} is multiple of {num2}")
    elif num2 % num1 == 0:
        print(f"{num2} is multiple of {num1}")
    else:
        print("Neither number is multiple of each other !")
   
except ValueError :
    print("Invalid Input ! enter numeric Value only .")

"""
Test Cases 
Input	Expected result
10 5	10 is a multiple of 5
3 12	12 is a multiple of 3
7 4	    Neither is a multiple of the other
0 5	    Cannot check multiples when either number is zero
hello 5	Invalid input
"""














