# Demonstration of method overloading using variable-length arguments in Python
def add(*nums):
    return sum(nums)

result1 = add(10, 25)
result2 = add(10, 25, 35)

print("Result with 2 arguments:", result1)
print("Result with 3 arguments:", result2)

# assigment: using kwargs to achieve method overloading
def greet(**kwargs):
    if 'name' in kwargs and 'age' in kwargs:
        return f"Hello {kwargs['name']}, you are {kwargs['age']} years old!"
    elif 'name' in kwargs:
        return f"Hello {kwargs['name']}, you are {kwargs['age']} years old!"
    elif 'name' in kwargs:
        return f"Hello {kwargs['name']}!"
    else:
        return "Hello there!"
