.. role:: hidden
    :class: hidden-section

.. module:: kairseq.models

.. _Models:

Models
======

A Model defines the neural network's ``forward()`` method and encapsulates all
of the learnable parameters in the network. Each model also provides a set of
named *architectures* that define the precise network configuration (e.g.,
embedding dimension, number of layers, etc.).

Both the model type and architecture are selected via the ``--arch``
command-line argument. Once selected, a model may expose additional command-line
arguments for further configuration.

.. note::

    All kairseq Models extend :class:`BaseKairseqModel`, which in turn extends
    :class:`torch.nn.Module`. Thus any kairseq Model can be used as a
    stand-alone Module in other PyTorch code.


Convolutional Neural Networks (CNN)
-----------------------------------

.. module:: kairseq.models.fconv
.. autoclass:: kairseq.models.fconv.FConvModel
    :members:
.. autoclass:: kairseq.models.fconv.FConvEncoder
    :members:
    :undoc-members:
.. autoclass:: kairseq.models.fconv.FConvDecoder
    :members:


Long Short-Term Memory (LSTM) networks
--------------------------------------

.. module:: kairseq.models.lstm
.. autoclass:: kairseq.models.lstm.LSTMModel
    :members:
.. autoclass:: kairseq.models.lstm.LSTMEncoder
    :members:
.. autoclass:: kairseq.models.lstm.LSTMDecoder
    :members:


Transformer (self-attention) networks
-------------------------------------

.. module:: kairseq.models.transformer
.. autoclass:: kairseq.models.transformer.TransformerModel
    :members:
.. autoclass:: kairseq.models.transformer.TransformerEncoder
    :members:
.. autoclass:: kairseq.models.transformer.TransformerEncoderLayer
    :members:
.. autoclass:: kairseq.models.transformer.TransformerDecoder
    :members:
.. autoclass:: kairseq.models.transformer.TransformerDecoderLayer
    :members:


Adding new models
-----------------

.. currentmodule:: kairseq.models
.. autofunction:: kairseq.models.register_model
.. autofunction:: kairseq.models.register_model_architecture
.. autoclass:: kairseq.models.BaseKairseqModel
    :members:
    :undoc-members:
.. autoclass:: kairseq.models.KairseqEncoderDecoderModel
    :members:
    :undoc-members:
.. autoclass:: kairseq.models.KairseqEncoderModel
    :members:
    :undoc-members:
.. autoclass:: kairseq.models.KairseqLanguageModel
    :members:
    :undoc-members:
.. autoclass:: kairseq.models.KairseqMultiModel
    :members:
    :undoc-members:
.. autoclass:: kairseq.models.KairseqEncoder
    :members:
.. autoclass:: kairseq.models.CompositeEncoder
    :members:
.. autoclass:: kairseq.models.KairseqDecoder
    :members:


.. _Incremental decoding:

Incremental decoding
--------------------

.. autoclass:: kairseq.models.KairseqIncrementalDecoder
    :members:
    :undoc-members:
