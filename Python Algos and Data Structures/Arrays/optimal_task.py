# Given: Array of non-negative integers that represent hours required for tasks
# Problem: Assign tasks to workers to ensure that time is maximized
# Each worker takes care of 2 tasks

# Solution:
#    - Greedy Approach, pairing longest with shortest
A = [6, 3, 2, 7, 5, 5]

A = sorted(A)

for i in range(len(A)//2):
    print(A[i], A[~i])