""" 
input: 4
2 4 10 18
3
-5 11 12

output: -5 2 4 10 11 12 18
"""

def merge(array1, array2):
    result = []
    i, j = 0, 0

    # we merge our arrays by comparing their elements
    while i < len(array1) and j < len(array2):  # we use i and j to track indexes
        if array1[i] <= array2[j]:
            result.append(array1[i])
            i += 1  # we increase i of 1 after appending from array1 
        else:
            result.append(array2[j])
            j += 1  # we increase j of 1 after appending from array2

    # lastly, we need to append any remaining elements from array1 
    while i < len(array1):
        result.append(array1[i])
        i += 1

    # ...or any remaining elements from array2
    while j < len(array2):
        result.append(array2[j])
        j += 1

    return result

# input arrays
a = '2 4 10 18'
a  = a.split()
a = [int(num) for num in a]

b = '-5 11 12'
b = b.split()
b = [int(num) for num in b]

mergedlist = merge(a,b)
print(*mergedlist) 