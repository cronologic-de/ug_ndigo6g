Installing the Board
--------------------

The Ndigo6G-12 board can be installed in any PCIe x8 (or higher
amount of lanes) PCIe slot.
If the slot electrically supports less than eight lanes, the board will operate
at lower data throughput rates.

Cooling
^^^^^^^
The Ndigo6G-12 board is equipped with an active cooling system, ensuring 
proper cooling of the device. If, however, the temperature of the ADC chip
exceeds 90 °C (for instance, if the device is operated in inappropriate 
environmental conditions, see 
:numref:`Section %s<techdata environmental conditions for operation>`), 
a warning is issued to the device driver.
When the temperature exceeds 95 °C, the ADC chip is disabled to avoid damaging 
the device.
