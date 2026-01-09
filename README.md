# test_speach_to_text
STT(Speech-to-Text)

        conda create -n s2txt python=3.9
        conda activate s2txt

        conda install pytorch torchvision torchaudio cpuonly -c pytorch
        conda install pytorch torchvision torchaudio pytorch-cuda=11.8 -c pytorch -c nvidia
        pip install openai-whisper setuptools-rust
        conda install -c conda-forge ffmpeg
