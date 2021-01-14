# Given: Array of non-negative integers like  [3,3,1,0,2,0,1]
# Each number represents the maximum you can advance in the array
# Problem: Is it possible to go from the start to the end of the array based on the values of the array that you are on?

# Greedy Approach
# Take the maximum number of advancements at every index
# This doesn't work as there are exceptions

# Solution
#   - Iterate through each entry in array (A)
#   - Track furthest we can reach from entry (A[i] + i)
#   - If for some i, we don't reach end and that is the furthest we can reach, then we can't reach last index
#   - Otherwise, end is reached

def array_advance(A):
    furthest_reached = 0
    last_idx = len(A) - 1
    i = 0
    while i <= furthest_reached and furthest_reached < last_idx:
        furthest_reached = max(furthest_reached, A[i] + i)
        i += 1
    return furthest_reached >= last_idx

