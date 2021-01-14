# Given: Two sorted arrays 
# Problem: What are the elements that are common to the arrays?

# Solution 1: One-line set function that operates on a list 
# and returns a set object containing elements of the list (doesn't have to be sorted)
# Method intersection is a member of Set class
A = [2, 3, 3, 5, 7, 11]
B = [3, 3, 7, 15, 31]

print(set(A).intersection(B))

# Solution 2: Since the arrays are sorted, you can have two pointers
# that increment if the value is bigger compared to other and
# both increment if the values are the same (intersection)

def intersect_sorted_array(A, B):
    i = 0
    j = 0
    intersection = []

    while i < len(A) and j < len(B):
        if A[i] == B[j]:
            if i == 0 or A[i] != A[i - 1]:
                intersection.append(A[i])
            i += 1
            j += 1
        elif A[i] < B[j]:
            i += 1
        else:
            j += 1
    return intersection

print(intersect_sorted_array(A, B))
