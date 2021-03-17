#!/usr/bin/env python3

#!/bin/bash
  
# This is a SLURM script for the Pinnacle cluster

# define variables
name = 'Trinity-assembly'
queue = 'partition comp06'
output = 'Trinity-assembly'
nodes = 1
processors = 32
wall = 6

# This section prints the header and the required info for SLURM script
print('#SBATCH -J', name) # job name
print('#SBATCH --' + queue) # which queue to use
print('#SBATCH -o', output + '_%j.txt') # output file
print('#SBATCH -e Trinity_%j.err') # error log
print('#SBATCH --mail-type=ALL') # mail events 
print('#SBATCH --mail-user=sllenadu@uark.edu ') # email address
print('#SBATCH --nodes=' + str(nodes)) # number of nodes to be used
print('#SBATCH --ntasks-per-node=' + str(processors)) # number of tasks assigned per node
print('#SBATCH --time=' + str(wall) + ':00:00') # time limit hrs:min:sec

print()

print('export OMP_NUM_THREADS=32')
 
print()
# load required modules
print('module load samtools')
print('module load jellyfish')
print('module load bowtie2')
print('module load salmon/0.8.2')
print('module load java')
 
print()

# cd into the directory where you're submitting this script from
print('cd $SLURM_SUBMIT_DIR')

print()

# copy files from storage to scratch
print('rsync -av RNA-R*.fastq.gz /scratch/$SLURM_JOB_ID')

print()

# cd onto the scratch disk to run the job
print('cd /scratch/$SLURM_JOB_ID/')

print()

# run the Trinity assembly
print('/share/apps/bioinformatics/trinity/trinityrnaseq-v2.11.0/Trinity --seqType fq --left RNA-R1.fastq.gz --right RNA-R2.fastq.gz --CPU 48 --max_memory 250G --trimmomatic --no_normalize_reads --full_cleanup --output trinity_Run2')

print()

# copy output files back to storage
print('sync -av trinity_Run2 $SLURM_SUBMIT_DIR')

print()


