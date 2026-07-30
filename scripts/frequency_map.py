# UCSD Bioinformatics: FrequencyMap()
def FrequencyMap(Text, k):
    freq = {}       # start with a blank dictionary
    n = len(Text)                   
    for i in range(n - k + 1):      # for a certain index in the range of 0 to (n-k+1) where there are n-k+1 k-mers in a string of length n
        Pattern = Text[i:i + k]         # extract the k-mer, which in this case is Pattern, at index i
        if Pattern in freq:     # if the k-mer is already in the dictionary, increment its count by 1
            freq[Pattern] += 1      
        else:       # if the k-mer is not in the dictionary, add it to the dictionary with a count of 1
            freq[Pattern] = 1
    return freq