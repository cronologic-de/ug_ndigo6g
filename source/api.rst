Driver Programming API
======================

The API is a DLL with C linkage.
Declarations of the interface are found in *ndigo6g12_interface.h*.

This chapter provides an overview of the provided API functionality.

.. Typedefs
.. --------

.. .. doxygentypedef:: crono_bool_t

Constants
---------

General
~~~~~~~

.. doxygengroup:: constants

Return values
~~~~~~~~~~~~~

.. doxygengroup:: funcreturns


Initialization
--------------

To use the Ndigo6G12, it first needs to be initialized. This is done by
calling :code:`ndigo6g12_init()`. The device must first be initialized by
with a set of default parameters, as provided by
:code:`ndigo6g12_get_default_init_parameters`. The initialization parameters
are of type :code:`ndigo6g12_init`. Information on the current
device will be stored as type :code:`ndigo6g12_device`.

Constants for clock setup 
~~~~~~~~~~~~~~~~~~~~~~~~~

.. doxygengroup:: clockmodes

Functions for initialization
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. doxygengroup:: initfuncts
    :content-only:

Structures for initialization
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. doxygengroup:: initstructs
    :content-only:
    :members:
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

Functions for information retrieval
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. doxygengroup:: statfuncts
    :content-only:

Structures for status information
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. doxygengroup:: infostructs
    :content-only:
    :members:

Configuration
-------------

Constants
~~~~~~~~~

ADC mode
^^^^^^^^

.. doxygengroup:: adcdefs

Trigger source
^^^^^^^^^^^^^^

.. doxygengroup:: sourcedefs


Trigger gates
^^^^^^^^^^^^^
.. doxygengroup:: gatedefs

Trigger blocks
^^^^^^^^^^^^^^
.. doxygengroup:: triggerblockdefs


Configuration setup
~~~~~~~~~~~~~~~~~~~

.. doxygengroup:: conffuncts
    :content-only:

.. _api confstructs:

Structures for configuration 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. doxygengroup:: confstructs
    :members:
    :undoc-members:
    :content-only:


Runtime control
~~~~~~~~~~~~~~~

.. doxygengroup:: runtimefuncts
    :content-only:


Readout
-------

Constants for error codes
~~~~~~~~~~~~~~~~~~~~~~~~~

.. doxygengroup:: packflags

Constants for PCIe information
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. doxygengroup:: pciecorrectableerrors
.. doxygengroup:: pcieuncorrectableerrors
.. doxygengroup:: pcieclearflags


Functions for readout
~~~~~~~~~~~~~~~~~~~~~

.. doxygengroup:: readfuncts
    :content-only:


Structures for readout
~~~~~~~~~~~~~~~~~~~~~~

.. doxygengroup:: readstructs
    :members:
    :content-only:

