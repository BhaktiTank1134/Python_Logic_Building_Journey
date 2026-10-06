"""
Question-1. Take a number and print whether it’s positive, negative, or zero. 
2. Check if a number is even or odd. 
"""
number = int(input("Enter Any Number --"))
if number == 0:
    print("Your Number is Zero ")
    print("And Your Number Is EVEN ")
elif number >0:
    print("Your Number is Positive")
    if number % 2 == 0 :
        print("And Your Number Is EVEN ")
    else:
        print("And Your Number Is ODD ")
else:
    print("Your Number is Negitive")
    if number % 2 == 0 :
        print("And Your Number Is EVEN ")
    else:
        print("And Your Number Is ODD ")
