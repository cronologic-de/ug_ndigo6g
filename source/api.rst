Driver Programming API
======================

.. attention:: 

    This User Guide is under active development and is subject to major 
    changes.


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
    :content-only:

Function return values
~~~~~~~~~~~~~~~~~~~~~~

.. doxygengroup:: funcreturns



Initialization
--------------
To use the Ndigo6G12, it first needs to be initialized. This is done by
calling :code:`ndigo6g12_init()`. The device must first be initialized by
with a set of default parameters, as provided by
:code:`ndigo6g12_get_default_init_parameters`. The initialization parameters
are of type :code:`ndigo6g12_init`. Information on the current
device will be stored as type :code:`ndigo6g12_device`.

Defines used for Initialization
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Clock modes
^^^^^^^^^^^
.. doxygengroup:: clockmodes

Application types
^^^^^^^^^^^^^^^^^
.. doxygengroup:: apptypes

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

Defines
~~~~~~~
Device states
^^^^^^^^^^^^^
The device may be in one of the following states.

.. doxygengroup:: devicestates

Alerts
^^^^^^
.. doxygengroup:: alertdefs

PCIe information
^^^^^^^^^^^^^^^^
.. doxygengroup:: pciecorrectableerrors
.. doxygengroup:: pcieuncorrectableerrors
.. doxygengroup:: pcieclearflags

    


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

Defines
~~~~~~~

ADC mode
^^^^^^^^
.. doxygengroup:: adcdefs

External trigger source
^^^^^^^^^^^^^^^^^^^^^^^
.. doxygengroup:: triggerdefs

Trigger source for gating blocks
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. doxygengroup:: sourcedefs

Trigger gates
^^^^^^^^^^^^^
.. doxygengroup:: gatedefs

Trigger blocks
^^^^^^^^^^^^^^
.. doxygengroup:: triggerblockdefs

DC offsets
^^^^^^^^^^
.. doxygengroup:: defdcoffset

Output modes
^^^^^^^^^^^^
.. doxygengroup:: outputdefs


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


Functions for readout
~~~~~~~~~~~~~~~~~~~~~

.. doxygengroup:: readfuncts
    :content-only:

Structures for readout
~~~~~~~~~~~~~~~~~~~~~~

.. doxygengroup:: readstructs
    :members: