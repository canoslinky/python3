# This is a comment
from itertools import permutations

print("Hello, World!")

# Using permutation instead of brute force


def getPermutations(arr):
    return permutations(arr)


number = input("Enter number:")
n = int(number)

arr = [item for item in range(1, n+1)]

# Get all permutations of [1, 2, 3]
perm = getPermutations(arr)

# Print the obtained permutations
for i in list(perm):
    print(i)
