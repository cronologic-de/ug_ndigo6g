.. _packet format:

Packet Format
=============

Packets are retrieved by :cpp:func:`ndigo6g12_read`. They are of type
:cpp:struct:`crono_packet`.

- Each hit on an ADC channel is stored in one packet.
  The format of the payload data (see :cpp:member:`crono_packet::data`)
  is explained in :numref:`Section %s<adc data format>`.

- All TDC hits within the time given by
  :cpp:member:`ndigo6g12_param_info::tdc_rollover_period` are stored in a single
  packet (stored in the payload data). The memory layout thereof is shown in
  :numref:`Section %s<tdcpacket bit table>`.


.. _min packet length:

Minimal Packet Length
---------------------
Packets have a minimal length, which depends on the
:cpp:member:`ndigo6g12_static_info::application_type` in use (see also
:doc:`../functionality/adc_modes`).

The minimal lengths are:

- 4 :math:`\times` 8 Samples (20 ns) @ 1.6 Gsps (4-Channel Mode)
- 3 :math:`\times` 16 Samples (15 ns) @ 3.2 Gsps (2-Channel Mode)
- 3 :math:`\times` 32 Samples (15 ns) @ 6.4 Gsps (1-Channel Mode)

.. raw:: html

    <h2>Contents of this Chapter</h2>

.. toctree::
    :maxdepth: 1

    constants
    struct
    utility
    adcdata
    tdcdata