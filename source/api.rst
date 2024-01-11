Driver Programming API
======================

The API is a DLL with C linkage.
Declarations of the interface are found in *ndigo6g12_interface.h*.

This chapter provides an overview of the provided API functionality.

Constants
---------

.. doxygengroup:: constants
    :content-only:


Initialization
--------------

To use the Ndigo6G12, it first needs to be initialized. This is done by
calling :code:`ndigo6g12_init()`. The device must first be initialized by
with a set of default parameters, as provided by
:code:`ndigo6g12_get_default_init_parameters`. The initialization parameters
are of type :code:`ndigo6g12_init`. Information on the current
device will be stored as type :code:`ndigo6g12_device`.

Initialization setup
~~~~~~~~~~~~~~~~~~~~

.. doxygengroup:: initfuncts
    :content-only:

Structures
~~~~~~~~~~

.. doxygenstruct:: ndigo6g12_init_parameters
    :members:

.. doxygenstruct:: ndigo6g12_device
    :undoc-members:

Status information
------------------

The driver provides functions to retrieve detailed information on the type
of board, it's configuration, settings and state. The information is split
according to its scope and the computational requirements to query the
information from the board.

Constants defining device states
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The device may be in one of the following states.

.. doxygengroup:: devicestates
    :content-only:

Structures
~~~~~~~~~~

.. doxygenstruct:: ndigo6g12_static_info
    :members:

.. doxygenstruct:: ndigo6g12_param_info
    :members:

.. doxygenstruct:: ndigo6g12_fast_info
    :members:



Configuration
-------------

Constants for ADC mode
~~~~~~~~~~~~~~~~~~~~~~

.. doxygengroup:: adcdefs

Constants for trigger source
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. doxygengroup:: sourcedefs


Constants for trigger gates
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. doxygengroup:: gatedefs


Configuration setup
~~~~~~~~~~~~~~~~~~~

.. doxygengroup:: conffuncts
    :content-only:

Structures
~~~~~~~~~~

.. doxygenstruct:: ndigo6g12_configuration
    :members:

.. doxygenstruct:: ndigo6g12_trigger
    :members:


.. doxygenstruct:: ndigo6g12_trigger_block
    :members:

.. doxygenstruct:: ndigo6g12_gating_block
    :members:

.. doxygenstruct:: ndigo6g12_averager_configuration
    :members:

.. doxygenstruct:: ndigo6g12_tdc_configuration
    :members:

.. doxygenstruct:: ndigo6g12_tdc_channel
    :members:

.. doxygenstruct:: ndigo6g12_tdc_tiger_block
    :members:


Runtime control
~~~~~~~~~~~~~~~

.. doxygengroup:: runtime


Readout
-------

Constants for error codes
~~~~~~~~~~~~~~~~~~~~~~~~~

.. doxygengroup:: packflags


Readout setup
~~~~~~~~~~~~~

.. doxygengroup:: readout

.. doxygengroup:: errorfuncts

.. doxygengroup:: pciefuncts


Structures
~~~~~~~~~~

.. doxygenstruct:: ndigo6g12_read_in
    :members:

.. doxygenstruct:: ndigo6g12_read_out
    :members:


Other functions
---------------

.. doxygenfunction:: ndigo6g12_device_state_to_str