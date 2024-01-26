.. _Command-line Tools:

Command-line Tools
==================

Kairseq provides several command-line tools for training and evaluating models:

- :ref:`kairseq-preprocess`: Data pre-processing: build vocabularies and binarize training data
- :ref:`kairseq-train`: Train a new model on one or multiple GPUs
- :ref:`kairseq-generate`: Translate pre-processed data with a trained model
- :ref:`kairseq-interactive`: Translate raw text with a trained model
- :ref:`kairseq-score`: BLEU scoring of generated translations against reference translations
- :ref:`kairseq-eval-lm`: Language model evaluation


.. _kairseq-preprocess:

kairseq-preprocess
~~~~~~~~~~~~~~~~~~
.. automodule:: kairseq_cli.preprocess

    .. argparse::
        :module: kairseq.options
        :func: get_preprocessing_parser
        :prog: kairseq-preprocess


.. _kairseq-train:

kairseq-train
~~~~~~~~~~~~~
.. automodule:: kairseq_cli.train

    .. argparse::
        :module: kairseq.options
        :func: get_training_parser
        :prog: kairseq-train


.. _kairseq-generate:

kairseq-generate
~~~~~~~~~~~~~~~~
.. automodule:: kairseq_cli.generate

    .. argparse::
        :module: kairseq.options
        :func: get_generation_parser
        :prog: kairseq-generate


.. _kairseq-interactive:

kairseq-interactive
~~~~~~~~~~~~~~~~~~~
.. automodule:: kairseq_cli.interactive

    .. argparse::
        :module: kairseq.options
        :func: get_interactive_generation_parser
        :prog: kairseq-interactive


.. _kairseq-score:

kairseq-score
~~~~~~~~~~~~~
.. automodule:: kairseq_cli.score

    .. argparse::
        :module: kairseq_cli.score
        :func: get_parser
        :prog: kairseq-score


.. _kairseq-eval-lm:

kairseq-eval-lm
~~~~~~~~~~~~~~~
.. automodule:: kairseq_cli.eval_lm

    .. argparse::
        :module: kairseq.options
        :func: get_eval_lm_parser
        :prog: kairseq-eval-lm
