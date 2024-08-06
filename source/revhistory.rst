Revision History
================

Firmware
--------
24120 |emdash| 2024-04-30
    | Improved ADC/TDC synchronisation
    | Added sample averaging modes AA/DD, AAAA/DDDD, and AADD
    | TiGer Updates
    | Internal optimizations
    | Bug fixes

5493 |emdash| 2023-10-30
    | Fixed bug related to level triggering
    | Fixed first packet being empty
    | Minor bug fixes

5467 |emdash| 2023-05-05
    | PCIe optimizations
    | Minor bug fixes

5444 |emdash| 2023-01-16

Driver
------
2.0.1 |emdash| 2024-07-17
    | Extensive revision of the application programming interface
    | Improved linux support
    | Improved documentation
    | Improved TDC and ADC synchronisation

1.5.4 |emdash| 2024-07-13
    | Fixed 2 channel handling with trigger from opposite channel (trigger A on channel D)
    | Fixed timestamp uncertainty in lower bits


1.5.3 |emdash| 2024-07-07
    | Dynamic reconfiguration with .cronorom support

1.4.5 |emdash| 2023-01-23
    | Crono kernel driver update to v1.4.2
    | Added support for revision 3 boards
    | Minor bug fixes
    | Support for 32-bit OS discontinued

1.4.0 |emdash| 2022-08-18
    | Added support for external 10 MHz reference on slot bracket

1.3.0 |emdash| 2022-05-25
    | Added support for Averager


User Guide
----------
|version| |emdash| 2024-08-06
    | Added figures for the :ref:`Trigger Matrix<fig triggermatrix>` and
      :ref:`Gating Blocks<fig gatingblock>`.
    | Added gating examples

0.1.3 |emdash| 2024-08-01
    | Added documentation for clock connections
    | Added link to current user guide example code
    | Removed clutter from the APIs "ON THIS PAGE" sidebar
    | Updated C++ example
    | General improvements

0.1.2 |emdash| 2024-07-17
    | Renamed FPGA0/1 to TRG/GATE
    | Restructured API documentation
    | Expanded documentation on Packet Format

0.1.1 |emdash| 2024-07-16
    | Corrected values in introduction
    | Improved phrasing throughout

0.1.0 |emdash| 2024-07-11
    | Initial release