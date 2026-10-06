"""
Question-
3. Check if a number is divisible by 5. 
4. Check if a number is divisible by both 3 and 5.
"""
num = int(input("Enter Any Number-- \t"))
if num % 3 == 0 and num % 5 == 0 :
    print("Your Number Is Divisible By 3 & 5 both ")
elif num % 3 ==0 :
    print("Your Number is Only Divisible By 3")
elif num % 5 == 0:
     print("Your Number is Only Divisible By 5")
else :
    print(" Tera Number kisise bhi divisible Nhi hai ")

