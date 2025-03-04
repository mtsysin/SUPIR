echo "Running the local script."

CUDA_VISIBLE_DEVICES=0,1 python -u test.py\
    --img_dir './run'\
    --save_dir ./results-Q\
    --SUPIR_sign Q\
    --upscale 2\
    --no_llava\
    --caption "A Mercedes car"

# sbatch --nodes=1 --gpus-per-node=1 run_script.sh   scontrol show job      squeue -u mtsysin
# Specific node sbatch --nodes=1 --ntasks=16 --gres=gpu:1 --constraint=A myjobsubmissionfile.sub
# sinteractive -A stanchan-k --nodes=1 -n32 --gpus-per-node=1 -t 3-0:00:00
# Attach to your job sattach <job_id>