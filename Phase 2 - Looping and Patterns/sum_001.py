"""
Question - 
1. Print numbers from 1 to 10. 
2. Print all even numbers between 1 and 10. 
3. Print all odd numbers between 1 and 10

"""
try:
    num = int(input("""1.press 1 to print number 1 to 10 .
                       2.Press 2 to print Even number between 1 to 10.
                       3.Press 3 to print Odd Number between 1 to 10
                       4.Press 4 to Exit .\t"""))
    match num :
        case 1 :
            for i in range(1,11):
                print(i)
        case 2 :
            for i in range(2,11,2):
                print(i)
        case 3 :
            for i in range(1,11,2):
                print(i)
        case 4:
            print("Exit")
        case _:
            print("Invalid Choice !")
except ValueError :
    print("Invalid ")












