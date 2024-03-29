#!/usr/bin/env python3 -u
# Copyright (c) Facebook, Inc. and its affiliates.
#
# This source code is licensed under the MIT license found in the
# LICENSE file in the root directory of this source tree.
"""
Legacy entry point. Use kairseq_cli/train.py or kairseq-train instead.
"""

from kairseq_cli.train import cli_main


if __name__ == "__main__":
    cli_main()
