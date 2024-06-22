# config for training GPT-2 (124M) down to very nice loss of ~2.85 on 1 node of 8X A100 40GB
# launch as the following (e.g. in a screen session) and wait ~5 days:
# $ torchrun --standalone --nproc_per_node=8 train.py config/train_gpt2.py

wandb_log = True
wandb_project = 'GPT2'
experiment_name='dense_mine_better_optimizer_fanin'

# these make the total batch size be ~0.5M
# 12 batch size * 1024 block size * 5 gradaccum * 8 GPUs = 491,520
batch_size = 12
block_size = 1024
gradient_accumulation_steps = 5 * 8

# this makes total number of tokens be 300B
max_iters = 600000
lr_decay_iters = 600000

# eval stuff
eval_interval = 200
eval_iters = 200
log_interval = 10

# optimizer
weight_decay = 1e-1
beta1 = 0.9
beta2 = 0.999
learning_rate = 5e-5

# Linear layer
linear_type = "dense"
init_mode = "fan_in"
