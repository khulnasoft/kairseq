.. role:: hidden
    :class: hidden-section

.. _Criterions:

Criterions
==========

Criterions compute the loss function given the model and batch, roughly::

  loss = criterion(model, batch)

.. automodule:: kairseq.criterions
    :members:

.. autoclass:: kairseq.criterions.KairseqCriterion
    :members:
    :undoc-members:

.. autoclass:: kairseq.criterions.adaptive_loss.AdaptiveLoss
    :members:
    :undoc-members:
.. autoclass:: kairseq.criterions.composite_loss.CompositeLoss
    :members:
    :undoc-members:
.. autoclass:: kairseq.criterions.cross_entropy.CrossEntropyCriterion
    :members:
    :undoc-members:
.. autoclass:: kairseq.criterions.label_smoothed_cross_entropy.LabelSmoothedCrossEntropyCriterion
    :members:
    :undoc-members:
