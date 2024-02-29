Initialization
--------------
To use a Ndigo6G-12 board, it first needs to be initialized. This is done by
calling :cpp:func:`ndigo6g12_init`. The device must first be initialized by
with a set of default parameters, as provided by
:c:macro:`ndigo6g12_get_default_init_parameters`. The initialization 
parameters are of type :cpp:struct:`ndigo6g12_init_parameters`. Information on 
the current device will be stored as type :cpp:struct:`ndigo6g12_device`.

.. doxygengroup:: initfuncts
    :content-only:

.. doxygengroup:: initstructs
    :content-only:
    :members:
    :undoc-members:
