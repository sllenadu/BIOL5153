#! /share/apps/python/anaconda3-3.6.0/bin/python3

# This script generates a PBS files for AHPCC Razor Cluster


# define a variable  
name = 'pbs_script'
queue = 'med16core'
output = 'pbs_script'
nodes = 1 # number of nodes
processors = 1 # number of processors 
wall = 3 # This is in hours


# This section prints the header and the required info for PBS script

print('#PBS -N', name) # job name
print('#PBS -q', queue) # which queue to use
print('#PBS -j oe') # join STDOUT and STERR into a single line
print('#PBS -o' , output +'.$PBS_JOBID') # name of the output file
print('#PBS -l nodes=' + str(nodes) + ':' + 'ppn=' + str(processors)) # resources to ask for 
print('#PBS -l walltime=' + str(wall) +':00:00') # set the walltime
print()

# Print working directory
print('cd $PBS_O_WORKDIR')
print()


# load modules necessary for this script
print('module purge')
print('module load gcc/7.2.1 python/3.6.0-anaconda java/sunjdk_1.8.0 blast mafft/7.304b')
print()

# Commands for these jobs
print('# insert commands here')
'''
command 1
command 2
.
.
.
command n
'''



