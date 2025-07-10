# 3. Finding temperature
# (-40-0): Too Cold
# (0-25): Cold
# (25-32): Normal
# (32-40): Warm

temp = int(input("Please enter a value for a: "))

if -40 >= temp <= 0:
    print("Too Cold")
elif 0 < temp <= 25:
    print("Cold")
elif 25 < temp <= 32:
    print("Normal")
elif 32 < temp <= 40:
    print("Warm")
else:
    print("Temp range non-existant!")
    