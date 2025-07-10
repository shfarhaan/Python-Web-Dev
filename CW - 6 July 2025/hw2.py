# Homework:
# 2.Write a function to calculate the sum of all even numbers in a list


"""
    This function iterates through a list of numbers, checks if each number is even, and adds it to a running total.

"""

def sum_even_numbers(numbers):
    """
    Calculates the sum of all even numbers in a list.
    """
    total_count = 0
    for number in numbers:
        if number % 2 == 0:  # Check if the number is even
            total_count += number
    return total_count


# test

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_sum = sum_even_numbers(my_list)
print(f"The sum of even numbers in the list {my_list} is: {even_sum}")


