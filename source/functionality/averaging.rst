.. _Averaging Mode:

Averaging Mode
~~~~~~~~~~~~~~

Instead of streaming each recorded trigger event as packets, it is possible
to average over multiple trigger events.

By initializing the Ndigo6G-12 board with :c:macro:`NDIGO6G12_APP_TYPE_AVRG`,
Averaging Mode is enabled. Then, a number of
:cpp:member:`ndigo6g12_averager_configuration::iterations` are averaged
before output is written.

Averaging Mode can be used only with ADC modes A and D
(see :numref:`Section %s <ADC Modes>`).


.. attention::

    Be aware that in averaging mode, the first two 64-bit words in
    :cpp:member:`data<crono_packet::data>` are an extended header. See
    :numref:`Section %s<avrg data format>` for more information.
