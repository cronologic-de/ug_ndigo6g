Driver Programming API
======================

Constants
---------

.. doxygengroup:: constants


Initialization
--------------

.. . Functions
.. . ~~~~~~~~~

.. doxygengroup:: initfuncts

.. . Structure ndigo6g12_init_parameters
.. . ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. doxygenstruct:: ndigo6g12_init_parameters
    :members:



Status information
------------------

The driver provides functions to retrieve detailed information on the type
of board, it's configuration, settings and state. The information is split
according to its scope and the computational requirements to query the
information from the board.

.. . Defines
.. . ~~~~~~~

.. doxygengroup:: devicestates


.. . Functions
.. . ~~~~~~~~~

.. doxygengroup:: statfuncts


.. . Structure ndigo6g12_static_info
.. . ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. doxygenstruct:: ndigo6g12_static_info
    :members:


.. . Structure ndigo6g12_param_info
.. . ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. doxygenstruct:: ndigo6g12_param_info
    :members:


.. . Structure ndigo6g12_fast_info
.. . ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. doxygenstruct:: ndigo6g12_fast_info
    :members:



Configuration
-------------

.. . ADC mode defines
.. . ~~~~~~~~~~~~~~~~

.. doxygengroup:: adcdefs

.. . Trigger source defines
.. . ~~~~~~~~~~~~~~~~~~~~~~

.. doxygengroup:: sourcedefs

.. . Gate defines
.. . ~~~~~~~~~~~~

.. doxygengroup:: gatedefs


.. . Configuration setup
.. . ~~~~~~~~~~~~~~~~~~~

.. doxygengroup:: conffuncts


.. . Structure ndigo6g12_configuration
.. . ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. doxygenstruct:: ndigo6g12_configuration
    :members:


.. . Structure ndigo6g12_trigger
.. . ~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. doxygenstruct:: ndigo6g12_trigger
    :members:


.. . Structure ndigo6g12_trigger_block
.. . ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. doxygenstruct:: ndigo6g12_trigger_block
    :members:


.. . Structure ndigo6g12_gating_block
.. . ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. doxygenstruct:: ndigo6g12_gating_block
    :members:

.. . Structure ndigo6g12_averager_configuration
.. . ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. doxygenstruct:: ndigo6g12_averager_configuration
    :members:

.. . Structure ndigo6g12_tdc_configuration
.. . ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. doxygenstruct:: ndigo6g12_tdc_configuration
    :members:

.. . Structure ndigo6g12_tdc_channel
.. . ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. doxygenstruct:: ndigo6g12_tdc_channel
    :members:

.. . Structure ndigo6g12_tdc_tiger_block
.. . ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. doxygenstruct:: ndigo6g12_tdc_tiger_block
    :members:


.. . Runtime control
.. . ~~~~~~~~~~~~~~~

.. doxygengroup:: runtime


Readout
-------

.. . Error code defines
.. . ~~~~~~~~~~~~~~~~~~

.. doxygengroup:: packflags


.. Functions
.. ~~~~~~~~~

.. doxygengroup:: readout

.. doxygengroup:: errorfuncts

.. doxygengroup:: pciefuncts

.. Input structure ndigo6g12_read_in
.. ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. doxygenstruct:: ndigo6g12_read_in
    :members:

.. Output structure ndigo6g12_read_out
.. ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. doxygenstruct:: ndigo6g12_read_out
    :members:


Other functions
---------------

.. doxygenfunction:: ndigo6g12_device_state_to_str