# Make sure we don't overload memory with our models:
# conda activate /depot/chan129/apps/SUPIR

path=$(findscratch)

export TRANSFORMERS_CACHE=${path}
export HF_HOME=${path}