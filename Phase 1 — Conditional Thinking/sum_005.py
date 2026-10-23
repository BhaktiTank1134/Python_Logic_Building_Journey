"Question - "
"Take a character and check if it’s a vowel or consonant."
"Hint - vowel = a,e,i,o,u "
"Consonants = rest all alphabets except vowels ."
"Attempt 1 ="
"""letter = input("Enter Any Single Character to check whether it is VOWEL Or CONSONANT :\t")
vowel = ['a','e','i','o','u','A','E','I','O','U']
if letter in vowel:
    print(f"Your Charachter {letter} is Vowel ")
else :
    print(f"Your Charachter {letter} is Consonant ")"""

"Attempt 2 = Passed "

letter = input("Enter Any Single Character to check whether it is VOWEL Or CONSONANT :\t").lower()
if len(letter) != 1 or not letter.isalpha():
    print("Please enter SINGLE ALPHABETICAL Character ")
elif letter in "a,e,i,o,u":
    print(f"Your Charachter {letter} is Vowel ")
else :
    print(f"Your Charachter {letter} is Consonant ")

"""Notes - 
What new concepts did you learn?
Concept                 	Purpose
len(letter)	                Checks the number of characters
letter.isalpha()	        Checks whether the input contains alphabetic characters
letter.lower()	            Converts uppercase letters to lowercase
letter in "aeiou"	        Checks whether the letter is a vowel
"""