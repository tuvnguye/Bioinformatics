# Pasrse a FASTA file and print the name, sequence, and length of each sequence in the file

with open ("data/raw/sample.fasta", "r") as file:
    lines = file.readlines()

name = ""
sequence = ""

for line in lines:
    line = line.strip()

    if line.startswith(">"):
        if name != "":
            print("Name: ", name)
            print("Sequence: ", sequence)
            print("Length of sequence: ", len(sequence), "nucleotides")
            print()
        name = line[1:].strip()
        sequence = ""
    else:
        sequence += line.strip()

print("Name:", name)
print("Sequence:", sequence)       
print("Length of sequence:", len(sequence), "nucleotides")
