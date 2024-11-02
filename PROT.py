"""
input: AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA
output: MAMAPRTEINSTRING
"""

codon_table = {
    'UUU': 'F', 'UUC': 'F',
    'UUA': 'L', 'UUG': 'L',
    'CUU': 'L', 'CUC': 'L', 'CUA': 'L', 'CUG': 'L',
    'AUU': 'I', 'AUC': 'I', 'AUA': 'I',
    'AUG': 'M',
    'GUU': 'V', 'GUC': 'V', 'GUA': 'V', 'GUG': 'V',
    
    'UCU': 'S', 'UCC': 'S', 'UCA': 'S', 'UCG': 'S',
    'CCU': 'P', 'CCC': 'P', 'CCA': 'P', 'CCG': 'P',
    'ACU': 'T', 'ACC': 'T', 'ACA': 'T', 'ACG': 'T',
    'GCU': 'A', 'GCC': 'A', 'GCA': 'A', 'GCG': 'A',
    
    'UAU': 'Y', 'UAC': 'Y',
    'CAU': 'H', 'CAC': 'H',
    'AAU': 'N', 'AAC': 'N',
    'GAU': 'D', 'GAC': 'D',
    
    'UAA': '', 'UAG': '', 'UGA': '',
    'CAA': 'Q', 'CAG': 'Q',
    'AAA': 'K', 'AAG': 'K',
    'GAA': 'E', 'GAG': 'E',
    
    'UGU': 'C', 'UGC': 'C',
    'CGU': 'R', 'CGC': 'R', 'CGA': 'R', 'CGG': 'R',
    'AGU': 'S', 'AGC': 'S',
    'GGU': 'G', 'GGC': 'G', 'GGA': 'G', 'GGG': 'G',
    
    'UGG': 'W', 'AGA': 'R', 'AGG': 'R'
}


rna = 'AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA'
def ProtTrans(rna):
    codons = [rna[i:i+3] for i in range(0, len(rna), 3)]
    proteins = [codon_table[i] for i in codons]
    proteins =''.join(proteins)
    return proteins

result = ProtTrans(rna)
print(result)

