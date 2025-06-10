# Problem 5: Three Sum
# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] 
# such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

# Notice that the solution set must not contain duplicate triplets.

def three_sum(nums):
    triplets = []
    nums.sort()
    p1 = 0
    p2 = 1
    p3 = 2
    while p1 < len(nums)-2:
        while p2 < len(nums)-1:
            while p3 < len(nums):
                if (nums[p1] + nums[p2] + nums[p3]) == 0 and ([nums[p1], nums[p2], nums[p3]]) not in triplets:
                    triplets.append([nums[p1], nums[p2], nums[p3]])
                p3 += 1
            p2 += 1
            p3 = p2+1
        p1 += 1
        p2 = p1+1
        p3 = p2+1
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