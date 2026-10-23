"""
Question -
8.Take a temperature value and print “Cold”, “Warm”, or “Hot” using range conditions.

lets Assume - Temperature Range lies like :
< 15 Degree Celcius = Cold
between 15 and 30 Degree Celcius = warm 
> 30 Degree Celcius = Hot 
"""
"Attempt 1 "
temp = float(input("Enter Temperature :\t"))
if temp >=15 or temp <=30 :
    print("Its Warm")
elif temp > 30 :
    print("Its Hot")
else:
    print("Its Cold")

