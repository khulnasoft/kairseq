.. role:: hidden
    :class: hidden-section

.. module:: kairseq.tasks

.. _Tasks:

Tasks
=====

Tasks store dictionaries and provide helpers for loading/iterating over
Datasets, initializing the Model/Criterion and calculating the loss.

Tasks can be selected via the ``--task`` command-line argument. Once selected, a
task may expose additional command-line arguments for further configuration.

Example usage::

    # setup the task (e.g., load dictionaries)
    task = kairseq.tasks.setup_task(args)

    # build model and criterion
    model = task.build_model(args)
    criterion = task.build_criterion(args)

    # load datasets
    task.load_dataset('train')
    task.load_dataset('valid')

    # iterate over mini-batches of data
    batch_itr = task.get_batch_iterator(
        task.dataset('train'), max_tokens=4096,
    )
    for batch in batch_itr:
        # compute the loss
        loss, sample_size, logging_output = task.get_loss(
            model, criterion, batch,
        )
        loss.backward()


Translation
-----------

.. autoclass:: kairseq.tasks.translation.TranslationTask

.. _language modeling:

Language Modeling
-----------------

.. autoclass:: kairseq.tasks.language_modeling.LanguageModelingTask


Adding new tasks
----------------

.. autofunction:: kairseq.tasks.register_task
.. autoclass:: kairseq.tasks.KairseqTask
    :members:
    :undoc-members:
