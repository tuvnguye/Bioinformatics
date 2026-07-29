# DNA Toolkit

def validate_dna_seq(dna_seq):
    validate_bases = "A", "T", "G", "C"
    for bases in dna_seq:
        if bases not in validate_bases:
            return False
    return True

def nucleotide_count(dna_seq):
    count = {"A": 0, "T": 0, "G": 0, "C": 0}
    for nuc in dna_seq:
        if nuc in count:
            count[nuc] += 1
    return count

def gc_content(dna_seq):
    gc_count = dna_seq.count("G") + dna_seq.count("C")
    return (gc_count / len(dna_seq)) * 100

def reverse_complement(dna_seq):
    complement = ""
    for base in dna_seq:
        if base == "A":
            complement += "T"
        elif base == "T":
            complement += "A"
        elif base == "C":
            complement += "G"
        elif base == "G":
            complement += "C"
    return complement[::-1]

def transcribe_dna_to_mRNA(dna_seq):
    return dna_seq.replace("T", "U")

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

if __name__ == "__main__":
    dna_seq = input("Enter a DNA sequence from 5' to 3': ").upper()
    if validate_dna_seq(dna_seq):
        print("Validated DNA sequence")
        count = nucleotide_count(dna_seq)
        print("Number of A nucleotides: ", count["A"])
        print("Number of T nucleotides: ", count["T"])
        print("Number of G nucleotides: ", count["G"])
        print("Number of C nucleotides: ", count["C"])
        print("GC content:", gc_content(dna_seq), "%")
        print("Reverse complement:", reverse_complement(dna_seq))
        print("mRNA sequence:", transcribe_dna_to_mRNA(dna_seq))
        print("Protein sequence:", translate_mRNA_to_protein(transcribe_dna_to_mRNA(dna_seq)))
    else:
        print("Invalid DNA sequence")
        