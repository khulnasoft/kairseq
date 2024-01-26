from pathlib import Path
import os

cwd = Path(".").resolve()
print("running 'check_installation.py' from:", cwd)

# Old versions of numpy/torch can prevent loading the .so files
import torch

print("torch:", torch.__version__)
import numpy

print("numpy:", numpy.__version__)

import kairseq

print("Kairseq installed at:", kairseq.__file__)
import kairseq.criterions
import kairseq.dataclass.configs

import _imp

print("Should load following .so suffixes:", _imp.extension_suffixes())

so_files = list(Path(kairseq.__file__).parent.glob("*.so"))
so_files.extend(Path(kairseq.__file__).parent.glob("data/*.so"))
print("Found following .so files:")
for so_file in so_files:
    print(f"- {so_file}")

from kairseq import libbleu

print("Found libbleu at", libbleu.__file__)
from kairseq.data import data_utils_fast

print("Found data_utils_fast at", data_utils_fast.__file__)
