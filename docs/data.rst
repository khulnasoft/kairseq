.. role:: hidden
    :class: hidden-section

.. module:: kairseq.data

Data Loading and Utilities
==========================

.. _datasets:

Datasets
--------

**Datasets** define the data format and provide helpers for creating
mini-batches.

.. autoclass:: kairseq.data.KairseqDataset
    :members:
.. autoclass:: kairseq.data.LanguagePairDataset
    :members:
.. autoclass:: kairseq.data.MonolingualDataset
    :members:

**Helper Datasets**

These datasets wrap other :class:`kairseq.data.KairseqDataset` instances and
provide additional functionality:

.. autoclass:: kairseq.data.BacktranslationDataset
    :members:
.. autoclass:: kairseq.data.ConcatDataset
    :members:
.. autoclass:: kairseq.data.ResamplingDataset
    :members:
.. autoclass:: kairseq.data.RoundRobinZipDatasets
    :members:
.. autoclass:: kairseq.data.TransformEosDataset
    :members:


Dictionary
----------

.. autoclass:: kairseq.data.Dictionary
    :members:


Iterators
---------

.. autoclass:: kairseq.data.CountingIterator
    :members:
.. autoclass:: kairseq.data.EpochBatchIterator
    :members:
.. autoclass:: kairseq.data.GroupedIterator
    :members:
.. autoclass:: kairseq.data.ShardedIterator
    :members:
