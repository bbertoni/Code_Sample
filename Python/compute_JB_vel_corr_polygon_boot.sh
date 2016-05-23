#!/bin/bash

# This shell script submits a job to the Stanford cluster (managed by SLURM) which runs a Python
# code called "compute_JB_vel_corr_polygon_boot.py" and makes sure that the compute node which 
# ends up running to code has access to the Anaconda python distribution if necessary.
 

#all commands that start with SBATCH contain commands that are used by SLURM for scheduling  
#################
#set a job name  
#SBATCH --job-name=JB_vel_corr_boot
#################  
#a file for job output, you can check job progress
#SBATCH --output=JB_vel_corr_boot.out
#################
# a file for errors from the job
#SBATCH --error=JB_vel_corr_boot.err
#################
#time you think you need; default is one hour; maximum on normal queue is 2 days
#in minutes in this case, hh:mm:ss
#SBATCH --time=47:59:00
#################
#quality of service; think of it as job priority
#SBATCH --qos=normal
#################
#number of nodes you are requesting
#SBATCH --nodes=1
#################
#memory per node; default is 4000 MB per CPU
#SBATCH --mem=4000
#you could use --mem-per-cpu; they mean what we are calling cores
#################
#tasks to run per node; a "task" is usually mapped to a MPI processes.
# for local parallelism (OpenMP or threads), use "--ntasks-per-node=1 --cpus-per-task=16" instead
#SBATCH --ntasks-per-node=1
#################
#SBATCH -p iric
# recommended by Tom -- run on iric partition
#################


export PATH="/home/bbertoni/anaconda3/bin:$PATH"

python /home/bbertoni/BullockJohnston/compute_JB_vel_corr_polygon_boot.py $1 $2 $3 $4 $5
