# d1 = {"fruits": ["apple", "banana"], "Flower": ["rose", "lily"]}
# d2 = {("India", "USA"): "Country", ("New York", "London"): "City"}
# d3 = {"Fruits": "apple", "Flower": "rose", "Fruits": "banana"}    # Duplicate key 'Fruits' overrides the first entry
# print(d3)
# print(d1)
# print(d2)

student_info = {
    "name": "John Doe",
    "age": 21,
    "courses": "Computer Science",
    "graduattion_year": 2023
}

for key in student_info:
    print(f"Keys:", key)

for value in student_info.values():
    print(f"Value: ", value)