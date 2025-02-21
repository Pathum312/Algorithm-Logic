"""
Description:
    Array is a collection of items of the same variable type that are stored at contiguous memory locations. 
    It is one of the most popular and simple data structures used in programming. 
"""

print("\n### Basic Array Operations ###\n")

# Initializing the numebr list
number_list: list[int] = [1, 2, 3, 4]

print(f"1. Initial Array: {number_list}\n")

# Append 8 to the list
number_list.append(8)
print(f"2. Append 8: {number_list}\n")

# Remove 2 from the list
number_list.remove(2)
print(f"3. Remove 2: {number_list}\n")
