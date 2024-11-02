"""
input: AAAACCCGGT
output: ACCGGGTTTT
"""


# reverse the string and then take complements

def RevComplement(sequence):
    sequence = sequence[::-1] # needed to reverse the directionality of our starting string
    complements = {"A":"T", "C":"G", "G":"C", "T":"A"}
    # we'll use the dictionary to substitute the nucleotides accordingly in a for loop
    new_sequence = [complements[i] for i in sequence]
    new_sequence =''.join(new_sequence) # cause our output wants a string not a list
    return new_sequence


dna_seq = 'AAAACCCGGT'
result = RevComplement(dna_seq)
print(result)


