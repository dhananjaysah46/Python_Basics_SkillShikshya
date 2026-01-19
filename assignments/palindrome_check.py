# Assignment-1 Day-1: A python program to check whether the given string is palindrome or not

def is_palindrome(value):
    # converting to lowercase for uniformity
    value_check = value.lower()
    # Checking if the string is equal to its reverse
    return value_check == value_check[::-1]  

print(is_palindrome("Madam"))  # True
print(is_palindrome("Hello"))  # False