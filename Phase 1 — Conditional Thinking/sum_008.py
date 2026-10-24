"""
Question -
3. Take marks (0–100) and print the corresponding grade (A/B/C/D/F).
lets Assume : 0 to <=20 --> Failed (F)
              >20 to <=40 --> (D)
              >40 to <=60 --> (C)
              >60 t0 <=80 --> (B)
              >80 to <=90 --> (A)
              >90 to <=100 --> (A+)

Now marks can be 0 , whole num , Float ---but it cannot be Negative 
"""

try:
    marks = float(input("Enter Students Marks --\t"))

    if marks < 0 or marks > 100 :
        print("Invalid marks ! Enter marks between0 and 100 .")
    elif marks <= 100 and marks > 90 :
        print("Grade A+")
    elif marks <= 90 and marks > 80 :
        print("Grade A")
    elif marks <= 80  and marks > 60 :
        print("Grade B")
    elif marks <= 60  and marks > 40 :
        print("Grade C")
    elif marks <= 40  and marks > 20 :
        print("Grade D")
    else :
        print("Failed !! ")
except ValueError :
    print("Invalid Input ! Please Enter numeric Marks .")