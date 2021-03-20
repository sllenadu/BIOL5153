#!/usr/bin/env python3

# creating a variable for nad4L.fasta
filename = 'dna.txt'


# open the input file and assign to file handle called 'infile'
infile = open(filename, 'r')

# print infile
# print(infile)

# read the file without the line break
dna_sequence = infile.read().rstrip() 
# yet another way to read the file
# dna_sequence = dna_sequence.rstrip()

# print the dna_sequence variable
# print(dna_sequence)

# close the infile file
infile.close()

#print(dna_sequence)

# getting the length of the dna sequence
seqlen = len(dna_sequence)
print("Sequence length: ", seqlen)


# counting the number of As 
#print(dna_sequence.count('A'))

# setting a variable for the frequency of As
freqA = round((dna_sequence.count('A') / seqlen), 3)
print("Freq of A:", freqA)

# setting a variable for the frequency of Cs
freqC = round((dna_sequence.count('C') / seqlen), 3)
print("Freq of C:", freqC)

# setting a variable for the frequency of Gs
freqG = round((dna_sequence.count('G') / seqlen), 3)
print("Freq of G:", freqG)

# setting a variable for the frequency of Ts
freqT = round((dna_sequence.count('T') / seqlen), 3)
print("Freq of T:", freqT)

# calculating the G + C content
print('G+C content:', freqG + freqC)

# total frequency check
print('Total frequency=', freqA + freqC + freqG + freqT)

