"""
Question - 
10. Take a character and check whether it’s uppercase, lowercase, a digit, or a special 
characte
"""
"Attempt 1 "
"""letter = input("Enter Single Character Only : \t")
if len(letter) != 1 :
    print("Please Enter Single Character :")
elif letter.isalpha():
    print(f"Your Character {letter} is Alphabet")
elif letter.isnumeric() :
    print(f"Your Character {letter} is Digit")
else :
    print(f"Your Character {letter} is Special Charachter ")
"""

"Attempt 2 = Passed "

letter = input("Enter Single Character Only : \t")
if len(letter) != 1 :
    print("Please Enter Single Character !")
elif letter.isalpha():
    if letter.isupper():
        print(f"Your Character {letter} is UpperCase ")
    else:
        print(f"Your Character {letter} is LowerCase ")
elif letter.isnumeric() :
    print(f"Your Character {letter} is Digit")
else :
    print(f"Your Character {letter} is Special Charachter ")