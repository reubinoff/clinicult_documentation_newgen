Scenarios
=====


Patient state update
------------
Once patient has start his visit in the clinic, he may see couple of medical entities. 
each entity has option to change the pearson who need to check the patient. changing the medicak entity is similar to change his visit state.
The patien can change his state couple of times, and can visit in the same state more then one time.
for example, at the begining, the patient will see the nurse. then he can move to the doctor care, and then come back to the nurse.

each state will be recorded and will update within his medical file.
in addition, all those update will be stored in his visit event, and may be query later.
Each medical update his medical file as mentioed before.


Patient state update
------------

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

