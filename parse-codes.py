#!/usr/bin/env python3

#importing csv package 
import csv

#importing argparse packge
import argparse
from Bio import SeqIO # importing SeqIO (is a command) in biopython 
from collections import defaultdict
import re

# declaring rev_comp function
def rev_comp(sequence):
    return(sequence.reverse_complement())


# this script will parse a GFF file and extract each feature from the genome
# inputs: 1) GFF file 2) corressponding genome sequence (FASTA format)

#create an argument parser object
parser = argparse.ArgumentParser(description = ' this script will parse a GFF file and extract each feature from the genome')

# add positional arguments
parser.add_argument("gff", help='name of the GFF file')
parser.add_argument("fasta", help='name of the FASTA file')

# parse the arguments
args = parser.parse_args()
#print(args.gff)
#print(args.fasta)


#make sure you have the link or files in the same directory as you save your scripts. YOu can link
# by using ln -s ~PATH_to_file

# GFF filename
gff_input = 'watermelon.gff'

# fasta filename
fasta_input = 'watermelon.fsa'

# read in GFF file
#with open(gff_input, 'r') as gff_in:
    #for line in gff_in:
        #columns = line.split('\t') #split columns based on tab delimtter
        # for CSV files using (',') is insufficient. You can use athe csv package for this
        #print(columns[3], columns[4]) #grabbing the columns we needed

# read in FASTA file 
genome = SeqIO.read(args.fasta, 'fasta')
#print(genome.id)
#print(len(genome.seq))

# creating a dictionary for header
thisdict = defaultdict(dict)
        
# building the coding sequence (CDS) 
with open(args.gff, 'r') as gff_in: # reads the GFF file
    reader = csv.reader(gff_in, delimiter='\t') 
    for line in reader:
        if line[2] == "CDS":
            start = int(line[3])-1 # use column 3, python indexing considers the first integer as 0 therefore, substract by 1
            end = int(line[4])
            strand = line[6]
            desc = line[-1]
            re_exon = re.search("exon (\d)", desc)
        # creating the header
            name = line[-1]
            split = name.split()[1]
            exon_num = name.split()[3]
            species = line[0]
            split_species = species.split()
            #print(">" + split_species[0] + "_" + split_species[1] + "_" +  split)
            header = str(">" + split_species[0] + "_" + split_species[1] + "_" +  split)
        
            if strand =="-":
                seq = rev_comp(genome.seq[start:end])
            else:
                seq = genome.seq[start:end]
            # adding value to dictionary key
            if not re_exon:
                thisdict[header]= seq
            elif not thisdict[header]:
                thisdict[header] = ['']*10
                thisdict[header][int(exon_num)-1] = seq
            else:
                thisdict[header][int(exon_num)-1] = seq
            

for l in thisdict:
    thisdict[l] = ''.join(str(exon) for exon in thisdict[l])

for i,j in thisdict.items():
    print(i)
    print(j)            
            




