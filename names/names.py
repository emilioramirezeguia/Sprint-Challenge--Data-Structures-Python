import time
from binary_search_tree import BSTNode

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure

# # Replace the nested for loops below with your improvements
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)

# create an instance of a binary search tree
bst = BSTNode("Emilio")
# loop the first list of names, insert each name into binary search tree
for name in names_1:
    bst.insert(name)
# loop through second list of names, call contains method on each name
for name in names_2:
    duplicate = bst.contains(name)
    if duplicate is True:
        duplicates.append(name)

end_time = time.time()
print(f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print(f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.

# BINARY SEARCH TREE
# create instance of that tree
# populate binary search tree with first set of names
# loop through the first list, and then call bst insert method on each item
# from that instance, call contains on the second list
# loop through the second list, and then call bst contains on each item
