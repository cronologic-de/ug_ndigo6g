.. _Averaging Mode:

Averaging Mode
~~~~~~~~~~~~~~

Instead of streaming each recorded trigger event as packets, it is possible
to average over multiple trigger events.

By initializing the Ndigo6G-12 board with :c:macro:`NDIGO6G12_APP_TYPE_AVRG`,
Averaging Mode is enabled. Then, 
:cpp:member:`ndigo6g12_averager_configuration::iterations` are averaged
before output is written.

Averaging Mode can be used with all ADC modes
(see :numref:`Section %s <ADC Modes>`).