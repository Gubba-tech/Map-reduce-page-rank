#!/bin/bash
#
#SBATCH --output=v2_2.csv
#SBATCH --ntasks-per-node=28
#SBATCH --nodes=2
#SBATCH --time=20:00
#SBATCH -p short-28core


module load anaconda/2
module load slurm
module load mvapich2/gcc/64/2.2rc1
/gpfs/home/weicdeng/project/hw2/map2_2.py
