# Tensorflow 
- Installation for Tensorflow and Keras environment for legacy Dell Precision Workstations.
- Testing/tested on Dell Precision 5510 Workstation.
- `requirements.txt` and `conda-requirements.txt` provides TF and Keras versioning information and Python version needed. Runs on Python 3.8, Tensorflow 2.6.0, Keras 2.6.0, CUDA 11.8, CUDNN 8.9.7, and Windows WSL2 - Ubuntu 24.04
- Arch Linux wip
- Windows WSL2 for Linux does not have NUMA support.
- Run Tensorflow environment in a conda virtual environment.
---
## Getting Started 
### Ubuntu/UbuntuWSL
Clone repository
```bash
git clone https://github.com/rcghpge/tensorflow.git
cd tensorflow
```

Initialize a Conda environment (install Conda if needed - see technical documentation)
```bash
conda init
conda config --set auto_activate_base false # disables venv auto-activate 
conda create -n tfenv python=3.8
conda activate tfenv
```

You should be able to replicate the environment via
```bash
conda install --file conda-requirements.txt
pip install -r requirements.txt

```

### Arch Linux/ArchWSL
wip - Arch Linux installation is a little different. Currently not detecting GPU.
```bash
sudo pacman -S python-conda
conda init
conda config --set auto_activate_base false
conda create -n tfenv python=3.8
conda activate tfenv

# Install requirements
conda install --file conda-requirements.txt
pip install -r requirements.txt
```

You can install TensorFlow from pacman on Arch Linux and test Python versioning from latest.
Currently only detects CPU - no GPU detected.

Verify Tensorflow and Keras environment
```bash
python -c "import tensorflow as tf; print('TensorFlow Keras Version:', tf.keras.__version__)"
python -c "import tensorflow as tf; print('Num CPUs Available:', len(tf.config.list_physical_devices('CPU')))"
python -c "import tensorflow as tf; print('Num GPUs Available:', len(tf.config.list_physical_devices('GPU')))"
```

## Test Tensorflow and Keras environment
I have provided a `test/` directory with sample models to test the development environment. Run test models 
```bash
python3 testkeras.py
```
---
## Technical Documentation
- [Ubuntu Desktop](https://ubuntu.com/tutorials/install-ubuntu-desktop#1-overview) - Ubuntu Installation docs
- [Arch Linux](https://wiki.archlinux.org/title/Installation_guide) - Arch Linux Installation docs
- [UbuntuWSL](https://documentation.ubuntu.com/wsl/en/latest/howto/install-ubuntu-wsl2/) - UbuntuWSL Instalation docs
- [LnOS Arch](https://github.com/uta-lug-nuts/LnOS/wiki) - LnOS Arch Installation Wiki
- [Conda](https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html) - Main Conda Installation docs
- [Conda on Arch Linux](https://wiki.archlinux.org/title/Conda) - Conda Installation docs for Arch Linux
- [TensorFlow](https://www.tensorflow.org/install) - TensorFlow Installation docs
- [Keras](https://keras.io/getting_started/) - Keras Installation docs
  
---
If there is a stable solution for older Dell workstations feel free to contact me or send PR's to optimize this stack for legacy Dell Precision Workstation line of machines.

---
