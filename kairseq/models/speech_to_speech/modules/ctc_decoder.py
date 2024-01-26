# Copyright (c) Facebook, Inc. and its affiliates.
#
# This source code is licensed under the MIT license found in the
# LICENSE file in the root directory of this source tree.

from torch import nn

from kairseq.models import KairseqEncoder


class CTCDecoder(KairseqEncoder):
    def __init__(self, dictionary, in_dim):
        super().__init__(dictionary)
        self.proj = nn.Linear(in_dim, len(dictionary))

    def forward(self, src_tokens, src_lengths=None, **kwargs):
        encoder_out = self.proj(src_tokens)
        return {"encoder_out": encoder_out}
