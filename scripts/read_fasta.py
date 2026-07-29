# Read a FASTA file

with open("data/raw/sample.fasta", "r") as file:
    content = file.read()

print(content)
