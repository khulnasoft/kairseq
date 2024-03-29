# Copyright (c) Facebook, Inc. and its affiliates.
#
# This source code is licensed under the MIT license found in the
# LICENSE file in the root directory of this source tree.


from dataclasses import dataclass

from kairseq.dataclass import KairseqDataclass
from kairseq.scoring import BaseScorer, register_scorer


@dataclass
class ChrFScorerConfig(KairseqDataclass):
    pass


@register_scorer("chrf", dataclass=ChrFScorerConfig)
class ChrFScorer(BaseScorer):
    def __init__(self, args):
        super(ChrFScorer, self).__init__(args)
        import sacrebleu

        self.sacrebleu = sacrebleu

    def add_string(self, ref, pred):
        self.ref.append(ref)
        self.pred.append(pred)

    def score(self, order=4):
        return self.result_string(order).score

    def result_string(self, order=4):
        if order != 4:
            raise NotImplementedError
        return self.sacrebleu.corpus_chrf(self.pred, [self.ref]).format()
