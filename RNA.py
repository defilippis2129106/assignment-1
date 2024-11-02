"""
input: GATGGAACTTGACTACGTAAATT
output: GAUGGAACUUGACUACGUAAAUU
"""

char_T = 'T'
char_U = 'U'

def DNA2RNA(input_dna):
    # firstly we define the base case: when the input string is empty
    if input_dna == '':
        return ''
    
    # then we define the recursive case: we process the first character, then call the function on the rest of the string
    char_1 = char_U if input_dna[0] == char_T else input_dna[0]
    return char_1 + DNA2RNA(input_dna[1:])

input_dna = 'GATGGAACTTGACTACGTAAATT'

result = DNA2RNA(input_dna)
print(result)


    
