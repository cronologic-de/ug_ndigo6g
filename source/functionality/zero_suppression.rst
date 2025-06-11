Zero Suppression
~~~~~~~~~~~~~~~~
One of the Ndigo6G-12's key features is on-board zero suppression to reduce
PCIe bus load.
Only data that passes specifications predefined by the user is transmitted.
Data is transmitted as so-called “:doc:`packets <../packform/index>`.”
For the ADC channels, the packet contains the waveform data and a timestamp
giving the absolute time (i.e., the time since the start of the data
acquisition) of the packet's first sample.

:numref:`Figure %s<Figure Zero Suppression>` shows a simple example:
Data is only written to the PC if the sample values exceed a specific
threshold.
Expanding on that, the Ndigo6G-12's zero suppression can be used to
realize much more complex scenarios using the *Trigger* and *Gating Blocks*
(see :numref:`Sections %s<Section Trigger Blocks>` and
:numref:`%s<Section Gating Blocks>`).

.. _Figure Zero Suppression:
.. figure:: ../figures/ZeroSupp.*
    :width: 70%

    Simple zero suppression: Only data
    with values above a threshold are written to the PC.
