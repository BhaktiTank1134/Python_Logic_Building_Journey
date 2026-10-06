"""
Question - 
6. Take two numbers and print the larger one. 
7. Take three numbers and print the largest. 
"""
num1 = int(input("Comparision between 2 number or 3 number ? if 2 -> press 2 or press 3 - \t"))
if num1 == 2 :
    a,b = map(int,input("Enter Number's - ").split())
    if a > b :
        print(f"{a} is greater than {b}")
    elif b>a :
        print(f"{b} is greater than {a}")
    else:
        print("Both are equal ")
else :
    a,b,c = map(int,input("Enter Numbers-\t").split())
    if a > b and a > c:
        print(f"{a} is grater than {b} and {c}")
    elif b > c and b > a :
        print(f"{b} is greater than {a} and {c}")
    elif c > a and c > b:
        print(f"{c} is greater than {a} and {b}")
    else :
        print("All Are equal ")






