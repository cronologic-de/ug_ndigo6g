.. _packet format:

Packet Format
=============

Packets are retrieved by :cpp:func:`ndigo6g12_read`. They are of type
:cpp:struct:`crono_packet`.

- Each hit on an ADC channel is stored in one packet. For ADC-packets.

- All TDC hits within the time given by 
  :cpp:member:`ndigo6g12_param_info::tdc_rollover_period` are stored in a single
  packet (stored in the payload data :cpp:member:`crono_packet::data`).
  The memory layout thereof is shown in 
  :numref:`Section %s<tdcpacket bit table>`.

.. toctree::
    :maxdepth: 2
    :caption: Contents

    constants
    utility
    bittable
    struct