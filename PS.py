'''
input: 10
4 -6 7 8 -9 100 12 13 56 17
3
Output
-9 -6 4
'''

def PartialSort(arr, k):
    # we sort the array as we did in the Median exercise
    sorted_array = sorted(arr)
    # we return the k smallest elements by basically extracting the elements from 0 to k
    return sorted_array[:k]

# Sample Input
n = 10
A = '4 -6 7 8 -9 100 12 13 56 17'
k = 3

A = A.split()
A = [int(num) for num in A]

# Get k smallest elements using sorting
result = PartialSort(A, k)

# Output the result
print(*result)