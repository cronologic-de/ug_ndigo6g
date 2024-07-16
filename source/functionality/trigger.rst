.. _Section Trigger Blocks:

Trigger Setup
~~~~~~~~~~~~~

The Ndigo6G-12 records analog waveforms using zero suppression.
Whenever a relevant waveform is detected, data is written to an internal
FIFO memory.
Each ADC channel has one *trigger block* determining whether data is written to
the FIFO.

All triggers are configured with the Structures
:cpp:struct:`ndigo6g12_trigger` and :cpp:struct:`ndigo6g12_trigger_block`.

Each *trigger block* consists of two independent units that check the
incoming raw data stream for trigger conditions.

The trigger conditions are configured using the :cpp:struct:`ndigo6g12_trigger` 
structure.

Trigger configuration
^^^^^^^^^^^^^^^^^^^^^

Users can specify a :cpp:member:`threshold <ndigo6g12_trigger::threshold>`
and can choose whether triggering is used
whenever incoming data is below or above the threshold (level triggering,
see :numref:`Figure %s<fig level trigger>`) or
only if data exceeds the threshold (edge triggering, see
:numref:`Figure %s<fig edge trigger>`).

.. _fig level trigger:
.. figure:: ../figures/level-trigger.*

   Example for level triggering.

.. _fig edge trigger:
.. figure:: ../figures/edge-trigger.*

   Example for edge triggering.


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

If :cpp:member:`retrigger <ndigo6g12_trigger_block::retrigger>` is enabled,
the current trigger window is extended if a trigger event is detected inside
the window (see :numref:`Figure %s<figure zero suppression>`).


.. _Fig 2.13:
.. figure:: ../figures/4ChannelTriggering.*

   Triggering in 4-channel mode at 8 samples per clock cycle.

.. _Fig 2.14:
.. figure:: ../figures/2ChannelTriggering.*

   Triggering in 2-channel mode at 16 samples per clock cycle.


.. _Fig 2.15:
.. figure:: ../figures/1ChannelTriggering.*

   Triggering in 1-channel mode at 32 samples per clock cycle.

Trigger inputs
^^^^^^^^^^^^^^

A :cpp:struct:`trigger_block <ndigo6g12_trigger_block>` can use several
input :cpp:member:`sources <ndigo6g12_trigger_block::sources>`:

-  The eight trigger decision units of all four ADC channels
   \(:numref:`Figure %s<Fig 2.16>`)
-  The four TDC and the two FPGA inputs (:numref:`Figure %s<Fig 2.17>`)
-  A function trigger providing random or periodic triggering (see
   :doc:`auto_trigger`).

Trigger inputs from the above sources can be concatenated using a logical OR
by setting the appropriate bits in the bitmask
(see :cpp:member:`ndigo6g12_trigger_block::sources`).

.. (:numref:`Figure %s<fig triggermatrix>`)



.. _Fig 2.16:
.. figure:: ../figures/analog-trigger.*

   From the ADC inputs, a trigger unit creates an input flag for
   the trigger matrix. Each digitizer channel (A, B, C, D) has two trigger
   units.

.. _Fig 2.17:
.. figure:: ../figures/DigitalInput.*
   :width: 50%

   The digital inputs TDC0, TDC1, TDC2, TDC4, FPGA0, and FPGA1
   have simpler trigger units.


.. .. _fig triggermatrix:
.. .. figure:: ../figures/triggermatrix.*

..    Trigger Matrix. The eight trigger signals from the four analog channels and
..    the trigger signals from the six digital channels (four TDC channels, FPGA0,
..    FPGA1) can be combined to create a trigger input for each *trigger block*.
..    Additionally, four *gate signals* can be used to suppress trigger during
..    configurable time frames.

.. _gating trigger events:

Gating trigger events
^^^^^^^^^^^^^^^^^^^^^

Triggers can be fed into the
:cpp:member:`gating_blocks <ndigo6g12_configuration::gating_block>`
as outlined in
:numref:`Chapter %s<section gating blocks>`.

.. and :numref:`Figure %s<Fig 2.20>`.


In return, the
:cpp:member:`gating_blocks <ndigo6g12_configuration::gating_block>`
can be used to block writing data to the FIFO. That way, only
zero-suppressed data occurring when the selected gate is active is transmitted.
This procedure reduces PCIe bus load even further.

Which
:cpp:member:`gating_block <ndigo6g12_configuration::gating_block>`
is used to block a particular
:cpp:member:`trigger_block <ndigo6g12_configuration::trigger_block>`
is configured
with :cpp:member:`ndigo6g12_trigger_block::gates`.