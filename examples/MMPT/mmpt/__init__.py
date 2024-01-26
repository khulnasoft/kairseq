# Copyright (c) Facebook, Inc. and its affiliates.
#
# This source code is licensed under the MIT license found in the
# LICENSE file in the root directory of this source tree.
try:
    # kairseq user dir
    from .datasets import KairseqMMDataset
    from .losses import KairseqCriterion
    from .models import KairseqMMModel
    from .tasks import KairseqMMTask
except ImportError:
    pass
