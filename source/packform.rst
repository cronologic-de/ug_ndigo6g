Packet Format
=============

.. attention:: 

    This User Guide is under active development and is subject to major 
    changes.

Overview
--------
Packets are retrieved by :cpp:func:`ndigo6g12_read`. They are of type
:cpp:struct:`crono_packet`.

- Each hit on an ADC channel is stored in one packet. For ADC-packets.

- All TDC hits within the time given by 
  :cpp:member:`ndigo6g12_param_info::tdc_rollover_period` are stored in a single
  packet (stored in the payload data :cpp:member:`crono_packet::data`).
  The memory layout thereof is shown in 
  :numref:`Section %s<tdcpacket bit table>`.

.. _tdcpacket bit table:

:cpp:member:`crono_packet::data` encoding for TDC hits
------------------------------------------------------
+-------------+----+----+-----------------------------+---+---+---+---+---+-------------------+---+---+---+--------------------+
| **Bit**     | 31 | 30 | ...                         | 9 | 8 | 7 | 6 | 5 | 4                 | 3 | 2 | 1 | 0                  |
+-------------+----+----+-----------------------------+---+---+---+---+---+-------------------+---+---+---+--------------------+
| **Data**    | Timestamp                                     | TDC hit flags                 |Channel number                  |
+-------------+-----------------------------------------------+-------------------------------+--------------------------------+
| **Details** |The timestamp is relative to                   | See :ref:`here<tdchitflags>`  | | :code:`0x1`: TDC channel 1   |
|             |:cpp:member:`crono_packet::timestamp`          |                               | | :code:`0x2`: TDC channel 2   |
|             |and is given in units of                       |                               | | :code:`0x4`: TDC channel 3   |
|             |:cpp:member:`ndigo6g12_param_info::tdc_period`.|                               | | :code:`0x8`: TDC channel 4   |
|             |                                               |                               | | :code:`0xD`: Dummy data      |
|             |                                               |                               | | :code:`0xF`: Rollover marker |
+-------------+-----------------------------------------------+-------------------------------+--------------------------------+

Defines for `crono_packet`
--------------------------

.. _packettypes:
.. doxygengroup:: packettypes

.. doxygengroup:: packetflags

.. doxygengroup:: tdcpacketflags

.. _tdchitflags:

.. doxygengroup:: tdchitflags


Output Structure :cpp:`crono_packet`
------------------------------------
.. doxygenstruct:: crono_packet
   :members:


