Driver Programming API
======================

Constants
---------

.. doxygengroup:: constants
    :content-only:


Initialization
--------------

Functions
~~~~~~~~~

.. doxygengroup:: initfuncts
    :content-only:

Structure ndigo6g12_init_parameters
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. doxygenstruct:: ndigo6g12_init_parameters
    :members:
    :members-only:



Status information
------------------

The driver provides functions to retrieve detailed information on the type
of board, it's configuration, settings and state. The information is split
according to its scope and the computational requirements to query the
information from the board.

Defines
~~~~~~~

.. doxygengroup:: devicestates
    :content-only:


Functions
~~~~~~~~~

.. doxygengroup:: statfuncts
    :content-only:


Structure ndigo6g12_static_info
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. doxygenstruct:: ndigo6g12_static_info
    :members:
    :members-only:


Structure ndigo6g12_param_info
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. doxygenstruct:: ndigo6g12_param_info
    :members:
    :members-only:


Structure ndigo6g12_fast_info
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. doxygenstruct:: ndigo6g12_fast_info
    :members:
    :members-only:



Configuration
-------------

ADC mode defines
~~~~~~~~~~~~~~~~

.. doxygengroup:: adcdefs
    :content-only:

Trigger source defines
~~~~~~~~~~~~~~~~~~~~~~

.. doxygengroup:: sourcedefs
    :content-only:

Gate defines
~~~~~~~~~~~~

.. doxygengroup:: gatedefs
    :content-only:


Configuration setup
~~~~~~~~~~~~~~~~~~~

.. doxygengroup:: conffuncts
    :content-only:


Structure ndigo6g12_configuration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. doxygenstruct:: ndigo6g12_configuration
    :members:
    :members-only:


Structure ndigo6g12_trigger
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. doxygenstruct:: ndigo6g12_trigger
    :members:
    :members-only:


Structure ndigo6g12_trigger_block
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. doxygenstruct:: ndigo6g12_trigger_block
    :members:
    :members-only:


Structure ndigo6g12_gating_block
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. doxygenstruct:: ndigo6g12_gating_block
    :members:
    :members-only:

Structure ndigo6g12_averager_configuration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. doxygenstruct:: ndigo6g12_averager_configuration
    :members:
    :members-only:

Structure ndigo6g12_tdc_configuration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. doxygenstruct:: ndigo6g12_tdc_configuration
    :members:
    :members-only:

Structure ndigo6g12_tdc_channel
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. doxygenstruct:: ndigo6g12_tdc_channel
    :members:
    :members-only:

Structure ndigo6g12_tdc_tiger_block
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. doxygenstruct:: ndigo6g12_tdc_tiger_block
    :members:
    :members-only:


Runtime control
~~~~~~~~~~~~~~~

.. doxygengroup:: runtime
    :content-only:


Readout
-------

Error code defines
~~~~~~~~~~~~~~~~~~

.. doxygengroup:: packflags
    :content-only:


Functions
~~~~~~~~~

.. doxygengroup:: readout
    :content-only:

.. doxygengroup:: errorfuncts
    :content-only:

.. doxygengroup:: pciefuncts
    :content-only:

Input structure ndigo6g12_read_in
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. doxygenstruct:: ndigo6g12_read_in
    :members:
    :members-only:

Output structure ndigo6g12_read_out
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. doxygenstruct:: ndigo6g12_read_out
    :members:
    :members-only:


Other functions
---------------

.. doxygenfunction:: ndigo6g12_device_state_to_str