# Copyright (c) Facebook, Inc. and its affiliates.
#
# This source code is licensed under the MIT license found in the
# LICENSE file in the root directory of this source tree.

from dataclasses import dataclass, field

from kairseq import file_utils
from kairseq.data.encoders import register_bpe
from kairseq.dataclass import KairseqDataclass


@dataclass
class fastBPEConfig(KairseqDataclass):
    bpe_codes: str = field(default="???", metadata={"help": "path to fastBPE BPE"})


@register_bpe("fastbpe", dataclass=fastBPEConfig)
class fastBPE(object):
    def __init__(self, cfg):
        if cfg.bpe_codes is None:
            raise ValueError("--bpe-codes is required for --bpe=fastbpe")
        codes = file_utils.cached_path(cfg.bpe_codes)
        try:
            import fastBPE

            self.bpe = fastBPE.fastBPE(codes)
            self.bpe_symbol = "@@ "
        except ImportError:
            raise ImportError("Please install fastBPE with: pip install fastBPE")

    def encode(self, x: str) -> str:
        return self.bpe.apply([x])[0]

    def decode(self, x: str) -> str:
        return (x + " ").replace(self.bpe_symbol, "").rstrip()
