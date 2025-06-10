# Problem 6: Merge Intervals
# Write a function merge_intervals() that accepts an array of intervals
# where intervals[i] = [starti, endi], merge all overlapping intervals,
# and return an array of the non-overlapping intervals that cover all the intervals in the input.


#1-keep track of last element of current list within the bigger list
#2-keep track of the first element of next list withing bigger list
#3-if first element of next list < last element of previous list; add together into one list
#4-keep doing for next list witihin bigger list
#5-if the first element of next list < than last element of last list then remove all elements

def merge_intervals(intervals):
    new_intervals = []
    for i in range(len(intervals)-1):
        if intervals[i][-1] > intervals[i+1][0]:
            new_intervals.append(intervals[i] + intervals[i+1])
            new_intervals[i].pop(1)
            new_intervals[i].pop(1)
        else:
            new_intervals.append(intervals[i+1])
    print(new_intervals)
        
#Example Usage

intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
merge_intervals(intervals)

intervals = [[1, 4], [4, 5]]
merge_intervals(intervals)
            
            
#Example Output:

#[[1, 6], [8, 10], [15, 18]]
#[[1, 5]]