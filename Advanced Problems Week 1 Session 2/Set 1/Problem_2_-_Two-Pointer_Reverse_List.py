#Problem 2: Two-Pointer Reverse List
#Write a function reverse_list() that takes in a list lst
#and returns elements of the list in reverse order.
#The list should be reversed in-place without using list slicing (e.g. lst[::-1]).

#Instead, use the two-pointer approach,
# which is a common technique in which we initialize two variables
# (also called a pointer in this context)
# to track different indices or places in a list or string, 
# then moves the pointers to point at new indices based on certain conditions. 
# In the most common variation of the two-pointer approach, 
# we initialize one variable to point at the beginning of a list
# and a second variable/pointer to point at the end of list.
# We then shift the pointers to move inwards through the list towards each other, 
# until our problem is solved or the pointers reach the opposite ends of the list.

def reverse_list(lst):
    
    start = 0           #pointer 1
    end = len(lst) - 1      #pointer 2

    while start < end:          #As long as pointers don't meet
        lst[start], lst[end] = lst[end], lst[start]         #swap items at two pointer locations at the same time
        
        start += 1                  #move pointers towards each other
        end -+ 1    

    return lst


#Example Usage

lst = ["pooh", "christopher robin", "piglet", "roo", "eeyore"]
print(reverse_list(lst))
#Example Output:

#["eeyore", "roo", "piglet", "christopher robin", "pooh"]