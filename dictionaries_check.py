# d1 = {"fruits": ["apple", "banana"], "Flower": ["rose", "lily"]}
# d2 = {("India", "USA"): "Country", ("New York", "London"): "City"}
# d3 = {"Fruits": "apple", "Flower": "rose", "Fruits": "banana"}    # Duplicate key 'Fruits' overrides the first entry
# print(d3)
# print(d1)
# print(d2)

# student_info = {
#     "name": "John Doe",
#     "age": 21,
#     "courses": "Computer Science",
#     "graduattion_year": 2023
# }
# all_keys = student_info.values()
# print(all_keys)

# for key in student_info:
#     print(f"Keys:", key)

# for value in student_info.values():
#     print(f"Value: ", value)

# student_info = {
#     "name": "John Doe",
#     "age": 21,
#     "major": "Computer Science",

# }
# all_items = student_info.items()
# print("Items: ",all_items)
# print("Iterating through key-value pairs:")
# for key, value in all_items:
#     print(f"{key}: {value}")

# marks = {
#     "Savita": 90, "imtiaz": 85, "Laxman": 92, "David": 49}
# print("Original Dictionary: \n", marks)
# marks1 = {"Sarad":51, "Mushtaq": 61, "Laxman": 89}
# new_marks = {**marks, **marks1}  #what is this doing? **val = unpacking operator
# print("Marks Dictionary after update: \n", new_marks)

# student_info = {
#     "name": "John Doe",
#     "age": 21}
# major = student_info.setdefault("major", "Computer Science")
# print(student_info)

from collections import defaultdict

d = defaultdict(int)
d["a"] += 1
print(d)

d = defaultdict(list)
d["b"].append(1)
print(d)

def default_value():
    return "N/A"
