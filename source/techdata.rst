Technical Data
==============

.. attention:: 

    This User Guide is under active development and is subject to major 
    changes.

- Input Passband: **4.5** |nbws| **MHz** to **950** |nbws| **MHz**

- Power Requirements: **25** |nbws| **W**

- Mechanical Dimensions:
  **170** |nbws| **mm** :math:`\times` **106** |nbws| **mm**

- Throughput: **800** |nbws| **MByte/s** on PCIe x4


Digitizer Characteristics
-------------------------

Each board is tested against the values listed in the |bdq| Min |edq| column.
|bdq| Typical |edq| is the mean value of the first 10 boards produced.

1-Channel-Mode (5 Gsps)
~~~~~~~~~~~~~~~~~~~~~~~


+------------------------+--------------------------+-----+---------+-----+-------+
| Symbol                 | Parameter                | Min | Typical | Max | Units |
+========================+==========================+=====+=========+=====+=======+
| THD1                   | Total Harmonic           | 56  | 60      |     | dB    |
|                        | Distortion               |     |         |     |       |
+------------------------+--------------------------+-----+---------+-----+-------+
| SNR1                   | Signal to Noise Ration   | 47  | 49      |     | dB    |
+------------------------+--------------------------+-----+---------+-----+-------+
| SFDR\ :sub:`incl`\ 1   | Spurious Free Dynamic    | 55  | 59      |     | dB    |
|                        | Range (including         |     |         |     |       |
|                        | Harmonics)               |     |         |     |       |
+------------------------+--------------------------+-----+---------+-----+-------+
| SFDR\ :sub:`excl`\ 1   | Spurious Free Dynamic    | 55  | 60      |     | dB    |
|                        | Range (excluding         |     |         |     |       |
|                        | Harmonics)               |     |         |     |       |
+------------------------+--------------------------+-----+---------+-----+-------+
| SINAD1                 | Signal-to-Interference   | 47  | 48      |     | dB    |
|                        | Ratio including Noise    |     |         |     |       |
|                        | and Distortion           |     |         |     |       |
+------------------------+--------------------------+-----+---------+-----+-------+
| ENOB1                  | Effective Number of Bits | 7.5 | 7.7     |     |       |
+------------------------+--------------------------+-----+---------+-----+-------+

2-Channel-Mode (2.5 Gsps)
~~~~~~~~~~~~~~~~~~~~~~~~~

+---------------------+--------------------------+-----+---------+-----+-------+
| Symbol              | Parameter                | Min | Typical | Max | Units |
+=====================+==========================+=====+=========+=====+=======+
| THD2                | Total Harmonic           | 56  |  60     |     | dB    |
|                     | Distortion               |     |         |     |       |
+---------------------+--------------------------+-----+---------+-----+-------+
| SNR2                | Signal to Noise Ration   | 49  | 51      |     | dB    |
+---------------------+--------------------------+-----+---------+-----+-------+
| SFDR\ :sub:`incl`\ 2| Spurious Free Dynamic    | 58  | 60      |     | dB    |
|                     | Range (including         |     |         |     |       |
|                     | Harmonics)               |     |         |     |       |
+---------------------+--------------------------+-----+---------+-----+-------+
| SFDR\ :sub:`excl`\ 2| Spurious Free Dynamic    | 58  | 61      |     | dB    |
|                     | Range (excluding         |     |         |     |       |
|                     | Harmonics)               |     |         |     |       |
+---------------------+--------------------------+-----+---------+-----+-------+
| SINAD2              | Signal-to-Interference   | 49  | 50      |     | dB    |
|                     | Ratio including Noise    |     |         |     |       |
|                     | and Distortion           |     |         |     |       |
+---------------------+--------------------------+-----+---------+-----+-------+
| ENOB2               | Effective Number of Bits | 7.8 | 8.1     |     |       |
+---------------------+--------------------------+-----+---------+-----+-------+

4-Channel-Mode (1.25 Gsps)
~~~~~~~~~~~~~~~~~~~~~~~~~~

+----------------------+--------------------------+-----+---------+-----+-------+
| Symbol               | Parameter                | Min | Typical | Max | Units |
+======================+==========================+=====+=========+=====+=======+
| THD4                 | Total Harmonic           | 56  |  60     |     | dB    |
|                      | Distortion               |     |         |     |       |
+----------------------+--------------------------+-----+---------+-----+-------+
| SNR4                 | Signal to Noise Ration   | 49  | 51      |     | dB    |
+----------------------+--------------------------+-----+---------+-----+-------+
| SFDR\ :sub:`incl`\ 4 | Spurious Free Dynamic    | 58  | 60      |     | dB    |
|                      | Range (including         |     |         |     |       |
|                      | Harmonics)               |     |         |     |       |
+----------------------+--------------------------+-----+---------+-----+-------+
| SFDR\ :sub:`excl`\ 4 | Spurious Free Dynamic    | 68  | 73      |     | dB    |
|                      | Range (excluding         |     |         |     |       |
|                      | Harmonics)               |     |         |     |       |
+----------------------+--------------------------+-----+---------+-----+-------+
| SINAD4               | Signal-to-Interference   | 49  | 51      |     | dB    |
|                      | Ratio including Noise    |     |         |     |       |
|                      | and Distortion           |     |         |     |       |
+----------------------+--------------------------+-----+---------+-----+-------+
| ENOB4                | Effective Number of Bits | 7.9 | 8.1     |     |       |
+----------------------+--------------------------+-----+---------+-----+-------+

