# Tensorflow 
- Custom stable Tensorflow and Keras environment for Dell Precision 5510 Workstations.
- `requirements.txt` provides TF and Keras versioning information and Python version needed. Runs on CUDA 12.0 and CUDNN 8.9.7
- Windows WSL2 for Linux does not have NUMA support.
- Run Tensorflow environment in a conda virtual environment.
- Runs on Ubuntu 24.04 
---
## Getting Started
Clone repository
```bash
git clone https://github.com/rcghpge/tensorflow.git
cd tensorflow
```

Initialize a Conda environment (install Conda if needed - see technical documentation)
```bash
conda create -n tfenv python=x.x
conda activate tfenv
```

You should be able to replicate the environment via
```bash
pip install -r requirements.txt
```

## Test Tensorflow and Keras environment
I have provided a `test/` directory with sample models to test the development environment. Run test models 
```bash
python3 testkeras.py
```
---
## Technical Documentation
- [Conda](https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html) - Installation docs.
---
If you run into any issues feel free to open a issue or PR. DMs are open if this could serve as a Tensorflow and Keras toolchain for Dell machines.

---
