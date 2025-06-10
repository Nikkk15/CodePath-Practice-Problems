# Problem 4: Two-Pointer Two Sum
# Use the two pointer approach to implement a function two_sum()
# that takes in a sorted list of integers nums and an integer target as parameters
# and returns the indices of the two numbers that add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the indices in any order.

def two_sum(nums, target):

    start = 0
    end = len(nums) - 1

    while start < len(nums)-1:
        while start < end:
            if (nums[start] + nums[end]) == target:
                return [nums.index(nums[start]), nums.index(nums[end])]
            end -= 1
        end = len(nums) - 1
        start += 1
    return -1

nums = [2, 7, 11, 15]
target = 9
print(two_sum(nums, target))

nums = [2, 7, 11, 15]
target = 18
print(two_sum(nums, target))
# Example Output:

# [0, 1]
# [1, 2]