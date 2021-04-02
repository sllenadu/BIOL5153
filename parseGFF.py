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
print(args.gff)


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
        #print(columns[3], columns[4]) #grabbing hte columns we needed

# read in FASTA file 
genome = SeqIO.read(args.fasta, 'fasta')
print(genome.id)
print(len(genome.seq))


# create csv reader object 
with open(args.gff, 'r') as gff_in:
    reader = csv.reader(gff_in, delimiter='\t')
    for line in reader: # loop over al the lines in the reader object ie; parsed file
        # for CSV files using (',') is insufficient. You can use athe csv package for this
        start = line[3]
        end = line[4]
        strand = line[6]
        #print(start)
        #print(line) #makes a list out of the fields
        #print(line[3], line[4]) #grabbing the columns we needed
        
        # extract the sequence
        print(len(genome.seq))
       


# parse the GFF file




