"""
input: 6
6 10 4 5 1 2
Output: 12

"""


a = '6 10 4 5 1 2'

a  = a.split()
a = [int(num) for num in a]
# I used this command to turn a string of numbers into a list of numbers with commas
# so we don't have to do it manually

swaps = 0 # firstly, we initialize the swap count as 0

for i in range (1 , len (a)):
    key = a[i] # key is the numbers in the lists that we need to swap in the correct position
    j = i - 1 # instead, j is the number on the left of key that we compare to key
    while j >= 0 and key < a[j]:
        a[j +1] = a[j] # this means that if key is smaller than the number at index j (on the left), it swaps them
        j -= 1         # we switch of 1 index on the right to keep comparing with the other elements of a
        swaps += 1 # if the steps above happened we update the swap count
        a[j +1] = key 
        
print(swaps)
