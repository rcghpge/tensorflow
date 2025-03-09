# Tensorflow 
- Custom stable Tensorflow and Keras environment for Dell Precision 5510 Workstations.
- `requirements.txt` provides TF and Keras versioning information and Python version needed. Runs on CUDA 12.0 and CUDNN 8.9.7
- Windows WSL2 for Linux does not have NUMA support.
- Run Tensorflow environment in a conda virtual environment.
---
## Getting Started
Clone repository
```bash
git clone https://github.com/rcghpge/tensorflow.git
cd tensorflow
```

You should be able to replicate the environment via
```bash
pip install -r requirements.txt
```

Initialize a Conda environment (install Conda if needed - see technical documentation)
```bash
conda create -n tfenv python=x.x
conda activate tfenv
```
---
## Technical Documentation
- [Conda](https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html) - Installation docs.
---
