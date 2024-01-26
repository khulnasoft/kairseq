# Copyright (c) Facebook, Inc. and its affiliates.
#
# This source code is licensed under the MIT license found in the
# LICENSE file in the root directory of this source tree.
"""isort:skip_file"""

import os
import sys

try:
    from .version import __version__  # noqa
except ImportError:
    version_txt = os.path.join(os.path.dirname(__file__), "version.txt")
    with open(version_txt) as f:
        __version__ = f.read().strip()

__all__ = ["pdb"]

# backwards compatibility to support `from kairseq.X import Y`
from kairseq.distributed import utils as distributed_utils
from kairseq.logging import meters, metrics, progress_bar  # noqa

sys.modules["kairseq.distributed_utils"] = distributed_utils
sys.modules["kairseq.meters"] = meters
sys.modules["kairseq.metrics"] = metrics
sys.modules["kairseq.progress_bar"] = progress_bar

# initialize hydra
from kairseq.dataclass.initialize import hydra_init

hydra_init()

import kairseq.criterions  # noqa
import kairseq.distributed  # noqa
import kairseq.models  # noqa
import kairseq.modules  # noqa
import kairseq.optim  # noqa
import kairseq.optim.lr_scheduler  # noqa
import kairseq.pdb  # noqa
import kairseq.scoring  # noqa
import kairseq.tasks  # noqa
import kairseq.token_generation_constraints  # noqa

import kairseq.benchmark  # noqa
import kairseq.model_parallel  # noqa
