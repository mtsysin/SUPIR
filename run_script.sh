#!/bin/bash
#SBATCH --job-name=my_job
#SBATCH --output=slurm-%j.out
#SBATCH --error=slurm-%j.out
#SBATCH --mem=60G  # Request 16GB of memory
#SBATCH --time=01:00:00  # Set job time limit (1 hour)

echo "This is a test message."
# Get info about GPUs:
nvidia-smi

# Change to the directory from which you originally submitted this job.
cd $SLURM_SUBMIT_DIR



source run.sh
