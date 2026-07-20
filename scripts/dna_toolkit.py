# DNA sequence toolkit

seq = input("Enter a DNA sequence from 5' to 3': ").upper()
dna_seq = seq.replace(" ", "").join(seq.splitlines())

print("Length of the sequence: ", len(seq), "nucleotides")

def validate_dna_seq(seq):
    validate_bases = "A", "T", "G", "C"
    for bases in seq:
        if bases not in validate_bases:
            return False
    return True
if not validate_dna_seq(seq):
    print("Invalid DNA sequence")
else:
    nuc_A = seq.count("A")
    nuc_T = seq.count("T")
    nuc_C = seq.count("C")
    nuc_G = seq.count("G")

    print("Number of A nucleotides: ", nuc_A)
    print("Number of T nucleotides: ", nuc_T)
    print("Number of C nucleotides: ", nuc_C)
    print("Number of G nucleotides: ", nuc_G)

    AT_content = ((nuc_A + nuc_T) / len(seq) * 100)
    GC_content = ((nuc_C + nuc_G) / len(seq) * 100)

    print("The GC content of the sequence: ", GC_content, "%")
    print("The AT content of the sequence: ", AT_content, "%")

# Print reverse complementary sequence
complement = ""
for base in seq:
    if base == "A":
        complement += "T"
    elif base == "T":
        complement += "A"
    elif base == "C":
        complement += "G"
    elif base == "G":
        complement += "C"
reverse_complement = complement[::-1]
print("Reverse complementary sequence: 5'", reverse_complement, "3'")

# DNA to mRNA transcription
rna_seq = seq.replace("T", "U")
print("mRNA sequence: 5'", rna_seq, "3'")

# mRNA to protein translation
def translate_mRNA_to_protein(rna_seq):
    codon_table = {
        'UUU':'F','UUC':'F','UUA':'L','UUG':'L',
        'UCU':'S','UCC':'S','UCA':'S','UCG':'S',
        'UAU':'Y','UAC':'Y','UAA':'*','UAG':'*',
        'UGU':'C','UGC':'C','UGA':'*','UGG':'W',
        'CUU':'L','CUC':'L','CUA':'L','CUG':'L',
        'CCU':'P','CCC':'P','CCA':'P','CCG':'P',
        'CAU':'H','CAC':'H','CAA':'Q','CAG':'Q',
        'CGU':'R','CGC':'R','CGA':'R','CGG':'R',
        'AUU':'I','AUC':'I','AUA':'I','AUG':'M',
        'ACU':'T','ACC':'T','ACA':'T','ACG':'T',
        'AAU':'N','AAC':'N','AAA':'K','AAG':'K',
        'AGU':'S','AGC':'S','AGA':'*','AGG':'*',
        'GUU':'V','GUC':'V','GUA':'V','GUG':'V',
        'GCU':'A','GCC':'A','GCA':'A','GCG':'A',
        'GAU':'D','GAC':'D','GAA':'E','GAG':'E',
        'GGU':'G','GGC':'G','GGA':'G','GGG':'G'
        }
    protein_seq = ""
    for i in range(0, len(rna_seq) - 2, 3):
        codon = rna_seq[i:i+3]
        protein_seq += codon_table.get(codon) 
    return protein_seq

# Translate the DNA sequence to a protein sequence
protein_seq = translate_mRNA_to_protein(rna_seq)
print("Protein sequence: ", protein_seq)