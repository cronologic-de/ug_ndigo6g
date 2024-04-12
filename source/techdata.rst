Technical Data
==============

- Input Passband: **4.5 MHz** to **950 MHz**

- Power Requirements: **25 W**

- Mechanical Dimensions:
  **170 mm** :math:`\times` **106 mm**

- Throughput: **800 MByte/s** on PCIe x4


Digitizer Characteristics
-------------------------

Each board is tested against the values listed in the |bdq| Min |edq| column.
|bdq| Typical |edq| is the mean value of the first 10 boards that were produced.


1-Channel-Mode (6.4 Gsps)
~~~~~~~~~~~~~~~~~~~~~~~~~

+------------------------+--------------------------+-----+---------+-----+-------+
| Symbol                 | Parameter                | Min | Typical | Max | Units |
+========================+==========================+=====+=========+=====+=======+
| THD\ :sub:`1`          | Total Harmonic           | TBD |         |     | dB    |
|                        | Distortion               |     |         |     |       |
+------------------------+--------------------------+-----+---------+-----+-------+
| SNR\ :sub:`1`          | Signal to Noise Ratio    | TBD |         |     | dB    |
+------------------------+--------------------------+-----+---------+-----+-------+
| SFDR\ :sub:`incl,1`    | Spurious Free Dynamic    | TBD |         |     | dB    |
|                        | Range (including         |     |         |     |       |
|                        | Harmonics)               |     |         |     |       |
+------------------------+--------------------------+-----+---------+-----+-------+
| SFDR\ :sub:`excl,1`    | Spurious Free Dynamic    | TBD |         |     | dB    |
|                        | Range (excluding         |     |         |     |       |
|                        | Harmonics)               |     |         |     |       |
+------------------------+--------------------------+-----+---------+-----+-------+
| SINAD\ :sub:`1`        | Signal-to-Interference   | TBD |         |     | dB    |
|                        | Ratio including Noise    |     |         |     |       |
|                        | and Distortion           |     |         |     |       |
+------------------------+--------------------------+-----+---------+-----+-------+
| ENOB\ :sub:`1`         | Effective Number of Bits | TBD |         |     |       |
+------------------------+--------------------------+-----+---------+-----+-------+


2-Channel-Mode (3.2 Gsps)
~~~~~~~~~~~~~~~~~~~~~~~~~

+-----------------------+---------------------------+-----+---------+-----+-------+
| Symbol                |  Parameter                | Min | Typical | Max | Units |
+=======================+===========================+=====+=========+=====+=======+
| THD\ :sub:`2`         |  Total Harmonic           | TBD |         |     | dB    |
|                       |  Distortion               |     |         |     |       |
+-----------------------+---------------------------+-----+---------+-----+-------+
| SNR\ :sub:`2`         |  Signal to Noise Ratio    | TBD |         |     | dB    |
+-----------------------+---------------------------+-----+---------+-----+-------+
| SFDR\ :sub:`incl,2`   |  Spurious Free Dynamic    | TBD |         |     | dB    |
|                       |  Range (including         |     |         |     |       |
|                       |  Harmonics)               |     |         |     |       |
+-----------------------+---------------------------+-----+---------+-----+-------+
| SFDR\ :sub:`excl,2`   |  Spurious Free Dynamic    | TBD |         |     | dB    |
|                       |  Range (excluding         |     |         |     |       |
|                       |  Harmonics)               |     |         |     |       |
+-----------------------+---------------------------+-----+---------+-----+-------+
| SINAD\ :sub:`2`       |  Signal-to-Interference   | TBD |         |     | dB    |
|                       |  Ratio including Noise    |     |         |     |       |
|                       |  and Distortion           |     |         |     |       |
+-----------------------+---------------------------+-----+---------+-----+-------+
| ENOB\ :sub:`2`        |  Effective Number of Bits | TBD |         |     |       |
+-----------------------+---------------------------+-----+---------+-----+-------+


4-Channel-Mode (1.6 Gsps)
~~~~~~~~~~~~~~~~~~~~~~~~~

+-----------------------+--------------------------+-----+---------+-----+-------+
| Symbol                | Parameter                | Min | Typical | Max | Units |
+=======================+==========================+=====+=========+=====+=======+
| THD\ :sub:`4`         | Total Harmonic           | TBD |         |     | dB    |
|                       | Distortion               |     |         |     |       |
+-----------------------+--------------------------+-----+---------+-----+-------+
| SNR\ :sub:`4`         | Signal to Noise Ratio    | TBD |         |     | dB    |
+-----------------------+--------------------------+-----+---------+-----+-------+
| SFDR\ :sub:`incl,4`   | Spurious Free Dynamic    | TBD |         |     | dB    |
|                       | Range (including         |     |         |     |       |
|                       | Harmonics)               |     |         |     |       |
+-----------------------+--------------------------+-----+---------+-----+-------+
| SFDR\ :sub:`excl,4`   | Spurious Free Dynamic    | TBD |         |     | dB    |
|                       | Range (excluding         |     |         |     |       |
|                       | Harmonics)               |     |         |     |       |
+-----------------------+--------------------------+-----+---------+-----+-------+
| SINAD\ :sub:`4`       | Signal-to-Interference   | TBD |         |     | dB    |
|                       | Ratio including Noise    |     |         |     |       |
|                       | and Distortion           |     |         |     |       |
+-----------------------+--------------------------+-----+---------+-----+-------+
| ENOB\ :sub:`4`        | Effective Number of Bits | TBD |         |     |       |
+-----------------------+--------------------------+-----+---------+-----+-------+



