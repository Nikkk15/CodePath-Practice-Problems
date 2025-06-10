#Problem 4: Sort Array by Parity
#Given an integer array nums, write a function sort_by_parity()
# that moves all the even integers at the beginning of the array followed by all the odd integers.

#Return any array that satisfies this condition.

def sort_by_parity(nums):
    new_lst = []
    for num in nums:
        if num % 2 == 0:
            new_lst.append(num)
    for num in nums:
        if num % 2 == 1:
            new_lst.append(num)
    return new_lst

#Example Usage

nums = [3, 1, 2, 4]
print(sort_by_parity(nums))

nums = [0]
print(sort_by_parity(nums))
#Example Output:

#[2, 4, 3, 1]
#[0]