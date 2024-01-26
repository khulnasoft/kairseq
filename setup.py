#!/usr/bin/env python3
# Copyright (c) Facebook, Inc. and its affiliates.
#
# This source code is licensed under the MIT license found in the
# LICENSE file in the root directory of this source tree.

import os
import subprocess
import sys

from setuptools import Extension, find_packages, setup
from torch.utils import cpp_extension

if sys.version_info < (3, 6):
    sys.exit("Sorry, Python >= 3.6 is required for kairseq.")


def write_version_py():
    with open(os.path.join("kairseq", "version.txt")) as f:
        version = f.read().strip()

    # write version info to kairseq/version.py
    with open(os.path.join("kairseq", "version.py"), "w") as f:
        f.write('__version__ = "{}"\n'.format(version))
    return version


version = write_version_py()


with open("README.md") as f:
    readme = f.read()


if sys.platform == "darwin":
    extra_compile_args = ["-stdlib=libc++", "-O3"]
else:
    extra_compile_args = ["-std=c++11", "-O3"]


class NumpyExtension(Extension):
    """Source: https://stackoverflow.com/a/54128391"""

    def __init__(self, *args, **kwargs):
        self.__include_dirs = []
        super().__init__(*args, **kwargs)

    @property
    def include_dirs(self):
        import numpy

        return self.__include_dirs + [numpy.get_include()]

    @include_dirs.setter
    def include_dirs(self, dirs):
        self.__include_dirs = dirs


extensions = [
    Extension(
        "kairseq.libbleu",
        sources=[
            "kairseq/clib/libbleu/libbleu.cpp",
            "kairseq/clib/libbleu/module.cpp",
        ],
        extra_compile_args=extra_compile_args,
    ),
    NumpyExtension(
        "kairseq.data.data_utils_fast",
        sources=["kairseq/data/data_utils_fast.pyx"],
        language="c++",
        extra_compile_args=extra_compile_args,
    ),
    NumpyExtension(
        "kairseq.data.token_block_utils_fast",
        sources=["kairseq/data/token_block_utils_fast.pyx"],
        language="c++",
        extra_compile_args=extra_compile_args,
    ),
]


extensions.extend(
    [
        cpp_extension.CppExtension(
            "kairseq.libbase",
            sources=[
                "kairseq/clib/libbase/balanced_assignment.cpp",
            ],
        ),
        cpp_extension.CppExtension(
            "kairseq.libnat",
            sources=[
                "kairseq/clib/libnat/edit_dist.cpp",
            ],
        ),
        cpp_extension.CppExtension(
            "alignment_train_cpu_binding",
            sources=[
                "examples/operators/alignment_train_cpu.cpp",
            ],
        ),
    ]
)
if "CUDA_HOME" in os.environ:
    extensions.extend(
        [
            cpp_extension.CppExtension(
                "kairseq.libnat_cuda",
                sources=[
                    "kairseq/clib/libnat_cuda/edit_dist.cu",
                    "kairseq/clib/libnat_cuda/binding.cpp",
                ],
            ),
            cpp_extension.CppExtension(
                "kairseq.ngram_repeat_block_cuda",
                sources=[
                    "kairseq/clib/cuda/ngram_repeat_block_cuda.cpp",
                    "kairseq/clib/cuda/ngram_repeat_block_cuda_kernel.cu",
                ],
            ),
            cpp_extension.CppExtension(
                "alignment_train_cuda_binding",
                sources=[
                    "examples/operators/alignment_train_kernel.cu",
                    "examples/operators/alignment_train_cuda.cpp",
                ],
            ),
        ]
    )

cmdclass = {"build_ext": cpp_extension.BuildExtension}

if "READTHEDOCS" in os.environ:
    # don't build extensions when generating docs
    extensions = []
    if "build_ext" in cmdclass:
        del cmdclass["build_ext"]

    # use CPU build of PyTorch
    dependency_links = [
        "https://download.pytorch.org/whl/cpu/torch-1.7.0%2Bcpu-cp36-cp36m-linux_x86_64.whl"
    ]
else:
    dependency_links = []


if "clean" in sys.argv[1:]:
    # Source: https://bit.ly/2NLVsgE
    print("deleting Cython files...")

    subprocess.run(
        ["rm -f kairseq/*.so kairseq/**/*.so kairseq/*.pyd kairseq/**/*.pyd"],
        shell=True,
    )


extra_packages = []
if os.path.exists(os.path.join("kairseq", "model_parallel", "megatron", "mpu")):
    extra_packages.append("kairseq.model_parallel.megatron.mpu")


def do_setup(package_data):
    setup(
        name="kairseq",
        version=version,
        description="Facebook AI Research Sequence-to-Sequence Toolkit",
        url="https://github.com/pytorch/kairseq",
        classifiers=[
            "Intended Audience :: Science/Research",
            "License :: OSI Approved :: MIT License",
            "Programming Language :: Python :: 3.6",
            "Programming Language :: Python :: 3.7",
            "Programming Language :: Python :: 3.8",
            "Topic :: Scientific/Engineering :: Artificial Intelligence",
        ],
        long_description=readme,
        long_description_content_type="text/markdown",
        install_requires=[
            "cffi",
            "cython",
            "hydra-core>=1.0.7,<1.1",
            "omegaconf<2.1",
            "numpy>=1.21.3",
            "regex",
            "sacrebleu>=1.4.12",
            "torch>=1.13",
            "tqdm",
            "bitarray",
            "torchaudio>=0.8.0",
            "scikit-learn",
            "packaging",
        ],
        extras_require={
            "dev": ["flake8", "pytest", "black==22.3.0"],
            "docs": ["sphinx", "sphinx-argparse"],
        },
        dependency_links=dependency_links,
        packages=find_packages(
            exclude=[
                "examples",
                "examples.*",
                "scripts",
                "scripts.*",
                "tests",
                "tests.*",
            ]
        )
        + extra_packages,
        package_data=package_data,
        ext_modules=extensions,
        test_suite="tests",
        entry_points={
            "console_scripts": [
                "kairseq-eval-lm = kairseq_cli.eval_lm:cli_main",
                "kairseq-generate = kairseq_cli.generate:cli_main",
                "kairseq-hydra-train = kairseq_cli.hydra_train:cli_main",
                "kairseq-interactive = kairseq_cli.interactive:cli_main",
                "kairseq-preprocess = kairseq_cli.preprocess:cli_main",
                "kairseq-score = kairseq_cli.score:cli_main",
                "kairseq-train = kairseq_cli.train:cli_main",
                "kairseq-validate = kairseq_cli.validate:cli_main",
            ],
        },
        cmdclass=cmdclass,
        zip_safe=False,
    )


def get_files(path, relative_to="kairseq"):
    all_files = []
    for root, _dirs, files in os.walk(path, followlinks=True):
        root = os.path.relpath(root, relative_to)
        for file in files:
            if file.endswith(".pyc"):
                continue
            all_files.append(os.path.join(root, file))
    return all_files


if __name__ == "__main__":
    try:
        # symlink examples into kairseq package so package_data accepts them
        kairseq_examples = os.path.join("kairseq", "examples")
        if "build_ext" not in sys.argv[1:] and not os.path.exists(kairseq_examples):
            os.symlink(os.path.join("..", "examples"), kairseq_examples)

        package_data = {
            "kairseq": (
                get_files(kairseq_examples)
                + get_files(os.path.join("kairseq", "config"))
            )
        }
        do_setup(package_data)
    finally:
        if "build_ext" not in sys.argv[1:] and os.path.islink(kairseq_examples):
            os.unlink(kairseq_examples)
