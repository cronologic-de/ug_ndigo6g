.. _tdcpacket bit table:

:cpp:member:`crono_packet::data` encoding for TDC hits
------------------------------------------------------

.. only:: html

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

.. raw:: latex

    \begingroup
    \renewcommand\tabularxcolumn[1]{>{\Centering}p{#1}}
    \begin{tabularx}{\textwidth}{|l||X|X|c|X|X|X|X|X|X|X|X|X|X|}
        \hline
        Bit & 31 & 30 & \dots & 9 & 8 & 7 & 6 & 5 & 4 & 3 & 2 & 1 & 0 \\
        \hline
        Data & \multicolumn{5}{c|}{Timestamp} & \multicolumn{4}{c|}{TDC hit flags} & \multicolumn{4}{c|}{Channel number} \\
        \hline
    \end{tabularx}
    \endgroup

.. only:: latex

    Details:

    - The timestamp is relative to
      :cpp:member:`crono_packet::timestamp`
      and is given in units of
      :cpp:member:`ndigo6g12_param_info::tdc_period`.
    - See :numref:`Section %s<tdchitflags>` for an overview of the TDC hit flags.
    - | The channel numbers are:
      | :code:`0x1`: TDC channel 1
      | :code:`0x2`: TDC channel 2
      | :code:`0x4`: TDC channel 3
      | :code:`0x8`: TDC channel 4
      | :code:`0xD`: Dummy data
      | :code:`0xF`: Rollover marker