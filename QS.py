"""
Input:
7
5 -2 4 7 8 -10 11
Output:
-10 -2 4 5 7 8 11
"""

def QuickSort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[len(arr) // 2]  # differently from par and par3 now the pivot is the middle element 
        left = [i for i in arr if i < pivot]  # elements less than pivot
        equal_pivot = [i for i in arr if i == pivot]  # elements equal to pivot
        right = [i for i in arr if i > pivot]  # elements greater than pivot
        return QuickSort(left) + equal_pivot + QuickSort(right)  
    # we concatenate sorted lists so that the final output is in ascending order
                                                                 

# Sample input
n = 7
A = '5 -2 4 7 8 -10 11'
A = A.split()
A = [int(num) for num in A]

result = QuickSort(A)
print(*result)