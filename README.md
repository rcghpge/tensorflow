# tensorflow 

[![CodeQL](https://github.com/rcghpge/tensorflow/actions/workflows/github-code-scanning/codeql/badge.svg)](https://github.com/rcghpge/tensorflow/actions/workflows/github-code-scanning/codeql)
[![Bandit](https://github.com/rcghpge/tensorflow/actions/workflows/bandit.yml/badge.svg)](https://github.com/rcghpge/tensorflow/actions/workflows/bandit.yml)

- Installation for Tensorflow and Keras environment for legacy Dell Precision Workstations and HP ZBook G-series Workstations
- Testing/tested on Dell Precision 5510 Workstation, HP ZBook G6 Workstation
- OS environments testing/tested on: Windows 10 Pro, Windows 11 Pro, LnOS Arch (Arch-based)
- wip: `environment.yml` provides TF and Keras versioning information and Python version needed. Runs on Python 3.8, Tensorflow 2.6.0, Keras 2.6.0, CUDA 11.8, CUDNN 8.9.7, and Windows WSL2 - Ubuntu 24.04
- Arch Linux wip
- Windows WSL2 for Linux does not have NUMA support.
- Run Tensorflow environment in a conda virtual environment.
---
## Getting Started 
### Ubuntu/UbuntuWSL
To install Anaconda on Ubuntu/UbuntuWSL see Anaconda installation docs at Technical Documentation section. Refer back to steps below
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
# List available Conda environments
conda env list

# Install Conda environment
conda env update -f environment.yml --prune
```

### Arch Linux/ArchWSL
wip - Arch Linux installation is a little different. Currently not detecting GPU.
```bash
# Install Conda
sudo pacman -S python-conda
conda init
conda config --set auto_activate_base false
conda create -n tfenv python=3.8
conda activate tfenv

# Check Conda local environment
# List available conda environments
conda env list

# Install Conda environment
conda env update -f environment.yml --prune
```

You can install TensorFlow from pacman on Arch Linux and test Python versioning from latest.
Currently only detects CPU - no GPU detected.

]Verify Tensorflow and Keras environment
```bash
python -c "import tensorflow as tf; print('TensorFlow Keras Version:', tf.keras.__version__)"
python -c "import tensorflow as tf; print('Num CPUs Available:', len(tf.config.list_physical_devices('CPU')))"
python -c "import tensorflow as tf; print('Num GPUs Available:', len(tf.config.list_physical_devices('GPU')))"
```

## Test Tensorflow and Keras environment
I have provided a `test/` directory with sample models to test the development environment. Run test models 
```bash
python3 test/testkeras.py
```
---
## Technical Documentation
- [Ubuntu Desktop](https://ubuntu.com/tutorials/install-ubuntu-desktop#1-overview) - Ubuntu Installation docs
- [Arch Linux](https://wiki.archlinux.org/title/Installation_guide) - Arch Linux Installation docs
- [UbuntuWSL](https://documentation.ubuntu.com/wsl/en/latest/howto/install-ubuntu-wsl2/) - UbuntuWSL Instalation docs
- [LnOS Arch](https://github.com/uta-lug-nuts/LnOS/wiki) - LnOS Arch (Arch-based) Installation Wiki
- [Conda](https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html) - Main Conda Installation docs
- [Conda on Arch Linux](https://wiki.archlinux.org/title/Conda) - Conda Installation docs for Arch Linux
- [Anaconda](https://www.anaconda.com/docs/getting-started/anaconda/install#macos-linux-installation:manual-shell-initialization) - Anaconda Installation docs for Ubuntu/UbuntuWSL
- [TensorFlow](https://www.tensorflow.org/install) - TensorFlow Installation docs
- [Keras](https://keras.io/getting_started/) - Keras Installation docs

---
If there is a stable solution for older Dell workstations feel free to contact me or send PR's to optimize this stack for legacy Dell Precision Workstation line of machines.

For HP Zbook G-series workstations there doesn't seem to be a backward compatibility issue so far but I have only just secured the model that I use.

---
