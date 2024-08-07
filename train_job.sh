#!/bin/bash
#SBATCH -n 1
#SBATCH --cpus-per-task=8
#SBATCH --time=4:00:00
#SBATCH --mem-per-cpu=4G
#SBATCH --output="run_sparse.out"
#SBATCH --nodelist=ault25

source ~/.bashrc
pyact Thesis
trap 'echo "SIGTERM received"; scontrol requeue ${SLURM_JOB_ID}; exit 15' 15
# Run your program here
# torchrun --standalone --nproc_per_node=8 ~/sparselinear/nanoGPT/train.py config/train_gpt2.py
# python ~/sparselinear/nanoGPT/train.py
torchrun --standalone --nproc_per_node=4 ~/sparselinear/nanoGPT/train.py $1
# python ~/sparselinear/nanoGPT/train.py $1
pop_queue