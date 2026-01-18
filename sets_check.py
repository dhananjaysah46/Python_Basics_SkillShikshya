# my_set = (1, 2, 3, 4, 5)  # This is a tuple, not a set
# print("Original value:", my_set)
# # my_set.remove(3)  # This will raise an AttributeError since tuples do not have a remove method  
# my_set.discard(4)  # This will also raise an AttributeError since tuples do not have a discard method
# print("Updated value:", my_set)

# Nested set comprehension
# nested_set = {(x,y) for x in range(1,3) for y in range(1,3)} # This creates a set
# print(nested_set)

# **IMPORTANT** Frozen sets are immutable and can be used as elements of other sets
# frozen_set = frozenset([1, 2, 3])
# print("Frozen set:", frozen_set)
# frozen_set.add(4)

my_set = {1, 2, 3, 4, 5}  # This is a set
acessed_items = [item for item in my_set]  # Set comprehension to get even numbers
print("Original value:", my_set)
print("Accessed items:", acessed_items)