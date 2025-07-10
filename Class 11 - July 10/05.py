def my_sum(*args):
    sum = 0
    
    for digit in args:
        print(digit)
        # sum += int(digit)
        sum = sum + digit
    return sum 

print(my_sum([1,2,3,4,5]))