#Problem 3: Remove Duplicates
#Write a function remove_dupes() that accepts a sorted 
# array items, and removes the duplicates in-place 
# such that each element appears only once. 
# Return the length of the modified array. 
# You may not create another array; 
# your implementation must modify the 
# original input array items.

def remove_dupes(items):
    
    slow = 0
    fast = 1

    while fast < len(items):
        if items[slow] == items[fast]:
            items.pop(fast)
        slow += 1
        fast += 1

    return len(items)

items = ["extract of malt", "haycorns", "honey", "thistle", "thistle"]
print(remove_dupes(items))

items = ["extract of malt", "haycorns", "honey", "thistle"]
print(remove_dupes(items))