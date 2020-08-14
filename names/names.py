import time
from binary_search_tree import BSTNode
start_time = time.time()

f = open('names/names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names/names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()
# making the 2nd list a set to remove duplicates so that
# we don't have to traverse over copies
# names_1 = set(names_1)
names_2 = set(names_2)

# runtime for this seems to be O(n log n)
# because it isn't constant but doesn't exponentially increase
# based on the size of the lists

duplicates = []  # Return the list of duplicates in this data structure

# creating the root node of the tree with the first value of names_1
tree = BSTNode(names_1[0])
# using the insert method to put the rest of the names_1 list to the tree
for name in names_1[1:]:
    tree.insert(name)
# checking the 2nd list with the contains method from the tree to 
for name in names_2:
    if tree.contains(name):
        # if the contains method
        duplicates.append(name)
# Replace the nested for loops below with your improvements
# for name_1 in names_1:
#     if name_1 in names_2:
#         duplicates.append(name_1)

end_time = time.time()

print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")


# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.