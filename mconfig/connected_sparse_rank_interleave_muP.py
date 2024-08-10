# config for training GPT-2 (124M) down to very nice loss of ~2.85 on 1 node of 8X A100 40GB
# launch as the following (e.g. in a screen session) and wait ~5 days:
# $ torchrun --standalone --nproc_per_node=8 train.py config/train_gpt2.py

wandb_log = True
# wandb_project = 'GPT2'
experiment_name='connected_sparse_rank_interleave_muP'

# Linear layer
linear_type = "connected_sparse"
guarantee_rank = True
interleave = True
init_mode = "muP"