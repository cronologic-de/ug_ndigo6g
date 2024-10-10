=======
Erratum
=======

Up to firmware revision 1.24120, the retrigger feature of the
:ref:`gating blocks<Section Gating Blocks>`
does not behave as intended. Instead of a gate being only extended by a
retrigger event, the state of the gate is reset to inactive.