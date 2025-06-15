# Problem 2: Verifying Authenticity
# Your art gallery has just been shipped a new collection of numbered
# art pieces, and you need to verify their authenticity. The collection
# is considered "authentic" if it is a permutation of an array base[n].

# The base[n] array is defined as [1, 2, ..., n - 1, n, n],
# meaning it is an array of length n + 1 containing the integers
# from 1 to n - 1 exactly once, and the integer n twice. For example,
# base[1] is [1, 1] and base[3] is [1, 2, 3, 3].

# Write a function is_authentic_collection that accepts an array
# of integers art_pieces and returns True if the given array is
# an authentic array, and otherwise returns False.

# Note: A permutation of integers represents an arrangement of these numbers.
# For example [3, 2, 1] and [2, 1, 3] are both permutations of the series of numbers 1, 2, and 3.

def is_authentic_collection(art_pieces):
    lst = sorted(art_pieces)
    for i in range(len(lst)-2):
        if lst[i]+1 == lst[i+1]:
            continue
        else:
            return False
    if lst[-2] != lst[-1]:
        return False
    return True




# Example Usage:

collection1 = [2, 1, 3]
collection2 = [1, 3, 3, 2]
collection3 = [1, 1]

print(is_authentic_collection(collection1))
print(is_authentic_collection(collection2))
print(is_authentic_collection(collection3))
# Example Output:

# False
# Example 1 Explanation: Since the maximum element of the array is 3, the only 
# candidate n for which this array could be a permutation of base[n], is n = 3. 
# However, base[3] has four elements but array collection1 has three. Therefore, 
# it can not be a permutation of base[3] = [1, 2, 3, 3]. So the answer is false.

# True
# Example 2 Explanation:  Since the maximum element of the array is 3, the only 
# candidate n for which this array could be a permutation of base[n], is n = 3. 
# It can be seen that collection2 is a permutation of base[3] = [1, 2, 3, 3] 
# (by swapping the second and fourth elements in nums, we reach base[3]).
#  Therefore, the answer is true.

# True
# Example 3 Explanation; Since the maximum element of the array is 1, 
# the only candidate n for which this array could be a permutation of base[n], 
# is n = 1. It can be seen that collection3 is a ppermutation of base[1] = [1, 1].
# Therefore, the answer is true.
