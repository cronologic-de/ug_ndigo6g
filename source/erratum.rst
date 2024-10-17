=======
Erratum
=======

Up to firmware revision 1.24120, the retrigger feature of the
:ref:`gating blocks<Section Gating Blocks>`
does not behave as intended. Instead of a gate being only extended by a
retrigger event, the state of the gate is reset to inactive.

Up to firmware revision 1.24120 and in 4-channel mode,
:cpp:func:`ndigo6g12_single_shot` only works properly if
:cpp:member:`ndigo6g12_trigger_block::multi_shot_count == 1<ndigo6g12_trigger_block::multi_shot_count>`.