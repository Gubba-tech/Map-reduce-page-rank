#!/bin/bash
#
#SBATCH --output=v1_1.csv
#SBATCH --ntasks-per-node=24
#SBATCH --nodes=2
#SBATCH --time=20:00
#SBATCH -p short-24core


module load anaconda/2
module load slurm
module load mvapich2/gcc/64/2.2rc1
/gpfs/home/weicdeng/project/hw2/iteration1_1.py
