"""
input: GAGCCTACTAACGGGAT
CATCGTAATGACGGCCT
output: 7
"""

def Hamm(dna1,dna2):
    counter = 0
    for i in range(len(dna1)):
        if dna1[i] != dna2[i]:
            counter += 1
        else:
            counter = counter
    return counter
        
dna3 = 'GAGCCTACTAACGGGAT'
dna4 = 'CATCGTAATGACGGCCT'

result = Hamm(dna3,dna4)
print(result)