.. _packet format:

Packet Format
=============

Packets are retrieved by :cpp:func:`ndigo6g12_read`. They are of type
:cpp:struct:`crono_packet`.

- Each hit on an ADC channel is stored in one packet.
  Two consecutive packets on the same ADC channel must have a minimum distance
  of eight ADC samples. The format of the payload data (see 
  :cpp:member:`crono_packet::data`) is explained in
  :numref:`Section %s<adc data format>`.

- All TDC hits within the time given by
  :cpp:member:`ndigo6g12_param_info::tdc_rollover_period` are stored in a single
  packet (stored in the payload data). The memory layout thereof is shown in
  :numref:`Section %s<tdcpacket bit table>`.


.. raw:: html

    <h2>Contents of this Chapter</h2>

.. toctree::
    :maxdepth: 1

    constants
    struct
    utility
    adcdata
    tdcdata