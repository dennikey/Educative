# Given: Array of non-negative digits that represent decimal integer
# Problem: Add one to the integer array

# Solution:
#   - Add 1 to rightmost
#   - Increment from the right to the left

def plus_one(A):
    A[-1] += 1
    for i in range(len(A) - 1, 0, -1):
        if A[i] != 10:
            break
        A[i] = 0
        A[i - 1] += 1

    if A[0] == 10:
        A[0] = 1
        A.append(0)

    return A
