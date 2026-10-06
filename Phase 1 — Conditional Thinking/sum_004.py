"""
Question - 
5. Check if a given year is a leap year.
"""

"""
THEORY:
A leap year normally occurs every 4 years.

However, there is a special rule for years that are divisible by 100:
- If a year is divisible by 100, it is NOT a leap year.
- The exception is when the year is also divisible by 400.
  In that case, it IS a leap year.

LEAP YEAR RULE:
1. Divisible by 400  -> Leap Year
2. Divisible by 100  -> Not a Leap Year
3. Divisible by 4    -> Leap Year
4. Otherwise         -> Not a Leap Year

EXAMPLES:
2024 -> Divisible by 4, but not by 100 -> Leap Year
1900 -> Divisible by 100, but not by 400 -> Not a Leap Year
2000 -> Divisible by 400 -> Leap Year
2023 -> Not divisible by 4 -> Not a Leap Year

LOGIC:
First check divisibility by 400.
If not, check divisibility by 100.
If not, check divisibility by 4.
If none of these conditions are satisfied, it is not a leap year.

Is it divisible by 400?
    YES → Leap Year
    NO → Is it divisible by 100?
              YES → Not Leap Year
              NO → Is it divisible by 4?
                        YES → Leap Year
                        NO → Not Leap Year
"""


year = int(input("Enter Year in format(yyyy)-\t"))
if year % 400 == 0:
    print(f"{year} is LEAP YEAR")
elif year % 100 == 0:
    print(f"{year} is not a leap year ")
elif year % 4 == 0:
    print(f"{year} is LEAP YEAR")
else:
    print(f"{year} is not a leap year ")