# config for training GPT-2 (124M) down to very nice loss of ~2.85 on 1 node of 8X A100 40GB
# launch as the following (e.g. in a screen session) and wait ~5 days:
# $ torchrun --standalone --nproc_per_node=8 train.py config/train_gpt2.py

wandb_log = True
# wandb_project = 'GPT2'
experiment_name='connected_sparse'

# Linear layer
linear_type = "better_connected_sparse"
guarantee_rank = False
interleave = False