Electrical Characteristics
--------------------------

Oscillator
~~~~~~~~~~

The Ndigo6G-12 uses an OCXO oscillator with **25 ppb** stability.
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


.. _techdata environmental conditions for storage:

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

=============== ============================================= ====== ======= ===== =====
Symbol          Parameter                                     Min    Typical Max   Units
=============== ============================================= ====== ======= ===== =====
I\ :sub:`3.3`   PCIe 3.3V rail power consumption                             TBD   mA
VCC\ :sub:`3.3` PCIe 3.3V rail power supply                   TBD            TBD    V
I\ :sub:`12`    PCIe 12V rail power consumption                              TBD   A
VCC\ :sub:`12`  PCIe 12V rail power supply                    TBD            TBD   V
I\ :sub:`aux`   PCIe 3.3V\ :sub:`aux` rail power consumption                 TBD   A
VCC\ :sub:`aux` PCIe 3.3V\ :sub:`aux` rail power supply                      TBD   V
=============== ============================================= ====== ======= ===== =====


Analog Input
~~~~~~~~~~~~

AC coupled single-ended analog inputs:

+---------------+---------------------------+------+---------+-----+-------+
|Symbol         |  Parameter                | Min  | Typical | Max | Units |
+===============+===========================+======+=========+=====+=======+
| V\ :sub:`p-p` | Peak to peak input voltage|      |         | TBD | V     |
+---------------+---------------------------+------+---------+-----+-------+
| Z\ :sub:`p`   | Input impedance           |      | 50      |     | Ω     |
+---------------+---------------------------+------+---------+-----+-------+
|               | Analog offset             | TBD  |         | TBD | V     |
+---------------+---------------------------+------+---------+-----+-------+

Single ended AC coupled inputs Trigger and GATE with configurable DC
offset bias.

======================  ================= ====== ======= ====== ==============
Symbol                  Parameter         Min    Typical Max    Units
======================  ================= ====== ======= ====== ==============
V\ :sub:`trig`          Pulse height                     5.0    V
V\ :sub:`trigoffset`    DC offset         TBD            TBD    V
V\ :sub:`tdcoffset`     DC offset for TDC TBD            TBD    V
Z\ :sub:`trig`          Input impedance           50            Ω
t\ :sub:`pulse`         Pulse width       TBD            TBD    ns
======================  ================= ====== ======= ====== ==============


Information Required by DIN EN 61010-1
--------------------------------------

.. _techdata manufacturer:

Manufacturer
~~~~~~~~~~~~

The Ndigo6G is a product of:

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
systems usually consist of a Ndigo6G, a main board, a case,
application software and possible additional electronics to attach the
system to some type of detector. They might also be integrated with the
detector.

The Ndigo6G is designed to comply with **DIN EN 61326-1** when operated on
a PCIe compliant main board housed in a properly shielded enclosure. When
operated in a closed standard compliant PC enclosure the device does not
pose any hazards as defined by **EN 61010-1.**

Radiated emissions, noise immunity and safety highly depend on the
quality of the enclosure. It is the responsibility of the system
integrator to ensure that the assembled system is compliant to
applicable standards of the country that the system is operated in,
especially with regard to user safety and electromagnetic interference.
Compliance was only tested for attached cables shorter than 3 m.

When handling the board, adequate measures have to be taken to protect
the circuits against electrostatic discharge (ESD). All power supplied
to the system must be turned off before installing the board.



Environmental Conditions
~~~~~~~~~~~~~~~~~~~~~~~~
See :numref:`Section %s<techdata environmental conditions for operation>`
and :numref:`Section %s<techdata power supply>`.


Inputs
~~~~~~

All inputs are AC coupled. The inputs have very high input bandwidth
requirements and therefore there are no circuits that provide over
voltage protection for these signals.

.. danger::
  Any voltage on the inputs above **5 V**
  or below **−5 V** relative to the voltage of the slot cover can result in
  permanent damage to the board.


Recycling
~~~~~~~~~

cronologic is registered with the “Stiftung Elektro-Altgeräte Register”
as a manufacturer of electronic systems with **Registration ID DE
77895909**.

The Ndigo6G belongs to **category 9**, **“Überwachungs und
Kontrollinstrumente für ausschließlich gewerbliche Nutzung”.** The last owner
of an Ndigo6G must recycle it, treat the board in compliance with **§11**
and **§12** of the German ElektroG, or return it to the manufacturer’s address
listed in :numref:`Section %s<techdata manufacturer>`.

Export Control
~~~~~~~~~~~~~~

The Ndigo6G product line is a dual use item under
`Council Regulation (EC) No 428/2009 of 5 May 2009 setting up a Community 
regime for the control of exports, transfer, brokering and transit of dual-use
items <https://data.europa.eu/eli/reg/2009/428/2021-10-077>`__ in
section **3A002h.** Similar regulations exist in many countries outside Europe.

An export permit is required to export this product from the European
Community (EC) which will cause additional lead time. When ordering from
outside the EC, the seller will ask you for additional information
needed to obtain this permit.

Before reexporting an Ndigo6G or any product containing an Ndigo6G as a
component please check you local regulations whether an export permit is
required.

It is not permitted to export an Ndigo6G to the Russian Federation or the
Republic of Belarus.