import time

# ---------------------------------------

class BSTNode:
    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if self.value:
            if value < self.value:
                if self.left:
                    self.left.insert(value)
                else:
                    self.left = BSTNode(value)
            else:
                if self.right:
                    self.right.insert(value)
                else:
                    self.right = BSTNode(value)
        else:
            self.value = value

    def contains(self, target):
        if self.value:
            if target == self.value:
                return True
            elif target < self.value:
                if self.left:
                    return self.left.contains(target)
            else:
                if self.right:
                    return self.right.contains(target)

        return False

# ---------------------------------------




start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure

# # runtime: 19.012087106704712 seconds
# # complexity: O(n^2) 
# # Replace the nested for loops below with your improvements
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)


# # runtime: 0.2648472785949707 seconds
# # complexity: 
# Worst case: O(n^2)
# Avarage: O(n log n)
# bstree = BSTNode()
# for name in names_1:
#     bstree.insert(name)

# for name in names_2:
#     if bstree.contains(name):
#         duplicates.append(name)

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.

# complexity: O(n)
# runtime: 0.01598978042602539 seconds
names = {}
for name in names_1:
    names[name] = name

for name in names_2:
    if name in names:
        duplicates.append(name)


end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")


