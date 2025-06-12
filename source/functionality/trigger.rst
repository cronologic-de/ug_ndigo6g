.. _Section Trigger Blocks:

Trigger Setup
~~~~~~~~~~~~~

The Ndigo6G-12 records analog waveforms using zero suppression.
Whenever a relevant waveform is detected, data is written to an internal
FIFO memory.

Each ADC channel has two *trigger units*. These can be configured independently 
(e.g., one unit could trigger on rising edges, the other on falling).
They are configured with
:cpp:member:`config.trigger <ndigo6g12_configuration::trigger>`.

Each ADC channel has a corresponding *trigger block* that determines whether 
data is written to the internal FIFOs. The trigger blocks are configured with
:cpp:member:`config.trigger_block <ndigo6g12_configuration::trigger_block>`.
Each trigger block can take any amount of trigger units as a source (for 
details, see :cpp:member:`ndigo6g12_trigger_block::sources` or
:numref:`Section %s<section trigger inputs>`),
thus, enabling sophisticated trigger setups.

Trigger configuration
^^^^^^^^^^^^^^^^^^^^^

Analog Inputs
*************

Users can specify a :cpp:member:`threshold <ndigo6g12_trigger::threshold>`
and can choose whether triggering is used
whenever incoming data is below or above the threshold (level triggering,
see :numref:`Figure %s<fig level trigger>`) or
only if data exceeds the threshold (edge triggering, see
:numref:`Figure %s<fig edge trigger>`).

.. _fig level trigger:
.. figure:: ../figures/level-trigger.*
   :width: 90%
   :alt: Example for level triggering of the Ndigo6G-12.

   Example for level triggering.

.. _fig edge trigger:
.. figure:: ../figures/edge-trigger.*
   :width: 90%
   :alt: Example for edge triggering of the Ndigo6G-12.

   Example for edge triggering.


A gate :cpp:member:`length <ndigo6g12_trigger_block::length>` can be set to
extend the recording window by multiples of 5 ns.
Furthermore, a :cpp:member:`precursor <ndigo6g12_trigger_block::precursor>`
window can be specified, causing the trigger unit to write data to
the FIFO (:code:`precursor` :math:`\times` 5 ns) before the trigger event.

When edge triggering is used, all packets have the same length of
(:code:`precursor` + :code:`length` + 1)-cycles of 5 ns.
For level triggering, packet length is data dependent.

If :cpp:member:`retrigger <ndigo6g12_trigger_block::retrigger>` is enabled and
the trigger conditions are fulfilled during the recording of the postcursor, 
the recording window is extended (see :numref:`Figure %s<figure zero 
suppression>`).

.. _Fig 2.13:
.. figure:: ../figures/4ChannelTriggering.*
   :width: 90%
   :alt: Ndigo6G-12 triggering in 4-channel mode

   Triggering in 4-channel mode at 8 samples per clock cycle.

.. _Fig 2.14:
.. figure:: ../figures/2ChannelTriggering.*
   :alt: Ndigo6G-12 triggering in 2-channel mode
   :width: 90%

   Triggering in 2-channel mode at 16 samples per clock cycle.


.. _Fig 2.15:
.. figure:: ../figures/1ChannelTriggering.*
   :alt: Ndigo6G-12 triggering in 1-channel mode
   :width: 90%

   Triggering in 1-channel mode at 32 samples per clock cycle.

Digital Inputs
**************

For all digital inputs, the configuration value
:cpp:member:`ndigo6g12_trigger::threshold` is ignored. Their trigger threshold is
configured by :cpp:member:`ndigo6g12_configuration::tdc_trigger_offsets`.

Equivalently to the analog inputs, edge- or level-trigger functionality can be
enabled using :cpp:member:`ndigo6g12_trigger::edge`. The duration of a level trigger
is solely limited by the AC-coupling (see :numref:`Figure %s<fig baselinedrift>` for
the effects of AC-coupling on a signal).


.. _section trigger inputs:

Trigger inputs
^^^^^^^^^^^^^^

A :cpp:struct:`trigger_block <ndigo6g12_trigger_block>` can use several
input :cpp:member:`sources <ndigo6g12_trigger_block::sources>`:

-  The eight trigger decision units of all four ADC channels
   \(:numref:`Figure %s<Fig 2.16>`)
-  The four TDC and the two digital control inputs
   (:numref:`Figure %s<Fig 2.17>`)
-  A function trigger providing random or periodic triggering (see
   :doc:`auto_trigger`).

Trigger inputs from the above sources can be concatenated using a logical OR
by setting the appropriate bits in the bitmask
(see :cpp:member:`ndigo6g12_trigger_block::sources`).

See also :numref:`Figure %s<fig triggermatrix>`.



.. _Fig 2.16:
.. figure:: ../figures/analog-trigger.*
   :alt: Logic of the analog inputs.
   :width: 70%

   From the ADC inputs, a trigger unit creates an input flag for
   the trigger matrix. Each digitizer channel (A, B, C, D) has two trigger
   units.

.. _Fig 2.17:
.. figure:: ../figures/DigitalInput.*
   :width: 70%
   :alt: Logic of the digital inputs.

   The digital inputs TDC0, TDC1, TDC2, TDC3, TRG, and GATE
   have simpler trigger units.


.. _fig triggermatrix:
.. figure:: ../figures/triggermatrix-Ndigo6G-12.*
    :alt: Triggermatrix of the Ndigo6G-12

    Trigger Matrix. The eight trigger signals from the four analog channels and
    the trigger signals from the six digital channels (four TDC channels, TRG,
    GATE) can be combined to create a trigger input for each *trigger block*.
    Additionally, four *gate signals* (see
    :numref:`Figure %s<fig gatingblock>`) can be used to suppress trigger 
    during configurable time frames.

.. _gating trigger events:

Gating trigger events
^^^^^^^^^^^^^^^^^^^^^

Triggers can be fed into the
:cpp:member:`gating_blocks <ndigo6g12_configuration::gating_block>`
as outlined in
:numref:`Chapter %s<section gating blocks>` and :numref:`Figure %s<fig gatingblock>`.


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