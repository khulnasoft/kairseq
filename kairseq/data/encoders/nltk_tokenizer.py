# Copyright (c) Facebook, Inc. and its affiliates.
#
# This source code is licensed under the MIT license found in the
# LICENSE file in the root directory of this source tree.

from kairseq.data.encoders import register_tokenizer
from kairseq.dataclass import KairseqDataclass


@register_tokenizer("nltk", dataclass=KairseqDataclass)
class NLTKTokenizer(object):
    def __init__(self, *unused):
        try:
            from nltk.tokenize import word_tokenize

            self.word_tokenize = word_tokenize
        except ImportError:
            raise ImportError("Please install nltk with: pip install nltk")

    def encode(self, x: str) -> str:
        return " ".join(self.word_tokenize(x))

    def decode(self, x: str) -> str:
        return x
