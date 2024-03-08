.. _ADC Modes:

ADC Modes
~~~~~~~~~

Depending on the board configuration, the analog input signal is quantized
to 8 or 10 bits. However, the board always scales and offsets the data
to 16-bit signed data centered around 0.

Data processing such as trigger detection or packet building are always
performed on 3.2 ns intervals. Depending on the ADC mode, this interval
may contain 4, 8 or 16 samples.

The ADC mode is configured using 
:cpp:member:`ndigo6g12_configuration::adc_mode`.

The board supports using one, two or four channels:


1-Channel Modes A and D
^^^^^^^^^^^^^^^^^^^^^^^
In these modes, only a single channel is used. The analog signal on that
channel is digitized at 6.4 Gsps. Packet size is always a multiple of 16
samples per 3.2 |nbws| ns (See :numref:`Figures %s<Fig 2.9>`
and :numref:`%s<Fig 2.15>`).

For this mode, :cpp:member:`ndigo6g12_static_info::application_type` needs to
be either :c:macro:`NDIGO6G12_APP_TYPE_1CH` or 
:c:macro:`NDIGO6G12_APP_TYPE_AVRG`.


2-Channel Mode AD
^^^^^^^^^^^^^^^^^
In this mode, two channels are used simultaneously. The analog signals
on these channels are digitized at 3.2 Gsps each.
Packet size is always a multiple of 8 samples per
3.2 ns (See :numref:`Figures %s<Fig 2.8>` and
:numref:`%s<Fig 2.14>`).

For this mode, :cpp:member:`ndigo6g12_static_info::application_type` needs to
be either :c:macro:`NDIGO6G12_APP_TYPE_2CH` or 
:c:macro:`NDIGO6G12_APP_TYPE_AVRG`.


4-Channel Mode ABCD
^^^^^^^^^^^^^^^^^^^

In this mode, all four channels are digitized independently at 1.6 Gsps
each. The packet size is always a multiple of 4 samples per 3.2 ns. (See
:numref:`Figures %s<Fig 2.7>` and :numref:`%s<Fig 2.13>`).

For this mode, :cpp:member:`ndigo6g12_static_info::application_type` needs to
be either :c:macro:`NDIGO6G12_APP_TYPE_4CH` or 
:c:macro:`NDIGO6G12_APP_TYPE_AVRG`.


.. _multiple sampling modes:

Multiple Sampling Modes
^^^^^^^^^^^^^^^^^^^^^^^
In these modes, only the specified input channels are used, but the channels
are sampled independently by the ADC chips.
The output of the board depends on
:cpp:member:`ndigo6g12_configuration::sample_averaging`.

- :code:`sample_averaging == false`: The digitized samples are output 
  as separate packages (the number of which depends on the selected mode).
- :code:`sample_averaging == true`: The average of the digitized
  samples is calculated and output as one single package.

Using the same trigger setting on all ADCs, can be used to reduce noise
by averaging the four channels. 
To deal with complex triggering conditions, different trigger settings on each
of the ADCs can be used.

During interleaving, the Ndigo6G-12 firmware reorders and groups the data
into a linear sample stream. The process is fully transparent. For
users, the only difference is that a 3.2 ns cycle can contain
4, 8 or 16 samples, depending on the mode.

The Ndigo6G-12 provides four ADCs sampling at 1.6 Gsps each.
Higher speed modes are implemented by interleaving two or four of these ADCs.

Modes AA and DD
``````````````` 
In this mode, input channel A (or D) is sampled at 3.2 Gsps two times and
independently by the internal ADC chips.

For this mode, :cpp:member:`ndigo6g12_static_info::application_type` needs to
be either :c:macro:`NDIGO6G12_APP_TYPE_2CH` or 
:c:macro:`NDIGO6G12_APP_TYPE_AVRG`.

Mode AADD
`````````
In this mode, input channel A and D are sampled at 1.6 Gsps two times and
independently by the internal ADC chips.

For this mode, :cpp:member:`ndigo6g12_static_info::application_type` needs to
be either :c:macro:`NDIGO6G12_APP_TYPE_4CH` or 
:c:macro:`NDIGO6G12_APP_TYPE_AVRG`.

Modes AAAA, DDDD
````````````````
In this mode, input channel A (or D) are sampled at 1.6 Gsps four times and
independently by the internal ADC chips.

For this mode, :cpp:member:`ndigo6g12_static_info::application_type` needs to
be either :c:macro:`NDIGO6G12_APP_TYPE_4CH` or 
:c:macro:`NDIGO6G12_APP_TYPE_AVRG`.


.. _Fig 2.7:
.. figure:: ../../figures/4ChannelMode.*

    ADCs in 4 channel mode ABCD at 1.6 Gsps. TODO: update graphics

.. _Fig 2.8:
.. figure:: ../../figures/2ChannelMode.*

    ADCs in 2 channel mode AD, interleaved for 3.2 Gsps. TODO: update graphics

.. _Fig 2.9:
.. figure:: ../../figures/1ChannelMode.*

    ADCs in 1 channel mode A, B, C or D interleaved for 6.4 Gsps. TODO: update graphics


