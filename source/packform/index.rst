.. _packet format:

Packet Format
=============

Packets are retrieved by :cpp:func:`ndigo6g12_read`. They are of type
:cpp:struct:`crono_packet`.

- Each hit on an ADC channel is stored in one packet.
  The format of the payload data (see :cpp:member:`crono_packet::data`)
  is explained in :doc:`adcdata`.

- All TDC hits within the time given by
  :cpp:member:`ndigo6g12_param_info::tdc_rollover_period` are stored in a single
  packet (stored in the payload data). The memory layout thereof is shown in
  :doc:`tdcdata`.

.. note::

    The minimum packet length depends on the application type. See
    :doc:`../functionality/adc_modes` for details.



.. raw:: html

    <h2>Contents of this Chapter</h2>

.. toctree::
    :maxdepth: 1

    struct
    utility
    adcdata
    tdcdata
    avrgdata
