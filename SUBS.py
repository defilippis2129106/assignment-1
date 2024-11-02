
"""
INPUT:
dna = 'GATATATGCATATACTT'
motif = 'ATAT'
OUTPUT:
2 4 10
"""

def MotifPosition(dna, motif):
    posit= [] 
    motif_length = len(motif)

    for char in range(len(dna) - motif_length + 1):
        if dna[char:char + motif_length] == motif:
            posit.append(char + 1)    
            
    return posit


seq = 'GATATATGCATATACTT'
motif1 = 'ATAT'

result = MotifPosition(seq, motif1)
print(*result) # I used a unpacking operator to not have a list as our final output but just the numbers