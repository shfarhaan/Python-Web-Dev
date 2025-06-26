# 2. Grading System
# user will input his marks:
# Grade: A, A, B, C......

marks = int(input("Please enter your marks: "))

if marks <= 97 :
    print("A+")
elif 97 < marks <= 90:
    print("A")
elif 89 <= marks <= 85:
    print("A-")
elif 84 <= marks <= 80:
    print("B+")
elif 79 <= marks <= 75:
    print("B")
elif 74 <= marks <= 70:
    print("B-")
elif 69 <= marks <= 65:
    print("C+")

elif 84 <= marks <= 80:
    print("B+")
elif 79 <= marks <= 75:
    print("B")
elif 74 <= marks <= 70:
    print("B-")
elif 69 <= marks <= 65:
    print("C+")
else:
    print("Temp range non-existant!")
    