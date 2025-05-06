========================
Timing Generator (TiGer)
========================

The LEMO connectors of all TDC channels, the TRG channel, and the GATE
channel can be used as an AC-coupled trigger output. The TiGer functionality
can be configured independently for each connector.

Each TiGer is configured using the :cpp:struct:`ndigo6g12_tdc_tiger_block` 
struct.  The tiger blocks can be triggered by any combination of inputs, 
including the auto-trigger and the ADC channels.

.. note::

    The TiGer configuration is similar to the
    :ref:`gating blocks<Section Gating Blocks>`.

The TiGer can be used in different output
:cpp:member:`modes<ndigo6g12_tdc_tiger_block::mode>`. For an overview of the
different modes, see the documentation in the API section.

With restrictions, the respective LEMO connectors can be used
simultaneously as a TiGer output *and* as an input.
