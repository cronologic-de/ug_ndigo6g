Hardware
========

Installation
------------

The Ndigo6G-12 board can be installed in any PCIe x8 (or higher
amount of lanes) PCIe slot.
If the slot electrically supports less than eight lanes, the board will operate
at lower data throughput rates.

Connect a 6-pin PCIe power cable to the connector at the rear of the board
(see :numref:`Figure %s<fig hardware picture>`).

.. note::

    The Ndigo6G-12 does not operate without a 6-pin PCIe power connector.

.. _fig hardware picture:
.. figure:: figures/Ndigo6G_periphery.jpg

    Overview of an Ndigo6G-12 board. Note the PCIe power connector at the rear
    of the board.


Cooling
-------
The Ndigo6G-12 board is equipped with an active cooling system, ensuring
proper cooling of the device. If, however, the temperature of the ADC chip
exceeds 90 °C (for instance, if the device is operated in inappropriate
environmental conditions, see
:numref:`Section %s<techdata environmental conditions for operation>`),
a warning is issued to the device driver.
When the temperature exceeds 95 °C, the ADC chip is disabled to avoid damaging
the device.

External Inputs and Connectors
------------------------------

Front bracket inputs
~~~~~~~~~~~~~~~~~~~~

The inputs of the Ndigo6G-12 board are located on the slot bracket.

:numref:`Figure %s<Fig 2.2>` shows the location of the four analog inputs A to
D (see :numref:`Section %s<analog inputs>`), the four digital TDC inputs 0 to 3 
(see :numref:`Section %s<digital TDC inputs>`), and the two digital control
inputs TRG and GATE (see :numref:`Section %s<digital ctrl inputs>`).


.. _Fig 2.2:
.. figure:: figures/Ndigo6G_connections.*
    :width: 90%

    Input connectors of an Ndigo6G-12 board located on the PCI bracket.

Clock connections
~~~~~~~~~~~~~~~~~

Connectors to connect an external clock or to access the internal clock 
signal are located at the top of the board (see
:numref:`Figure %s<fig hardware picture>`).

Clk in (SMA)
    Connect your external 10 MHz clock signal here. Make sure to set
    :cpp:member:`ndigo6g12_init_parameters::clock_source` to
    :c:macro:`NDIGO6G12_CLOCK_SOURCE_SMA`.

Clk out (SMA)
    10 MHz output. This is either the internal clock signal, or an
    external clock 10 MHz clock if one is used.


Clk diff (LEMO00)
    Same as Clk out, but as a differential signal and with a LEMO00 connector.




.. _analog inputs:

Analog Inputs
~~~~~~~~~~~~~

.. _Fig 2.4:
.. figure:: figures/InputCircuit.*
    :width: 70%

    Input circuit for each of the four analog channels.

The analog inputs of the ADC are single ended LEMO00 coax connectors.
The inputs have a 50 Ω impedance and are AC coupled. The
inputs are converted to a differential signal using a balun.

.. _analog offsets:

Analog Offsets
^^^^^^^^^^^^^^
AC coupling removes the DC voltage offset from the input signal.
However, users can shift the DC baseline voltage before sampling to a value of
their choice (using the
:cpp:member:`analog_offset <ndigo6g12_configuration::analog_offsets>`
parameter).

This feature is useful for highly asymmetric signals, such as pulses
from `TOF <https://www.cronologic.de/applications/tof-mass-spectrometry>`_
spectrometers or `LIDAR <https://www.cronologic.de/applications/lidar>`_
systems. Without analog offset
compensation, the pulses would begin in the middle of the ADC range,
effectively cutting the dynamic range in half
(see :numref:`Figure %s<Fig 2.6>`).
By shifting the DC baseline to one end of the ADC range, the input range
can be used fully, providing the maximum dynamic range. The analog offset
can be set between :math:`\pm` 0.5 V.


.. _Fig 2.5:
.. figure:: figures/analog_offset_sine.*
   :width: 80%

   Users can add an analog offset to the input before sampling.

.. _Fig 2.6:
.. figure:: figures/analog_offset_pulse.*
   :width: 80%

   Asymmetric signal shifted to increase dynamic range.


