# Assignment 1 Day-2: A python program to check whether the given string is anagram or not

def are_anagrams(str1, str2):
    # Remove spaces and convert to lowercase for uniformity
    str1_cleaned = str1.lower()
    str2_cleaned = str2.lower()
    
    # Sort the characters of both strings and compare
    return sorted(str1_cleaned) == sorted(str2_cleaned)

print(are_anagrams("Listen", "Silent"))  # True
print(are_anagrams("Hello", "World"))    # False