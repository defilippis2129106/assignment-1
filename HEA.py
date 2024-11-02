"""
Sample Dataset:
5
1 3 5 7 2
Sample Output:
7 5 1 3 2
"""


def max_heap(array):
    heap = [0]
    for element in array:
        heap.append(element)
        index = len(heap) - 1 # Get the index of the newly added element

        while heap[index // 2] < heap[index] and index // 2 > 0: # check if the element is larger than its parent; if so, swap them.
            heap[index], heap[index // 2] = heap[index // 2], heap[index]
            index = index // 2 # puts it at its parent's index (this is the bubble up process to keep the max-heap property)
    return heap[1:] # this is to remove the 0 placeholder we put in the first step


A = '1 3 5 7 2'
A = A.split()
A = [int(num) for num in A]

result = max_heap(A)
print(*result)
