Information Required by DIN EN 61010-1
======================================

Manufacturer
------------

The Ndigo5G is a product of:

   | cronologic GmbH & Co. KG
   | Jahnstraße 49
   | 60318 Frankfurt

   HRA 42869 beim Amtsgericht Frankfurt/M

   VAT-ID: DE235184378

Intended Use and System Integration
-----------------------------------

The devices are not ready to use as delivered by cronologic. It requires
the development of specialized software to fulfill the application of
the end user. The device is provided to system integrators to be built
into measurement systems that are distributed to end users. These
systems usually consist of a the Ndigo5G, a main board, a case,
application software and possible additional electronics to attach the
system to some type of detector. They might also be integrated with the
detector.

The Ndigo5G is designed to comply with DIN EN 61326-1 when operated on a
PCIe compliant main board housed in a properly shielded enclosure. When
operated in a closed standard compliant PC enclosure the device does not
pose any hazards as defined by EN 61010-1.

Radiated emissions, noise immunity and safety highly depend on the
quality of the enclosure. It is the responsibility of the system
integrator to ensure that the assembled system is compliant to
applicable standards of the country that the system is operated in,
especially with regards to user safety and electromagnetic interference.
Compliance was only tested for attached cables shorter than 3m.

When handling the board, adequate measures have to be taken to protect
the circuits against electrostatic discharge (ESD). All power supplied
to the system must be turned off before installing the board.

Cooling
-------

The Ndigo5G in its base configuration has passive cooling that requires
a certain amount of air flow. If the case design can’t provide enough
air flow to the board, a slot cooler like Zalman ZM-SC100 can be placed
next to the board. Active cooling is also available as an option to the
board.

Environmental Conditions
------------------------

See Sections `[enviro_op] <#enviro_op>`__ and
`[enviro_store] <#enviro_store>`__.

Inputs
------

All inputs are AC coupled. The inputs have very high input bandwidth
requirements and therefore there are no circuits that provide over
voltage protection for these signals. Any voltage on the inputs above 5V
or below -5V relative to the voltage of the slot cover can result in
permanent damage to the board.

Known Bugs
----------

The Ndigo5G does not work in most Thunderbolt PCIe extension enclosures.
The reason is unknown.

Workarounds
~~~~~~~~~~~

Use Ndigo6G
   | 
   | All other cronologic products work reliably in Thunderbolt
     enclosures. The Ndigo6G offers very similar functionality to the
     Ndigo5G at a higher performance. When using the Ndigo6G as a
     replacement, there are some software changes required in the device
     configuration. The readout data format and API is identical.
   | See
     `www.cronologic.de/products/adcs/ndigo6g-12 <https://www.cronologic.de/products/adcs/ndigo6g-12>`__
     for details.

Use Ndigo Crate
   | 
   | Up to eight Ndigo5G can be used in an Ndigo Crate connected to a
     PC. Electrically the setup is similar to an external Thunderbolt
     enclosure, but the PC must have a vacant PCIe slot.
   | See
     `www.cronologic.de/products/pcie/pcie-crates <https://www.cronologic.de/products/pcie/pcie-crates>`__
     for details.

All other cronogic products work reliably in Thundberbolt enclosure.
Consider using an Ndigo6G as a replace

6.3.6 Recycling
~~~~~~~~~~~~~~~

cronologic is registered with the “Stiftung Elektro-Altgeräte Register”
as a manufacturer of electronic systems with Registration ID DE
77895909.

The Ndigo5G belongs to category 9, “Überwachungs und Kontrollinstrumente
für ausschließlich gewerbliche Nutzung”. The last owner of an Ndigo5G
must recycle it, treat the board in compliance with §11 and §12 of the
German ElektroG, or return it to the manufacturer’s address listed on
page .

Export Control
--------------

The Ndigo5G product line is a dual use item under `Council Regulation
(EC) No 428/2009 of 5 May 2009 setting up a Community regime for the
control of exports, transfer, brokering and transit of dual-use
items <https://data.europa.eu/eli/reg/2009/428/2021-10-077>`__ in
section 3A002h. Similar regulations exist in many countries outside
Europe.

An export permit is required to export this product from the European
Community (EC) which will cause additional lead time. When ordering from
outside the EC, the seller will ask you for additional information
needed to obtain this permit.

Before reexporting an Ndigo5G or any product containing an Ndigo5G as a
component please check you local regulations whether an export permit is
required.
