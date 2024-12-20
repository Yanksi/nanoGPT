# config for training GPT-2 (124M) down to very nice loss of ~2.85 on 1 node of 8X A100 40GB
# launch as the following (e.g. in a screen session) and wait ~5 days:
# $ torchrun --standalone --nproc_per_node=8 train.py config/train_gpt2.py

wandb_log = True
# wandb_project = 'GPT2'
experiment_name='sparse_rank_muP_3'

# Linear layer
linear_type = "sparse"
guarantee_rank = True
init_mode = "muP"