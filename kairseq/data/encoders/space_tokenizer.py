# Copyright (c) Facebook, Inc. and its affiliates.
#
# This source code is licensed under the MIT license found in the
# LICENSE file in the root directory of this source tree.

import re

from kairseq.data.encoders import register_tokenizer
from kairseq.dataclass import KairseqDataclass


@register_tokenizer("space", dataclass=KairseqDataclass)
class SpaceTokenizer(object):
    def __init__(self, *unused):
        self.space_tok = re.compile(r"\s+")

    def encode(self, x: str) -> str:
        return self.space_tok.sub(" ", x)

    def decode(self, x: str) -> str:
        return x
