def merge_sort(list):
    # Only do something when the list has more than one element
    if len(list) > 1:
	# Get middle element
        mid = len(list) // 2
	# Get left side of list
        left = list[:mid]
	# Get right side of list
        right = list[mid:]

	# Sort left and right
        merge_sort(left)
        merge_sort(right)

	# Set "pointers" that point to the smallest array of lists left and right
        l = 0
        r = 0
        i = 0

	# fill list step by step with sorted numbers 
        while l < len(left) and r < len(right):
   	    # check whether the smallest remaining element in left is smaller or bigger than the 
	    # smallest element of right and put the smaller element to list[i]
            if left[l] <= right[r]:
		list[i] = left[l]
                l += 1
            else:
		list[i] = right[r]
                r += 1
            i += 1

	# if r == len(right) was reached, fill the remaining elements of list with left
        while l < len(left):
            list[i] = left[l]
            l += 1
            i += 1

	# if l == len(left) was reached, fill the remaining elements of list with right
        while r < len(right):
            list[i] = right[r]
            r += 1
            i += 1


import matplotlib.pyplot as plt
import numpy as np

# initialize list
my_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
x = np.array(range(len(my_list)))

plt.figure()
plt.bar(x-0.15, my_list, color='red', alpha=0.5, label="unsorted", width=0.3)
mergeSort(my_list)
plt.bar(x+0.15, my_list, color='green', alpha=0.5, label="sorted", width=0.3)
plt.legend()
plt.xlabel("Position within list")
plt.show()
