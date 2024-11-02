"""
input: 9
7 2 5 6 1 3 9 4 8
output: 5 6 3 4 1 2 7 9 8
"""


# we use a 2-way partition to return a sorted array with the elements smaller than the pivot on its left
# and the elements greater than the pivot on its right

def partition2(array):
    pivot = A[0] # the pivot is the first element of the array in the 2-way partition
    left = []
    right = []
    for i in array[1:]:
        if i <= pivot:
            left.append(i) # we simply use a for loop and append the elements to the left list or to the right list
            # by comparing their value with the pivot
        else:
            right.append(i)
    final_arr= left + [pivot] + right # we make the separate lists into a single list
    return final_arr 


n = 9
A = '7 2 5 6 1 3 9 4 8'

A= A.split()
A = [int(num) for num in A]

result = partition2(A)
print(*result)