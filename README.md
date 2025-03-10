# Tensorflow 
- Custom stable Tensorflow and Keras environment for Dell Precision 5510 Workstations.
- `requirements.txt` provides TF and Keras versioning information and Python version needed. Runs on Python 3.8, Tensorflow 2.6.0, Keras 2.6.0, CUDA 11.8, CUDNN 8.9.7, and Windows WSL2 - Ubuntu 24.04 
- Windows WSL2 for Linux does not have NUMA support.
- Run Tensorflow environment in a conda virtual environment.
---
## Getting Started (Linux)
Clone repository
```bash
git clone https://github.com/rcghpge/tensorflow.git
cd tensorflow
```

Initialize a Conda environment (install Conda if needed - see technical documentation)
```bash
conda create -n tfenv python=3.8
conda activate tfenv
```

You should be able to replicate the environment via
```bash
conda install --file conda-requirements.txt
pip install -r requirements.txt

```

Verify stable Tensorflow and Keras environment
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
- [Ubuntu](https://documentation.ubuntu.com/wsl/en/latest/howto/install-ubuntu-wsl2/) - Instalation docs
- [Conda](https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html) - Installation docs
---
If you run into any issues feel free to open a issue or PR. DMs are open if this could serve as a Tensorflow and Keras toolchain for Dell machines.

---
