# Homework:
# 3.Write a function to check for a palindrome string

"""
A palindrome is a word, phrase, or sequence that reads 
the same backward as forward. This function checks if 
a given string is a palindrome. 

"""


def is_palindrome(s):
    """
    Checks if a string is a palindrome.
    """
    # Clean the string: remove spaces and convert to lowercase
    cleaned_string = ''.join(s.split()).lower()
    
    # Check if the cleaned string is equal to its reverse
    return True if cleaned_string == cleaned_string[::-1] else False


string1 = "hello"
print(f"Is '{string1}' a palindrome?  \nAns: {is_palindrome(string1)}")
