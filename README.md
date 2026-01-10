# test_speach_to_text
STT(Speech-to-Text)


## 1. Setting up the Environment for Mac m2
        conda create -n s2txt python=3.9
        conda activate s2txt

        conda install pytorch torchvision torchaudio cpuonly -c pytorch
        pip install openai-whisper setuptools-rust
        conda install -c conda-forge ffmpeg

## 2. Setting up the Environment for Ubuntu 24.04.2 LTS 2080ti(Driver Version: 550.120 CUDA Version: 12.4 )
        conda create -n s2txt python=3.9
        conda activate s2txt

        conda install pytorch torchvision torchaudio pytorch-cuda=11.8 -c pytorch -c nvidia
        pip install openai-whisper setuptools-rust
        conda install -c conda-forge ffmpeg