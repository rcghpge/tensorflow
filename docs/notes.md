# Notes
---
**Dell Precision 5510 Workstation compatibility:**
These versions are stable to a degree on this machine
- Tensorflow - Keras version 2.6.0
- cudnn 8.9.7.29
- cuda-version 11.8
- cudatoolkit 11.8.0

GitHub security vulnerablities:
- This stable version of Tensorflow and Keras for this specific machine triggers security vulnerabilities with GitHub's Dependabot
and its cybersecurity toolchain.
- If the Dependabot's PR's are merged, it breaks the stability of this current 'stable' setup venv.

