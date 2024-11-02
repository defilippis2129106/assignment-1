"""

Input: AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC
Output: 20 12 17 21

"""

def countNucleotides(input_dna):
    amount_A = 0
    amount_C = 0
    amount_G = 0
    amount_T = 0
    for character in input_dna:
        if character == 'A':
            amount_A +=1
        elif character == 'C':
            amount_C += 1
        elif character == 'G':
            amount_G += 1
        else:
            amount_T += 1
    return amount_A, amount_C, amount_G, amount_T

input_dna = 'AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC'

result = countNucleotides(input_dna)
print(*result)