AC-Coupling and Baseline Drift
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Due to the AC-coupling of the analog and digital inputs, a baseline drift may
occur over time (see :numref:`Figure %s<fig baselinedrift>`). To avoid this problem,
make sure your input signal fulfills the requirements laid out in
:numref:`Section %s<analog inputs tech>`.

.. _fig baselinedrift:

.. figure:: figures/baselinedrift.*
    :width: 50%

    Baseline drift due to AC-coupling. A second pulse close to a first may be influenced
    by a shifted baseline, as sketched in the lower graph.


.. _digital tdc inputs:

Digital TDC Inputs
~~~~~~~~~~~~~~~~~~

The Ndigo6G-12 board includes four TDC channels with 13 ps timing resolution.
The inputs are AC coupled (see :numref:`Figure %s<fig digital input circuit>`).

.. _fig digital input circuit:
.. figure:: figures/InputCircuit_TDC.*

    Principal input circuit for each of the digital TDC and control inputs.

The following members of the :cpp:struct:`ndigo6g12_configuration` struct
configure, respectively, TDC channels 0 to 3:

:cpp:member:`tdc_trigger_offsets[0:3] <ndigo6g12_configuration::tdc_trigger_offsets>`
    Configure the DC offset.

:cpp:member:`trigger[NDIGO6G12_TRIGGER_TDC0:NDIGO6G12_TRIGGER_TDC3] <ndigo6g12_configuration::trigger>`
    Configure if an edge or level trigger is used (relevant, if the TDCs are used in
    :cpp:member:`trigger_blocks <ndigo6g12_configuration::trigger_block>` or
    :cpp:member:`gating_blocks <ndigo6g12_configuration::gating_block>`)
    and if the rising or falling edge of the input signal triggers.

:cpp:member:`tdc_configuration.channel[0:3] <ndigo6g12_tdc_configuration::channel>`
    Configure if
    (:cpp:member:`channel[0:3].enable <ndigo6g12_tdc_channel::enable>`)
    and when
    (:cpp:member:`channel[0:3].gating_block <ndigo6g12_tdc_channel::gating_block>`)
    timestamps are recorded on the TDC channel.

The trigger unit input logic is summarized, as well, in
:numref:`Figure %s<Fig 2.17>`.

.. _digital ctrl inputs:

Digital Control Inputs
~~~~~~~~~~~~~~~~~~~~~~
There are two digital control inputs on the front slot cover called
TRG and GATE.

Input-signals on the inputs TRG and GATE are digitized and routed to the 
Trigger Matrix. They can be used to trigger any of the trigger state machines 
and :doc:`gating blocks <functionality/gating>` with maximum sampling rate.

The digital control inputs are optimally suited to be used as digital triggers 
and gates, and we recommend using them instead of the
:ref:`digital TDC inputs <digital tdc inputs>` for these purposes.

TRG and GATE are configured analogously to the TDC inputs (see
:numref:`Section %s<digital tdc inputs>` and
:numref:`Figure %s<Fig 2.17>`), where indices 4 (5) and
:c:macro:`NDIGO6G12_TRIGGER_TRG` (:c:macro:`NDIGO6G12_TRIGGER_GATE`)
correspond to input TRG (GATE).

The input circuit and trigger logic is identical to the TDC inputs
(see :numref:`Figures %s<fig digital input circuit>` and
:numref:`%s<Fig 2.17>`).

Use Control Inputs as TDCs
^^^^^^^^^^^^^^^^^^^^^^^^^^
The control inputs TRG and GATE can be used as low-resolution TDCs.
The dead-time is 5 ns. Pulses should have a width of at least 300 ps to 
reliably be detected.

.. hint::

    To record timestamps with the TRG or GATE input, set
    :cpp:member:`config.tdc_configuration.channel[4||5].enable<ndigo6g12_tdc_channel::enable>`
    to :code:`true`.

.. note::

    The digital *control* inputs TRG and GATE are best suited for triggering
    and controlling gates.

    The digital *TDC* inputs are best suited for measuring precise time stamps.
