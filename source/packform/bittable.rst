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