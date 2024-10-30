#!/usr/bin/python3

import platform
import sys
import numpy
import scipy
try:
    import librosa
except ModuleNotFoundError:
    librosa = None

print(platform.platform())
print("Python", sys.version)
print("NumPy", numpy.__version__)
print("SciPy", scipy.__version__)
if librosa is not None:
    print("librosa", librosa.__version__)
    librosa.show_versions()
