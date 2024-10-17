Technical Data
==============

- Input Passband: **1 MHz** to **950 MHz**

- Power Requirements: **35 W**

- Mechanical Dimensions:
  **170 mm** :math:`\times` **106 mm** :math:`\times` **22 mm**
  (fits in one PCIe slot)

- Throughput: **5200 MByte/s** on PCIe x8


Digitizer Characteristics
-------------------------

Each board is tested against the values listed in the |bdq| Min |edq| column.
|bdq| Typical |edq| is the mean value of the first 10 boards that were produced.


1-Channel-Mode (6.4 Gsps)
~~~~~~~~~~~~~~~~~~~~~~~~~

+------------------------+--------------------------+-----+---------+-----+-------+
| Symbol                 | Parameter                | Min | Typical | Max | Units |
+========================+==========================+=====+=========+=====+=======+
| THD\ :sub:`1`          | Total Harmonic           |     | −67     | −56 | dB    |
|                        | Distortion               |     |         |     |       |
+------------------------+--------------------------+-----+---------+-----+-------+
| SNR\ :sub:`1`          | Signal-to-Noise Ratio    | 53  | 54      |     | dB    |
+------------------------+--------------------------+-----+---------+-----+-------+
| SFDR\ :sub:`incl,1`    | Spurious Free Dynamic    | 58  | 75      |     | dB    |
|                        | Range (including         |     |         |     |       |
|                        | Harmonics)               |     |         |     |       |
+------------------------+--------------------------+-----+---------+-----+-------+
| SFDR\ :sub:`excl,1`    | Spurious Free Dynamic    | 71  | 75      |     | dB    |
|                        | Range (excluding         |     |         |     |       |
|                        | Harmonics)               |     |         |     |       |
+------------------------+--------------------------+-----+---------+-----+-------+
| SINAD\ :sub:`1`        | Signal-to-Interference   | 49  | 54      |     | dB    |
|                        | Ratio including Noise    |     |         |     |       |
|                        | and Distortion           |     |         |     |       |
+------------------------+--------------------------+-----+---------+-----+-------+
| ENOB\ :sub:`1`         | Effective Number of Bits | 8.5 | 8.7     |     |       |
+------------------------+--------------------------+-----+---------+-----+-------+


2-Channel-Mode (3.2 Gsps)
~~~~~~~~~~~~~~~~~~~~~~~~~

+-----------------------+---------------------------+-----+---------+-----+-------+
| Symbol                |  Parameter                | Min | Typical | Max | Units |
+=======================+===========================+=====+=========+=====+=======+
| THD\ :sub:`2`         |  Total Harmonic           |     | −70     | −56 | dB    |
|                       |  Distortion               |     |         |     |       |
+-----------------------+---------------------------+-----+---------+-----+-------+
| SNR\ :sub:`2`         |  Signal-to-Noise Ratio    | 54  | 54      |     | dB    |
+-----------------------+---------------------------+-----+---------+-----+-------+
| SFDR\ :sub:`incl,2`   |  Spurious Free Dynamic    | 58  | 75      |     | dB    |
|                       |  Range (including         |     |         |     |       |
|                       |  Harmonics)               |     |         |     |       |
+-----------------------+---------------------------+-----+---------+-----+-------+
| SFDR\ :sub:`excl,2`   |  Spurious Free Dynamic    | 71  | 77      |     | dB    |
|                       |  Range (excluding         |     |         |     |       |
|                       |  Harmonics)               |     |         |     |       |
+-----------------------+---------------------------+-----+---------+-----+-------+
| SINAD\ :sub:`2`       |  Signal-to-Interference   | 49  | 54      |     | dB    |
|                       |  Ratio including Noise    |     |         |     |       |
|                       |  and Distortion           |     |         |     |       |
+-----------------------+---------------------------+-----+---------+-----+-------+
| ENOB\ :sub:`2`        |  Effective Number of Bits | 8.5 | 8.7     |     |       |
+-----------------------+---------------------------+-----+---------+-----+-------+


4-Channel-Mode (1.6 Gsps)
~~~~~~~~~~~~~~~~~~~~~~~~~

+---------------------+--------------------------+-----+---------+-----+-------+
| Symbol              | Parameter                | Min | Typical | Max | Units |
+=====================+==========================+=====+=========+=====+=======+
| THD\ :sub:`4`       | Total Harmonic           |     | −68     | −56 | dB    |
|                     | Distortion               |     |         |     |       |
+---------------------+--------------------------+-----+---------+-----+-------+
| SNR\ :sub:`4`       | Signal-to-Noise Ratio    | 53  | 55      |     | dB    |
+---------------------+--------------------------+-----+---------+-----+-------+
| SFDR\ :sub:`incl,4` | Spurious Free Dynamic    | 58  | 74      |     | dB    |
|                     | Range (including         |     |         |     |       |
|                     | Harmonics)               |     |         |     |       |
+---------------------+--------------------------+-----+---------+-----+-------+
| SFDR\ :sub:`excl,4` | Spurious Free Dynamic    | 71  | 75      |     | dB    |
|                     | Range (excluding         |     |         |     |       |
|                     | Harmonics)               |     |         |     |       |
+---------------------+--------------------------+-----+---------+-----+-------+
| SINAD\ :sub:`4`     | Signal-to-Interference   | 49  | 54      |     | dB    |
|                     | Ratio including Noise    |     |         |     |       |
|                     | and Distortion           |     |         |     |       |
+---------------------+--------------------------+-----+---------+-----+-------+
| ENOB\ :sub:`4`      | Effective Number of Bits | 8.5 | 8.7     |     |       |
+---------------------+--------------------------+-----+---------+-----+-------+


Oscillator Time Base
--------------------

+-------------------+------------------------------------------------+-----+---------+------+-----+
| Symbol            | Parameter                                      | Min | Typical | Max  | ppb |
+===================+================================================+=====+=========+======+=====+
| ΔT                | Temperature stability −20 °C to 70 °C\ :sup:`1`|     |         | 10   | ppb |
+-------------------+------------------------------------------------+-----+---------+------+-----+
| F\ :sub:`0`       | Initial calibration                            |     |  <300   | 500  | ppb |
+-------------------+------------------------------------------------+-----+---------+------+-----+
| ΔF / F\ :sub:`1`  | Aging first year                               |     |         | 100  | ppb |
+-------------------+------------------------------------------------+-----+---------+------+-----+
| ΔF / F\ :sub:`20` | All inclusive aging 20 years                   |     |         | 1000 | ppb |
+-------------------+------------------------------------------------+-----+---------+------+-----+
|                   | Warm-up\ :sup:`2`                              |     |         | 3    | min.|
+-------------------+------------------------------------------------+-----+---------+------+-----+

:sup:`1`\ Over –40 °C to +85 °C; relative to stabilized frequency after 1 hour
of continuous operation

:sup:`2`\ @+25 °C; within ±100 ppb of F, where F is the stabilized frequency
reached after 1 hour of continuous operation



Electrical Characteristics
--------------------------

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
|         | non condensing          |      |         |      |                              |
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

=============== ============================================== ====== ======= ===== =====
Symbol          Parameter                                      Min    Typical Max   Units
=============== ============================================== ====== ======= ===== =====
I\ :sub:`3.3`   PCIe 3.3 V rail power consumption                      0.42          W
VCC\ :sub:`3.3` PCIe 3.3 V rail power supply                   3.1     3.3    3.6    V
I\ :sub:`12`    PCIe 12 V rail power consumption\ :sup:`1`             31            W
VCC\ :sub:`12`  PCIe 12 V rail power supply\ :sup:`1`          11.1    12     12.9   V
I\ :sub:`aux`   PCIe 3.3 V\ :sub:`aux` rail power consumption          0             W
VCC\ :sub:`aux` PCIe 3.3 V\ :sub:`aux` rail power supply               3.3           V
=============== ============================================== ====== ======= ===== =====

