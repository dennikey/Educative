# Given: Array of integers and sum number
# Problem: Return True or False based on if the two numbers in the array adds up to a target
# Assume that there is exactly one solution

# Time: O(n^2) and Space: O(1)
def two_sum_brute_force(A, target):
    for i in range(len(A)-1):
        for j in range(i+1, len(A)):
            if A[i] + A[j] == target:
                print(A[i], A[j])
                return True
    return False

# Hash table to keep track of numbers (key: sum - number, value: number) so you can directly match the next numbers with the keys
# Time: O(n) and Space: O(n)
def two_sum_hash_table(A, target):
    ht = dict()
    for i in range(len(A)):
        if A[i] in ht:
            print(ht[A[i]], A[i])
            return True
        else:
            ht[target - A[i]] = A[i]
    return False

# Two pointers to move either one depending if the sum is too big or small
# Time: O(n) and Space: O(1)
# Must be in increasing order
def two_sum(A, target):
    i = 0
    j = len(A) - 1
    while i < j:
        if A[i] + A[j] == target:
            print(A[i], A[j])
            return True
        elif A[i] + A[j] < target:
            i += 1
        else:
            j -= 1
    return False