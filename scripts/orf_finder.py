# ORF finder

import dna_toolkit

def find_orfs(dna_sequence):
    #rc = reverse_complement(dna_sequence)
    start_codon = "ATG"
    stop_codon = {"TAA", "TAG", "TGA"}
    orfs = []
    for frame in range(3):
        orf_start = None
        for i in range(frame, len(dna_sequence) - 2, 3):
            codon = dna_sequence[i:i+3]
            if codon == start_codon and orf_start is None:
                orf_start = i
            elif codon in stop_codon and orf_start is not None:
                orf = dna_sequence[orf_start:i+3] 
                orfs.append(orf)
                orf_start = None
    return orfs

if __name__ == "__main__":
    dna_seq = input("Enter a DNA sequence from 5' to 3': ").upper()
    if dna_toolkit.validate_dna_seq(dna_seq):
        orfs = find_orfs(dna_seq)
        print("Open Reading Frames:", orfs)
    else:
        print("Invalid DNA sequence")

# shifing reading frame


