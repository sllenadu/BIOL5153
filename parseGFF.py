#!/usr/bin/env python3

#importing csv package 
import csv

#importing argparse packge
import argparse
from Bio import SeqIO # importing SeqIO (is a command) in biopython 


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


# create csv reader object 
with open(args.gff, 'r') as gff_in:
    reader = csv.reader(gff_in, delimiter='\t')
    for line in reader: # loop over all lines in the reader object ie; parsed file
        # for CSV files using (',') is insufficient. You can use athe csv package for this
        start = int(line[3])-1 # use column 3, python indexing considers the first integer as 0 therefore, substract by 1
        end = int(line[4]) 
        desc = line[-1]
        
        
        # extract the sequence
        print(">"+genome.id , desc)
        print(genome.seq[start:end])
        print()
        
        

# parse the GFF file




