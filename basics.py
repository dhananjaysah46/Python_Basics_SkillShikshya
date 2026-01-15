age = 21   # integer variable
height = 5.8  # float variable
name = "Ram"  # string variable
is_student = True  # boolean variable

#Control Statements
if age>18: 
    print("Adult.")
elif age==18:
    print("just became an adult.")
else:
    print("Minor.")

#For Loop and While Loop
for i in range(5):
    print(f"Number: {i}")

count = 0
while count < 3:
    print(f"Counting: {count}")
    count += 1

# Function Definition
def greet(name):
    return f"Hello, {name}!"

#function call
print(greet(name))  # Output: Hello, Ram!