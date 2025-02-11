pip install --upgrade pip
pip install torch==2.4.1 torchvision==0.19.1 torchaudio==2.4.1 --index-url https://download.pytorch.org/whl/cu121
pip install -r requirements.txt

# For loading checkpoints (Run the commands)
pip install gdown
gdown --folder https://drive.google.com/drive/folders/1yELzm5SvAi9e7kPcO_jPp2XkTs4vK6aR -O $(findscratch)
cd $(findscratch)

# Need to downgrade huggingface_hub to 0.25.0 because developers are morons.