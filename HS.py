"""
input: 9
2 6 7 1 3 5 4 8 9
Output
1 2 3 4 5 6 7 8 9
"""

def Heap(arr, n, i):
    
    largest = i # we initialize largest node as root
    l = 2 * i + 1 # left index
    r = 2 * i + 2  # right index

    # we make a if statement to see if the left child is larger than root 
    # and if so we change the largest with l
    if l < n and arr[l] > arr[largest]:
        largest = l

    # we make a if statement to see if the right child is larger than root
    # and if so we change the largest with r
    if r < n and arr[r] > arr[largest]:
        largest = r

    # if the largest is not root, after we compare them with left and right child...
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # ...we swap their positions in the array

        # now we recursively call this function on the affected sub-tree
        Heap(arr, n, largest)


def HeapSort(arr):
    n = len(arr) 

    # we use this to build the heap (rearrange array)
    for i in range(n // 2 - 1, -1, -1):
        Heap(arr, n, i)

    #  then we extract one by one the element from the array and move the root to the end
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0] 
        Heap(arr, i, 0) # finally we call our previous Heap() function on the heap we created


# Sample Input
n = 9
A = '2 6 7 1 3 5 4 8 9'
A = A.split()
A = [int(num) for num in A]

HeapSort(A)
print(*A)