Electrical Characteristics
--------------------------

Oscillator
~~~~~~~~~~


The **Ndigo5G** uses an OCXO oscillator with **25** |nbws| **ppb** stability.
After power up the oscillator needs to run for **10 minutes** to reach this
stability.

.. _techdata environmental conditions for operation:

Environmental Conditions for Operation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The board is designed to be operated under the following conditions:

+---------+-------------------------+------+---------+------+------------------------------+
| Symbol  | Parameter               | Min  | Typical | Max  | Units                        |
+=========+=========================+======+=========+======+==============================+
| T       | ambient                 | 5    |         | 40   | °C                           |
|         | temperature             |      |         |      |                              |
+---------+-------------------------+------+---------+------+------------------------------+
| RH      | relative                | 20   |         | 75   | %                            |
|         | humidity at             |      |         |      |                              |
|         | 31\ :math:`^{\circ}`\ C |      |         |      |                              |
|         |                         |      |         |      |                              |
+---------+-------------------------+------+---------+------+------------------------------+


Environmental Conditions for Storage
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The board shall be stored between operation under the following
conditions:

+---------+-----------------------------+------+---------+------+----------------------+
| Symbol  | Parameter                   | Min  | Typical | Max  | Units                |
+=========+=============================+======+=========+======+======================+
| T       | ambient                     | −30  |         | 60   | °C                   |
|         | temperature                 |      |         |      |                      |
+---------+-----------------------------+------+---------+------+----------------------+
| RH      | relative                    | 10   |         | 70   | %                    |
|         | humidity at                 |      |         |      |                      |
|         | 31\ :math:`^{\circ}`\ C     |      |         |      |                      |
|         | non condensing              |      |         |      |                      |
+---------+-----------------------------+------+---------+------+----------------------+

.. _techdata power supply:

Power Supply
~~~~~~~~~~~~

======= =================================== ====== ======= ===== =====
Symbol  Parameter                           Min    Typical Max   Units
======= =================================== ====== ======= ===== =====
I       PCIe 3,3V rail power consumption                   4     mA
VCC     PCIe 3,3V rail power supply         3.1    3.3     3.6    V
I       PCIe 12V rail power consumption                    2.1   A
VCC     PCIe 12V rail power supply          11.1   12      12.9  V
I       PCIe 3,3VAux rail power consumption        0             A
VCC     PCIe 3,3VAux rail power supply             3.3           V
======= =================================== ====== ======= ===== =====

Analog Input
~~~~~~~~~~~~

AC coupled single-ended analog inputs (standard version).

===============  ========================== ====== ======= ===== ==============
Symbol           Parameter                  Min    Typical Max   Units
===============  ========================== ====== ======= ===== ==============
V\ :sub:`p-p`    Peak to peak input voltage                0,5   V
Z\ :sub:`p`      Input impedance                    50           Ω
                 Analog offset              −0.25          0.25  V
===============  ========================== ====== ======= ===== ==============

AC coupled differential analog inputs (S version).

================= ========================== ===== ======= ===== ==============
Symbol            Parameter                  Min   Typical Max   Units
================= ========================== ===== ======= ===== ==============
V\ :sub:`com`     Input common mode          −4            6     V
V\ :sub:`p-p`     Differential input Voltage −125          125   mV
Z\ :sub:`p`       Input impedance                  100           Ω
                  Analog offset              −0.25         +0.25 V
================= ========================== ===== ======= ===== ==============

Analog inputs
~~~~~~~~~~~~~

Single ended AC coupled inputs Trigger and GATE with configurable DC
offset bias.

======================  ================= ====== ======= ====== ==============
Symbol                  Parameter         Min    Typical Max    Units
======================  ================= ====== ======= ====== ==============
V\ :sub:`trig`          Pulse height                     5.0    V
V\ :sub:`trigoffset`    DC offset         −1.25          1.25   V
V\ :sub:`tdcoffset`     DC offset for TDC −1.25          −0.01  V
Z\ :sub:`trig`          Input impedance          50             Ω
t\ :sub:`pulse`         pulse width       7              100    ns
======================  ================= ====== ======= ====== ==============


Information Required by DIN EN 61010-1
--------------------------------------

.. _techdata manufacturer:

Manufacturer
~~~~~~~~~~~~

The **Ndigo5G** is a product of:

    | cronologic GmbH & Co. KG
    | Jahnstraße 49
    | 60318 Frankfurt

    | HRA 42869 beim Amtsgericht Frankfurt/M
    | VAT-ID: DE235184378


Intended Use and System Integration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The devices are not ready to use as delivered by cronologic. It requires
the development of specialized software to fulfill the application of
the end user. The device is provided to system integrators to be built
into measurement systems that are distributed to end users. These
systems usually consist of a the **Ndigo5G**, a main board, a case,
application software and possible additional electronics to attach the
system to some type of detector. They might also be integrated with the
detector.

The **Ndigo5G** is designed to comply with **DIN EN 61326-1** when operated on
a PCIe compliant main board housed in a properly shielded enclosure. When
operated in a closed standard compliant PC enclosure the device does not
pose any hazards as defined by **EN 61010-1.**

Radiated emissions, noise immunity and safety highly depend on the
quality of the enclosure. It is the responsibility of the system
integrator to ensure that the assembled system is compliant to
applicable standards of the country that the system is operated in,
especially with regards to user safety and electromagnetic interference.
Compliance was only tested for attached cables shorter than 3 |nbws| m.

When handling the board, adequate measures have to be taken to protect
the circuits against electrostatic discharge (ESD). All power supplied
to the system must be turned off before installing the board.

Cooling
~~~~~~~

The **Ndigo5G** in its base configuration has passive cooling that requires
a certain amount of air flow. If the case design can’t provide enough
air flow to the board, a slot cooler like Zalman ZM-SC100 can be placed
next to the board. Active cooling is also available as an option to the
board.



Environmental Conditions
~~~~~~~~~~~~~~~~~~~~~~~~
See :numref:`Section %s<techdata environmental conditions for operation>`
and :numref:`Section %s<techdata power supply>`.


Inputs
~~~~~~

All inputs are AC coupled. The inputs have very high input bandwidth
requirements and therefore there are no circuits that provide over
voltage protection for these signals. Any voltage on the inputs above **5V**
or below **−5V** relative to the voltage of the slot cover can result in
permanent damage to the board.

Known Bugs
~~~~~~~~~~

The Ndigo5G does not work in most Thunderbolt PCIe extension enclosures.
The reason is unknown.

Workarounds
~~~~~~~~~~~

Use **Ndigo6G** All other cronologic products work reliably in Thunderbolt
enclosures. The **Ndigo6G** offers very similar functionality to the
**Ndigo5G** at a higher performance. When using the Ndigo6G as a
replacement, there are some software changes required in the device
configuration. The readout data format and API is identical. See
`www.cronologic.de/products/adcs/ndigo6g-12 <https://www.cronologic.de/products/adcs/ndigo6g-12>`__
for details.

Use Ndigo Crate Up to eight **Ndigo5G** can be used in an Ndigo Crate
connected to a PC. Electrically the setup is similar to an external
Thunderbolt enclosure, but the PC must have a vacant PCIe slot.
See
`www.cronologic.de/products/pcie/pcie-crates <https://www.cronologic.de/products/pcie/pcie-crates>`__
for details.

All other cronogic products work reliably in Thundberbolt enclosure.
Consider using an **Ndigo6G** as a replace

Recycling
~~~~~~~~~

cronologic is registered with the “Stiftung Elektro-Altgeräte Register”
as a manufacturer of electronic systems with **Registration ID DE
77895909**.

The **Ndigo5G** belongs to **category 9**, **“Überwachungs und
Kontrollinstrumente für ausschließlich gewerbliche Nutzung”.** The last owner
of an **Ndigo5G** must recycle it, treat the board in compliance with **§11**
and **§12** of the German ElektroG, or return it to the manufacturer’s address
listed in :numref:`Section %s<techdata manufacturer>`.

Export Control
~~~~~~~~~~~~~~

The **Ndigo5G** product line is a dual use item under
`Council Regulation (EC) No 428/2009 of 5 May 2009 setting up a Community regime for the
control of exports, transfer, brokering and transit of dual-use
items <https://data.europa.eu/eli/reg/2009/428/2021-10-077>`__ in
section **3A002h.** Similar regulations exist in many countries outside Europe.

An export permit is required to export this product from the European
Community (EC) which will cause additional lead time. When ordering from
outside the EC, the seller will ask you for additional information
needed to obtain this permit.

Before reexporting an **Ndigo5G** or any product containing an Ndigo5G as a
component please check you local regulations whether an export permit is
required.