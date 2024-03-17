.. _Section Trigger Blocks:

Trigger Conditions and Trigger Blocks
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Ndigo6G-12** record analog waveforms using zero suppression.
Whenever a relevant waveform is detected, data is written to an internal
FIFO memory.
Each ADC channel has one trigger block determining whether data is written to
the FIFO.
The parameters are set in Structures :cpp:struct:`ndigo6g12_trigger` and 
:cpp:struct:`ndigo6g12_trigger_block`.

Each trigger block consists of two independent units that check the
incoming raw data stream for trigger conditions. The trigger conditions
are configured using the :cpp:struct:`ndigo6g12_trigger` structure.

Users can specify a :cpp:member:`threshold <ndigo6g12_trigger::threshold>` 
and can choose whether triggering is used 
whenever incoming data is below or above the threshold (level triggering,
see :numref:`Figure %s<fig level trigger>`) or 
only if data exceeds the threshold (edge triggering, see 
:numref:`Figure %s<fig edge trigger>`).

.. _fig edge trigger:
.. figure:: ../../figures/edge-trigger.*

   Example for edge triggering.

.. _fig level trigger:
.. figure:: ../../figures/level-trigger.*

   Example for level triggering.

A gate :cpp:member:`length <ndigo6g12_trigger_block::length>` can be set to
extend the trigger window by multiples of 5 ns. 
Furthermore, a :cpp:member:`precursor <ndigo6g12_trigger_block::precursor>`
window can be specified, causing the trigger unit to write data to 
the FIFO (:code:`precursor` :math:`\times` 5 ns) before the trigger event.

When edge triggering is used, all packets have the same length of 
(:code:`precursor` + :code:`length` + 1)-cycles of 5 ns.
For level triggering, packet length is data dependent.

Please note that triggering is not accurate to sample. For each
5 ns clock cycle, it is determined whether on any sample during that clock
cycle a trigger condition is met. If it was met during a clock cycle, that 
cycle is then selected as the trigger point. 
As a result, the trigger sample can be anywhere
within a range of up to 8, 16, or 32 samples depending on the channel mode
(see :numref:`Section %s<ADC modes>` and :numref:`Figures %s<Fig 2.13>`,
:numref:`%s<Fig 2.14>`, and :numref:`%s<Fig 2.15>`). 

.. _Fig 2.13:
.. figure:: ../../figures/4ChannelTriggering.*

   Triggering in 4 channel mode at 8 samples per clock cycle.

.. _Fig 2.14:
.. figure:: ../../figures/2ChannelTriggering.*

   Triggering in 2 channel mode at 16 samples per clock cycle.


.. _Fig 2.15:
.. figure:: ../../figures/1ChannelTriggering.*

   Triggering in 1 channel mode at 32 samples per clock cycle.


If retriggering is active, the current trigger window is extended if a
trigger event is detected inside the window
(see :numref:`Figure %s<figure zero suppression>`).

A trigger block can use several input sources:

-  The 8 trigger decision units of all four ADC channels
   \(:numref:`Figure %s<Fig 2.16>`)
-  The GATE input (:numref:`Figure %s<Fig 2.17>`)
-  The Trigger or TDC input (:numref:`Figure %s<Fig 2.17>`)
-  A function trigger providing random or periodic triggering.

Trigger inputs from the above sources can be concatenated using logical
OR (:numref:`Figure %s<fig triggermatrix>`) by
setting the appropriate bits in the trigger blocks source mask.

Triggers can be fed into the gate blocks as described in
:numref:`Chapter %s<section gating blocks>` \(:numref:`Figure %s<Fig 2.20>`).
Gate blocks can be used to block writing data to the FIFO. That way, only
zero suppressed data occurring when the selected gate is active is transmitted.
This procedure reduces PCIe bus load even further 
\(:numref:`Figure %s<Fig 2.20>`).


.. _Fig 2.16:
.. figure:: ../../figures/analog-trigger.*

   From the ADC inputs, a trigger unit creates an input flag for
   the trigger matrix. Each digitizer channel (A, B, C, D) has two trigger
   units.

.. _Fig 2.17:
.. figure:: ../../figures/DigitalInput.*

   The digital inputs Trigger, GATE,
   BUS0, BUS1, BUS2 and BUS3 have simpler trigger units.


.. _Fig 2.18:
.. figure:: ../../figures/ExtensionBlock.*

   The extension block combines signals from
   the optional extension board and the sync cable.


.. _fig triggermatrix:
.. figure:: ../../figures/triggermatrix.*

   Trigger Matrix: The trigger signals of each ADC channel, the trigger
   input, the GATE input or the sync cable can be combined to create a
   trigger input for each trigger block. The four gate signals can be used
   to suppress triggers during certain time frames.