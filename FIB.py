"""
INPUT: 5 3
OUTPUT: 19
"""

n = 5
k = 3

def FibRabbits(n,k):
    if n <= 2:
        return 1
    else:
        return FibRabbits(n-1, k) + k * FibRabbits(n-2, k) 
    # it repeats over the sequence adding the previous rabbits to the final count
    # the 2nd month there's still just one pair of rabbits (they need a month to reach reproduction-age)
    # then the third month that pair gives birth to 3 pairs
    # the next month to other 3 pairs
    # the fifth month that pair and the 3 pairs of 3rd month (which reached reproduction-age) give birth to a total of 12 pairs
    # so the final count is: 1+3+3+12=19 
    
result = FibRabbits(n,k)
print(result)


        