.. note::

  :sup:`1` The 12 V power is sourced solely from the PCIe power connector
  located at the rear of the board.


Analog Inputs
~~~~~~~~~~~~~

AC coupled single-ended analog inputs:

+---------------+---------------------------+------+---------+-----+-------+
|Symbol         |  Parameter                | Min  | Typical | Max | Units |
+===============+===========================+======+=========+=====+=======+
| V\ :sub:`p-p` | Peak to peak input voltage|      |         | 1   | V     |
+---------------+---------------------------+------+---------+-----+-------+
| Z\ :sub:`p`   | Input impedance           |      | 50      |     | Ω     |
+---------------+---------------------------+------+---------+-----+-------+
| V\ :sub:`offs`| Adjustable offset         | -0.5 |         | 0.5 | V     |
+---------------+---------------------------+------+---------+-----+-------+

Digital Inputs
~~~~~~~~~~~~~~

AC coupled single-ended digital inputs:

+---------------+---------------------------+------+---------+-----+-------+
|Symbol         |  Parameter                | Min  | Typical | Max | Units |
+===============+===========================+======+=========+=====+=======+
| V\ :sub:`p-p` | Peak to peak input voltage|      |         | 1.3 | V     |
+---------------+---------------------------+------+---------+-----+-------+
| Z\ :sub:`p`   | Input impedance           |      | 50      |     | Ω     |
+---------------+---------------------------+------+---------+-----+-------+
| V\ :sub:`offs`| Adjustable offset         | -1.3 |         | 1.3 | V     |
+---------------+---------------------------+------+---------+-----+-------+


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

The Ndigo6G is designed to comply with **DIN EN 61326-1** when operated on
a PCIe compliant main board housed in a properly shielded enclosure. When
operated in a closed standard compliant PC enclosure the device does not
pose any hazards as defined by **EN 61010-1.**

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
requirements and therefore there are no circuits that provide overvoltage
protection for these signals.

.. danger::
  Any voltage on the inputs above **5 V**
  or below **−5 V** relative to the voltage of the slot cover can result in
  permanent damage to the board.


Recycling
~~~~~~~~~

cronologic is registered with the “Stiftung Elektro-Altgeräte Register”
as a manufacturer of electronic systems with **Registration ID DE
77895909**.

The Ndigo6G-12 belongs to **category 9**, **“Überwachungs und
Kontrollinstrumente für ausschließlich gewerbliche Nutzung”.** The last owner
of an Ndigo6G-12 must recycle it, treat the board in compliance with **§11**
and **§12** of the German ElektroG, or return it to the manufacturer’s address
listed in :numref:`Section %s<techdata manufacturer>`.

Export Control
~~~~~~~~~~~~~~

The Ndigo6G product line is a dual-use item under
`Council Regulation (EC) No 428/2009 of 5 May 2009 <https://eur-lex.europa.eu/eli/reg/2009/428/oj>`__
in section **3A002h.** Similar regulations exist in many countries outside
Europe.

Regardless of the fact that we at cronologic exclude the use of our
products for military purposes, **the laws of the EU and many other countries
restrict exports** of dual-use items.
Since we have to apply for a **General Export Permit** for these countries,
delivery processes may be delayed or delivery to certain countries may
become impossible.

For the application of this
`export license <https://www.cronologic.de/faq/export-license>`__
we need the following documents from you:

- Exporter declaration
- Company profile
- Import license (country dependent)

There are countries for which a **General Export License** can be used for the
export of dual-use goods. In this case we need the corresponding documents from
you and there will be no further delay. Included countries are:

- Australia
- Japan
- Canada
- Liechtenstein
- New Zealand
- Norway
- Switzerland
- Singapore
- USA

Before re-exporting an Ndigo6G or any product containing an Ndigo6G as a 
component, please check you local regulations whether an export permit is 
required.

It is not permitted to export an Ndigo6G to the Russian Federation or the
Republic of Belarus.
