$RESUME=0

if [[ "$*" == *"--resume"* ]]; then
    RESUME=1
fi

script_path=$(realpath "$0")
script_dir=$(dirname "$script_path")

config_file=$1
config_name=$(basename "$config_file" .py)
config_folder=$(dirname "$config_file")
output_file="$config_folder"/../out/"$config_name".out

if [[ $RESUME -eq 0 ]]; then
    rm -f "$config_folder"/../out/"$config_name".out*
    rm -rf "$config_folder"/../out/"$config_name"else
fi

sbatch --output="$output_file" "$script_dir"/train_job.sh "$config_file"
