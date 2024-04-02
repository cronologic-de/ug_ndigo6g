.. _Section Gating Blocks:

Gating Blocks
~~~~~~~~~~~~~

.. _Fig 2.20:
.. figure:: ../figures/GatingBlocks.*

    Gating Blocks: Each gating block can use an arbitrary combination
    of inputs to trigger its state machine. The outputs can be individually
    inverted and routed to the AND-gate feeding the trigger blocks. TODO
    update Figure.

In order to decrease the amount of data transmitted to the PC, the Ndigo6G-12 
includes four independent gate and delay units.

They are configured using :cpp:member:`ndigo6g12_configuration::gating_block`.

A gate and delay unit creates a gate window starting and closing at specified 
times after a trigger event (as configured by the user with
:cpp:member:`ndigo6g12_gating_block::start` and 
:cpp:member:`stop <ndigo6g12_gating_block::stop>`).

:cpp:member:`trigger_blocks <ndigo6g12_configuration::trigger_block>`
can use the gate signal to suppress data acquisition, that is, 
only data that fulfills zero suppression specifications occurring in an
active gate window is written to the PC.

Configuration
^^^^^^^^^^^^^

The inputs of each :cpp:member:`ndigo6g12_configuration::gating_block`
is configured by :cpp:member:`ndigo6g12_gating_block::sources`.

The :cpp:member:`retrigger <ndigo6g12_gating_block::retrigger>` feature will 
create a new gate if a trigger occurs during an active gate window.

The gate signal can be inverted using
:cpp:member:`ndigo6g12_gating_block::negate`, causing an
active gate to close (instead of opening) for the specified time.

:numref:`Figure %s<Fig 2.21>` shows the functionality of
the gate timing and delay unit.

.. _Fig 2.21:
.. figure:: ../figures/gating_principle.*

    Gate and delay functionality: When a trigger occurs, the gate opens after a
    set period of time “Gate Start” and closes when it reaches
    “Gate Stop”. A second trigger event may influence this behavior if
    retriggering is enabled.


.. Gating Example 1: Suppression of Noise After Starting an Acquisition
.. ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. In mass spectrometer and other experiments, noise while starting data
.. acquisition can result in undesired trigger events for that time period.
.. To prevent noise in the output data, a gating block could be used to
.. suppress all triggers during start-up,

.. The following example illustrates the use of a gating block to prevent
.. noise: The GATE input transmits a pulse on each acquisition start. The
.. trigger structure of the GATE input is used to select pulse polarity.
.. Then, the GATE trigger is selected as gating block input and the gating
.. block's start parameter is set to 0. The stop parameter is set to the
.. desired length measured in 5 ns clock cycle and negate is set to true.
.. The gating block will now output a low pulse of the desired length
.. whenever there is a pulse on the GATE input.

.. Enabling this gating block as an AND input to the trigger block, for
.. which noise shall be suppressed.

.. Gating Example 2: Delayed Trigger
.. ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. To sample a short window at a specified time after a trigger event on a
.. channel, the gating block can be used to create a delayed trigger. To do
.. this, one of the triggers of the channel of interested is configured to
.. the desired parameters by selecting the threshold, setting the edge
.. polarity and enabling edge triggering.

.. Instead of directly using this trigger as input to the trigger block’s
.. input matrix, the trigger is selected as an input to a gating block. The
.. block is configured to :code:`start = delay` (in 3.2 |nbws| ns clock cycles)
.. and :code:`stop = start+1`, :code:`negate = false`. This causes the gating
.. block to produce a one clock cycle pulse on its output after the
.. specified delay.

.. To send this pulse to the trigger block, the gating block must be
.. enabled in the trigger block’s AND matrix and the ONE trigger source
.. must be selected.

.. Gating Example 3: Dual Level Trigger
.. ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. The gates provide AND connections between each other (see
.. :numref:`Figure %s<fig triggermatrix>`) which can be used for
.. example in a dual level trigger. For the acquisition of signal data with
.. amplitudes between a lower and an upper bound, for example, two level
.. triggers can be connected (see 
.. :numref:`Figure %s<fig dualleveltrig>`): a falling level trigger
.. with an upper threshold and a rising level trigger with a lower
.. threshold.

.. Since the triggers are only connected by OR in the triggerblock logic
.. (see :numref:`Figure %s<fig triggermatrix>`) they are
.. assigned to one of the gates each and connected with AND via the gating
.. block region of the trigger matrix (see 
.. :numref:`Figures %s<fig triggermatrix>` and
.. :numref:`%s<fig dualleveltriglogic>`). Because of the
.. dead times of the gates it is important to enable the retriggering
.. feature. Furthermore a precursor of 2 clock cycles is needed, because
.. the gates are delayed in relation to the ADC samples.

.. .. _fig dualleveltrig:
.. .. figure:: figures/dual_level_triggering.*

..     Measureing data with amplitude between an upper and a lower threshold
..     by means of two level triggers.


.. .. _fig dualleveltriglogic:
.. .. figure:: figures/dual-level-triggering_logic.*

..     Gating block logic for the AND connection of two triggers.

.. Config settings can be found in the following code :cronoblue:`snippet`.

.. .. code-block:: c++

..     config.trigger_block[0].enabled = 1;
..     config.trigger_block[0].precursor = 2;
..     config.trigger_block[0].length = 0;
..     config.trigger_block[0].sources = NDIGO_TRIGGER_SOURCE_ONE;
..     config.trigger_block[0].gates = NDIGO_TRIGGER_GATE_0 | NDIGO_TRIGGER_GATE_1;
..     config.gating_block[0].retrigger = 1;
..     config.gating_block[0].stop = 0;
..     config.gating_block[0].sources = NDIGO_TRIGGER_A0;
..     config.gating_block[1].retrigger = 1;
..     config.gating_block[1].stop = 0;
..     config.gating_block[1].sources = NDIGO_TRIGGER_A1;
..     config.trigger[NDIGO_TRIGGER_A0].rising = 0;
..     config.trigger[NDIGO_TRIGGER_A0].threshold = 10000;
..     config.trigger[NDIGO_TRIGGER_A1].rising = 1;
..     config.trigger[NDIGO_TRIGGER_A1].threshold = -10000;