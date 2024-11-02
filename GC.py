""" input: >Rosalind_6404
CCTGCGGAAGATCGGCACTAGAATAGCCAGAACCGTTTCTCTGAGGCTTCCGGCCTTCCC
TCCCACTAATAATTCTGAGG
>Rosalind_5959
CCATCGGTAGCGCATCCTTAGTCCAATTAAGTCCCTATCCAGGCGCTCCGCCGAAGGTCT
ATATCCATTTGTCAGCAGACACGC
>Rosalind_0808
CCACCCTCGTGGTATGGCTAGGCATTCAGGAACCGGAGAACGCTTCAGACCAGCCCGGAC
TGGGAACCTGCGGGCAGTAGGTGGAAT

output:
Rosalind_0808
60.919540
"""

def GCContent(dna_seq):
    gc_bases = sum(1 for base in dna_seq if base in "GC")  # I used this to count the G and C bases
    gc_percentage = (gc_bases / len(dna_seq)) * 100
    return gc_percentage

def parser(fasta_data):
    dict = {}
    seq_id = None
    sequence_list = []

    for line in fasta_data.strip().splitlines():
        line = line.strip()
        if line.startswith('>'):
            if seq_id:  # If we have an active sequence with ID, this stores it in the dictionary
                dict[seq_id] = ''.join(sequence_list)
            seq_id = line[1:].strip()  # we want to extract the sequence ID without '>'
            sequence_list = []  # we reset the sequence list for the next sequence
        else:
            sequence_list.append(line)  # we collect the sequence parts into a list

    if seq_id:  # lastly, we store the last sequence after the loop ends
        dict[seq_id] = ''.join(sequence_list)

    return dict

def Max_GCContent(fasta_data):
    sequences = parser(fasta_data)
    max_id = None
    max_percentage = 0.0

    for seq_id, sequence in sequences.items():
        GC_Content = GCContent(sequence)
        if GC_Content > max_percentage:
            max_percentage = GC_Content
            max_id = seq_id

    return max_id, max_percentage

if __name__ == "__main__":
    # Sample input in FASTA format
    sample_input = """>Rosalind_6404
CCTGCGGAAGATCGGCACTAGAATAGCCAGAACCGTTTCTCTGAGGCTTCCGGCCTTCCC
TCCCACTAATAATTCTGAGG
>Rosalind_5959
CCATCGGTAGCGCATCCTTAGTCCAATTAAGTCCCTATCCAGGCGCTCCGCCGAAGGTCT
ATATCCATTTGTCAGCAGACACGC
>Rosalind_0808
CCACCCTCGTGGTATGGCTAGGCATTCAGGAACCGGAGAACGCTTCAGACCAGCCCGGAC
TGGGAACCTGCGGGCAGTAGGTGGAAT
"""

    Max_GC_id, Max_GC_content = Max_GCContent(sample_input)

    # Now we output the result
    print(Max_GC_id)
    print(f"{Max_GC_content:.6f}")