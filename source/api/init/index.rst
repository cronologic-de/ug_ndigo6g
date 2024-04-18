Initialization
--------------
To use a Ndigo6G-12 board, it first needs to be initialized. This is done by
calling :cpp:func:`ndigo6g12_init`.
The initialization parameters necessary for :cpp:func:`ndigo6g12_init` are
provided in the :cpp:struct:`ndigo6g12_init_parameters` struct.

The general procedure for initialization is as follows:

1. Load a default set of initialization parameters using
   :c:macro:`ndigo6g12_get_default_init_parameters`.
2. If necessary, adjust default parameters to your specific needs.
3. Initialize the Ndigo6G-12 board using :cpp:func:`ndigo6g12_init`.
4. Check that the initialization was successful. If so, the return value
   of :cpp:func:`ndigo6g12_init` is :c:macro:`CRONO_OK`.

Information on
the current device will be stored as type :cpp:struct:`ndigo6g12_device`.

.. toctree::
    :caption: Contents
    :maxdepth: 2

    defines
    functions
    structures

