Scenarios
=====


here are some main user flows in clinicult system

Client on-boarding
------------

This scenario describe the acceptance of new customer to the clinic. in this flow we have two options:
one case is that user already exists in clinic data, and the second one is the patient is new.

In both cases we will search for the Patient in the Search bar. if Patient exists, we can update his visit in the clinic. 
if Patient not exists in clinic data, we will have a form that add new Patient to our system, and after Patient added, we can update his visit.


.. code-block:: console

   (.venv) $ pip install lumache

Creating recipes
----------------

To retrieve a list of random ingredients,
you can use the ``lumache.get_random_ingredients()`` function:

.. autofunction:: lumache.get_random_ingredients

The ``kind`` parameter should be either ``"meat"``, ``"fish"``,
or ``"veggies"``. Otherwise, :py:func:`lumache.get_random_ingredients`
will raise an exception.

.. autoexception:: lumache.InvalidKindError

For example:

>>> import lumache
>>> lumache.get_random_ingredients()
['shells', 'gorgonzola', 'parsley']

