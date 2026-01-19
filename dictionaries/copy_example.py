# Demonstrating shallow copy of a dictionary
original_dict = {
    "name": "Alice",
    "age": 30,
    "skills": ["Python", "Data Analysis"]
}
shallow_copy = original_dict.copy()
shallow_copy["age"] = 26
shallow_copy["skills"].append("Machine Learning")
print("Original Dictionary:", original_dict)
print("Shallow Copy:", shallow_copy)