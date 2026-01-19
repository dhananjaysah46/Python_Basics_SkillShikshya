# tup = ('apple', 'banana', 'cherry', 333, 567, 999)
# print(tup)
# del tup
# print("After deleting tup:")
# print(tup)  # This will raise a NameError since 'tup' has been deleted

# original value
t1 = (34, 14, 95, 40)
new_value = ('green', 'blue', 'red', 'yellow')
part1 = t1[:2]
part2 = t1[2:]
updated_tuple = part1 + new_value + part2
print("Original tuple:", t1)   
print("Updated tuple:", updated_tuple)