script_path=$(realpath "$0")
script_dir=$(dirname "$script_path")

config_file=$1
config_name=$(basename "$config_file" .py)
config_folder=$(dirname "$config_file")
output_file="$config_folder"/../output/"$config_name".out

sbatch --output="$output_file" "$script_dir"/train_job.sh "$config_file"
