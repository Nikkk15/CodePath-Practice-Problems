# Problem 5: Three Sum
# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] 
# such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

# Notice that the solution set must not contain duplicate triplets.

def three_sum(nums):
    triplets = []
    start = 0
    end2 = len(nums)-1
    end1 = len(nums)-2
    while start < end1:
        if nums[start] != nums[end1] and nums[start] != nums[end2] and nums[end1] != nums[end2] and nums[start] + nums[end1] + nums[end2] == 0:
            triplets.append([nums[start], nums[end1], nums[end2]])
        end1 -= 1
        end2 -= 1
    return triplets
        



nums = [-1, 0, 1, 2, -1, -4]
print(three_sum(nums))

nums = [0, 1, 1]
print(three_sum(nums))

nums = [0, 0, 0]
print(three_sum(nums))
# Example Output:

# [[-1, -1, 2], [-1, 0, 1]]
# []
# [[0, 0, 0]]