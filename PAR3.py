"""
INPUT: 9
4 5 6 4 1 2 5 7 4
OUTPUT: 2 1 4 4 4 5 7 6 5
"""
def partition3(array):
    left = []
    equal_pivot = []
    right = []
    for i in  range(0 , len(array)):
        if array[i] < array[0]:
            left.append(array[i])
        elif array[i] == array[0]:
            equal_pivot.append(array[i]) # the only difference with the 2-way partition it's that in this case
            # we have an extra list (equal_pivot) in which we put the elements equal to our selected pivot
        else:
            right.append(array[i])
    final_arr= left + equal_pivot + right
    return final_arr  


A = '4 5 6 4 1 2 5 7 4'

A= A.split()
A = [int(num) for num in A]

result = partition3(A)
print(*result)