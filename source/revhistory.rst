Revision History
================

Firmware
--------

1.25086 — 2025-04-03
    | Bugfix: Removed trigger dead time

1.24120 — 2024-04-30
    | Improved ADC/TDC synchronization
    | Added sample averaging modes AA/DD, AAAA/DDDD, and AADD
    | TiGer Updates
    | Internal optimizations
    | Bug fixes

5493 — 2023-10-30
    | Fixed bug related to level triggering
    | Fixed first packet being empty
    | Minor bug fixes

5467 — 2023-05-05
    | PCIe optimizations
    | Minor bug fixes

Driver
------
2.2.0 — 2025-04-03
    | Bugfix: Removed trigger dead time
    | Bugfix: Fixed :c:macro:`NDIGO6G12_MAX_PRECURSOR` for :ref:`Averaging Mode`
    
2.0.1 — 2024-07-17
    | Extensive revision of the application programming interface
    | Improved linux support
    | Improved documentation
    | Improved TDC and ADC synchronization

1.5.4 — 2024-07-13
    | Fixed 2 channel handling with trigger from opposite channel (trigger A on channel D)
    | Fixed timestamp uncertainty in lower bits


1.5.3 — 2024-07-07
    | Dynamic reconfiguration with .cronorom support

1.4.5 — 2023-01-23
    | Crono kernel driver update to v1.4.2
    | Added support for revision 3 boards
    | Minor bug fixes
    | Support for 32-bit OS discontinued

1.4.0 — 2022-08-18
    | Added support for external 10 MHz reference on slot bracket

1.3.0 — 2022-05-25
    | Added support for Averager


User Guide
----------
1.4.0-dev — TBD
    | Updated documentation of :cpp:member:`ndigo6g12_configuration::output_mode`
    | Updated :cpp:member:`ndigo6g12_param_info::adc_sample_delay` docstring
    | Documented possible baseline drift due to the AC coupling
    | Updated :numref:`Figures %s<Fig 2.5>` and :numref:`%s<Fig 2.6>` to work in dark mode
    | Improved Averager documentation

1.3.0 — 2025-04-10
    | Documented firmware update procedure
    | Documented TDC calibration procedure

1.2.0 — 2025-04-02
    | Documented minimal packet length
    | Moved alert and device-state defines to corresponding documentation section
    | Updated Erratum

1.1.0 — 2025-01-14
    | Added :numref:`Section %s<maxratings>`

1.0.1 — 2024-10-22
    | Improved :numref:`Figure %s<fig hardware picture>`

1.0.0 — 2024-10-17
    | Added digitizer characteristics
    | Added chapter on TiGer
    | Added :doc:`erratum`
    | Fixed gating documentation
    | Many corrections

0.2.1 — 2024-10-01
    | Corrections in Export Control

0.2.0 — 2024-10-01
    | Added gating examples
    | Updated Export Control

0.1.4 — 2024-08-06
    | Added figures for the :ref:`Trigger Matrix<fig triggermatrix>` and
      :ref:`Gating Blocks<fig gatingblock>`.

0.1.3 — 2024-08-01
    | Added documentation for clock connections
    | Added link to current user guide example code
    | Removed clutter from the APIs "ON THIS PAGE" sidebar
    | Updated C++ example
    | General improvements

0.1.2 — 2024-07-17
    | Renamed FPGA0/1 to TRG/GATE
    | Restructured API documentation
    | Expanded documentation on Packet Format

0.1.1 — 2024-07-16
    | Corrected values in introduction
    | Improved phrasing throughout

0.1.0 — 2024-07-11
    | Initial release