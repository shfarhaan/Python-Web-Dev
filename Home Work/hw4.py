# 4. Write a program that takes three integers as input a,b,c. Your task is to:
# "All equal" if all the inputs are same, "two equal" if two of them are same, "asceding"
# if a < b < c, "descending" if a > b > c, otherwise print "No pattern"

a = int(input("Please enter a value for a: "))
b = int(input("Please enter a value for b: "))
c = int(input("Please enter a value for c: "))

if a == b == c:
    print("All Equal")
elif a == b or b == c or c == a:
    print("Two Equal")
elif a < b < c: 
    print("Ascending")
elif a > b > c: 
    print("Descending")
else:
    print("No Pattern!")
    
    