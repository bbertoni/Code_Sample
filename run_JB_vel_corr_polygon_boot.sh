#!/bin/bash

# This code is executed by typing "bash run_JB_vel_corr_polygon_boot.sh halo_number".  It then
# creates a new directory "halo_number_boot", generates a random number called "seed", and
# creates a directory within the "halo_number_boot" directory called "seed".  Within the
# directory "seed", it executes another shell script "compute_JB_vel_corr_polygon_boot.sh" many
# times, each time submitting a job to the cluster at Stanford which is managed by SLURM.

dir=$1
dir+=_boot

cd $dir

seed=$RANDOM

mkdir $seed

cd $seed

sbatch /home/bbertoni/BullockJohnston/compute_JB_vel_corr_polygon_boot.sh $1 0 10 10 $seed &

sbatch /home/bbertoni/BullockJohnston/compute_JB_vel_corr_polygon_boot.sh $1 10 20 10 $seed &

sbatch /home/bbertoni/BullockJohnston/compute_JB_vel_corr_polygon_boot.sh $1 20 30 10 $seed &

sbatch /home/bbertoni/BullockJohnston/compute_JB_vel_corr_polygon_boot.sh $1 30 40 10 $seed &

sbatch /home/bbertoni/BullockJohnston/compute_JB_vel_corr_polygon_boot.sh $1 40 50 10 $seed &

sbatch /home/bbertoni/BullockJohnston/compute_JB_vel_corr_polygon_boot.sh $1 50 60 10 $seed &

sbatch /home/bbertoni/BullockJohnston/compute_JB_vel_corr_polygon_boot.sh $1 60 70 10 $seed &

sbatch /home/bbertoni/BullockJohnston/compute_JB_vel_corr_polygon_boot.sh $1 70 80 10 $seed &

sbatch /home/bbertoni/BullockJohnston/compute_JB_vel_corr_polygon_boot.sh $1 80 90 10 $seed &

sbatch /home/bbertoni/BullockJohnston/compute_JB_vel_corr_polygon_boot.sh $1 90 100 10 $seed &

sbatch /home/bbertoni/BullockJohnston/compute_JB_vel_corr_polygon_boot.sh $1 100 120 10 $seed &

sbatch /home/bbertoni/BullockJohnston/compute_JB_vel_corr_polygon_boot.sh $1 120 140 10 $seed &

sbatch /home/bbertoni/BullockJohnston/compute_JB_vel_corr_polygon_boot.sh $1 140 160 10 $seed &

sbatch /home/bbertoni/BullockJohnston/compute_JB_vel_corr_polygon_boot.sh $1 160 180 10 $seed &

sbatch /home/bbertoni/BullockJohnston/compute_JB_vel_corr_polygon_boot.sh $1 180 200 10 $seed &

sbatch /home/bbertoni/BullockJohnston/compute_JB_vel_corr_polygon_boot.sh $1 200 220 10 $seed &

sbatch /home/bbertoni/BullockJohnston/compute_JB_vel_corr_polygon_boot.sh $1 220 240 10 $seed &

sbatch /home/bbertoni/BullockJohnston/compute_JB_vel_corr_polygon_boot.sh $1 240 260 10 $seed &

sbatch /home/bbertoni/BullockJohnston/compute_JB_vel_corr_polygon_boot.sh $1 260 280 10 $seed &

sbatch /home/bbertoni/BullockJohnston/compute_JB_vel_corr_polygon_boot.sh $1 280 300 10 $seed &

cd ..

cd ..
