"""
input: 11
2 36 5 21 8 13 11 20 5 4 1
8
output: 13
"""
def Median(A, k):
    A = sorted(A) # firstly we sort the given array into ascending order
    result = '' # we initialize an empty string into which we store our result
    result = A[k -1] # now we simply extract the number at our given position, remembering that the positions start from 
    # 0 so we need to put k-1 to find the right position
    return result

        
n = 11
A = '2 36 5 21 8 13 11 20 5 4 1'
A= A.split()
A = [int(num) for num in A]

k = 8

result = Median(A, k)
print(result)
