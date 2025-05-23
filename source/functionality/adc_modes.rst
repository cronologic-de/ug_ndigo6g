.. _ADC Modes:

ADC Modes
~~~~~~~~~

The ADC quantizes the input signal using 12 bits. By default, these are mapped
to signed 16 bit (for more details, see :numref:`Section %s<adc data format>`).

Data processing such as trigger detection or packet building are always
performed at 5 ns intervals. Depending on the ADC mode, this interval
may contain 32 (:ref:`1-Channel Mode <1channelmode>` @ 6.4 Gsps),
16 (:ref:`2-Channel Mode <2channelmode>` @ 3.2 Gsps) or
8 (:ref:`4-Channel Mode <4channelmode>` @ 1.6 Gsps) samples.

The ADC mode is configured using
:cpp:member:`ndigo6g12_configuration::adc_mode`.

The board supports using one, two or four channels. This is configured when
the board is initialized, see :cpp:member:`ndigo6g12_init_parameters::application_type`.

During interleaving, the Ndigo6G-12 firmware reorders and groups the data
into a linear sample stream. The process is fully transparent. For
users, the only difference is that a 5 ns cycle can contain
8, 16 or 32 samples, depending on the mode.

Depending on the
:cpp:member:`application_type <ndigo6g12_init_parameters::application_type>`,
the minimal length of the output packets changes. The minimal lengths are:

- 3 :math:`\times` 32 Samples (15 ns) @ 6.4 Gsps (1-Channel Mode)
- 3 :math:`\times` 16 Samples (15 ns) @ 3.2 Gsps (2-Channel Mode)
- 4 :math:`\times` 8 Samples (20 ns) @ 1.6 Gsps (4-Channel Mode)


.. _1channelmode:

1-Channel Modes A and D
^^^^^^^^^^^^^^^^^^^^^^^
In these modes, only a single channel is used. The analog signal on that
channel is digitized at 6.4 Gsps. Packet size is always a multiple of 32
samples per 5 ns (See :numref:`Figures %s<Fig 2.9>`
and :numref:`%s<Fig 2.15>`).

For this mode, :cpp:member:`ndigo6g12_static_info::application_type` needs to
be either :c:macro:`NDIGO6G12_APP_TYPE_1CH` or
:c:macro:`NDIGO6G12_APP_TYPE_AVRG`.

.. _Fig 2.9:
.. figure:: ../figures/1ChannelMode.*

    ADCs in 1-channel-mode A, B, C or D interleaved for 6.4 Gsps.

.. _2channelmode:

2-Channel Mode AD
^^^^^^^^^^^^^^^^^
In this mode, two channels are used simultaneously. The analog signals
on these channels are digitized at 3.2 Gsps each.
Packet size is always a multiple of 16 samples per
5 ns (See :numref:`Figures %s<Fig 2.8>` and
:numref:`%s<Fig 2.14>`).

For this mode, :cpp:member:`ndigo6g12_static_info::application_type` needs to
be :c:macro:`NDIGO6G12_APP_TYPE_2CH`.

.. _Fig 2.8:
.. figure:: ../figures/2ChannelMode.*

    ADCs in 2-channel-mode AD, interleaved for 3.2 Gsps.

.. _4channelmode:

4-Channel Mode ABCD
^^^^^^^^^^^^^^^^^^^

In this mode, all four channels are digitized independently at 1.6 Gsps
each. The packet size is always a multiple of 16 samples per 10 ns. (See
:numref:`Figures %s<Fig 2.7>` and :numref:`%s<Fig 2.13>`).

For this mode, :cpp:member:`ndigo6g12_static_info::application_type` needs to
be :c:macro:`NDIGO6G12_APP_TYPE_4CH`.

.. _Fig 2.7:
.. figure:: ../figures/4ChannelMode.*

    ADCs in 4-channel-mode ABCD at 1.6 Gsps.

.. _multiple sampling modes:

Multiple Sampling Modes
^^^^^^^^^^^^^^^^^^^^^^^
In these modes, only the specified input channels are used, but the channels
are sampled independently by the ADC cores.
The output of the board depends on
:cpp:member:`ndigo6g12_configuration::sample_averaging`.

- :code:`sample_averaging == false`: The digitized samples are output
  as separate packets (the number of which depends on the selected mode).
- :code:`sample_averaging == true`: The average of the digitized
  samples is calculated and output as one single packet.

Using the same trigger settings on all ADCs can be used to reduce noise
by averaging the four channels.
To deal with complex triggering conditions, different trigger settings on each
of the ADCs can be used.

The Ndigo6G-12 provides four ADCs sampling at 1.6 Gsps each.
Higher speed modes are implemented by interleaving two or four of these ADCs.

Modes AA and DD
```````````````
In this mode, input channel A (or D) is sampled at 3.2 Gsps two times and
independently by the internal ADC cores, see
:numref:`Figure %s<fig mode AA DD>`.

For this mode, :cpp:member:`ndigo6g12_static_info::application_type` needs to
be :c:macro:`NDIGO6G12_APP_TYPE_2CH`.

.. _fig mode AA DD:
.. figure:: ../figures/2ChannelMode_AA_DD.*

    ADCs in 2-channel-mode AA or DD at 3.2 Gsps.

Mode AADD
`````````
In this mode, input channel A and D are sampled at 1.6 Gsps two times and
independently by the internal ADC cores, see
:numref:`Figure %s<fig mode AADD>`.

For this mode, :cpp:member:`ndigo6g12_static_info::application_type` needs to
be :c:macro:`NDIGO6G12_APP_TYPE_4CH`.

.. _fig mode AADD:
.. figure:: ../figures/4ChannelMode_AADD.*

    ADCs in 4-channel-mode AADD at 1.6 Gsps.

Modes AAAA, DDDD
````````````````
In this mode, input channel A (or D) are sampled at 1.6 Gsps four times and
independently by the internal ADC cores, see
:numref:`Figure %s<fig mode AAAA DDDD>`.

For this mode, :cpp:member:`ndigo6g12_static_info::application_type` needs to
be :c:macro:`NDIGO6G12_APP_TYPE_4CH`.

.. _fig mode AAAA DDDD:
.. figure:: ../figures/4ChannelMode_AAAA_DDDD.*

    ADCs in 4-channel-mode AAAA or DDDD at 1.6 Gsps.




