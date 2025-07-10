# input("Please input any number from 1 to 7:")

# dict = {1: "Sunday", 2: "Monday", 3: "Tuesday", 4: "Wednesday", 5:"Thursday", 6: "Friday", 7:"Saturday"}

# val = int(input("Please input any number from 1 to 7: "))
# for i, day in enumerate(dict):
#       if val == i:
#          print(f"The day is: {day}")
#       else:
#          print(f"The number was {i} which was {day}")


# # 1. Day in the week

# Take a number from user between(1-7)
# 1: Saturday
# 2: Sunday

val = int(input("Please input any number from 1 to 7: "))

if val == 1:
    print("Sunday")
elif val == 2:
    print("Monday")
elif val == 3:
    print("Tuesday")
elif val == 4:
    print("Wednesday")
elif val == 5:
    print("Thursday")
elif val == 6:
    print("Friday")
elif val == 7:
    print("Saturday")
else:
    print("Please follow the instruction...")
