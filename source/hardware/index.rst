
Hardware
========

.. toctree::
   :caption: Contents

   installation
   connections
   update
   calibration





.. Extension Card
.. --------------

.. The **Ndigo Extension Card** provides additional inputs or outputs to the
.. FPGA. It is connected to the C1 (Samtec QSS-025) connector on an **Ndigo5G** by
.. an Samtec SQCD cable assembly.

.. The **Ndigo Extension Card** provides up to ten single ended LEMO00
.. connectors. The circuit connecting to each of these circuits can be
.. chosen to provide inputs or outputs. These can be AC or DC coupled. AC
.. coupled inputs support NIM signaling.

.. The signals connect to 2.5 |nbws| V IO Pins of the Xilinx Virtex-5 FPGA.
.. The current firmware revision provides the following signal connections.


.. .. container:: small

..       +-----------------+---------+----------+-----------+-----------------+
..       | Connector       | QSS Pin | FPGA Pin | Direction | Signal          |
..       +=================+=========+==========+===========+=================+
..       | LEMO00: CH0     | 22      | AD9      | Input     | Ndigo Extension |
..       |                 |         |          |           | digital channel |
..       |                 |         |          |           | 0               |
..       +-----------------+---------+----------+-----------+-----------------+
..       | LEMO00: CH1     | 18      | AE10     | Input     | Ndigo Extension |
..       |                 |         |          |           | digital channel |
..       |                 |         |          |           | 1               |
..       +-----------------+---------+----------+-----------+-----------------+
..       | LEMO00: CH2     | 14      | D10      |           | not connected   |
..       +-----------------+---------+----------+-----------+-----------------+
..       | LEMO00: CH3     | 10      | AF9      | Output    | 39.0625 MHz     |
..       |                 |         |          |           | clock for HPTDC |
..       +-----------------+---------+----------+-----------+-----------------+
..       | LEMO00: CH4     | 6       | AD11     | Output    | 39.0625 MHz     |
..       |                 |         |          |           | clock for HPTDC |
..       +-----------------+---------+----------+-----------+-----------------+
..       | LEMO00: CH5     | 5       | AE7      | Output    | 39.0625 MHz     |
..       |                 |         |          |           | clock for HPTDC |
..       +-----------------+---------+----------+-----------+-----------------+
..       | LEMO00: CH6     | 9       | AF7      | Output    | 39.0625 MHz     |
..       |                 |         |          |           | clock for HPTDC |
..       +-----------------+---------+----------+-----------+-----------------+
..       | LEMO00: CH7     | 13      | D9       |           | not connected   |
..       +-----------------+---------+----------+-----------+-----------------+
..       | LEMO00: CH8     | 17      | V9       | Input     | Ndigo Extension |
..       |                 |         |          |           | digital channel |
..       |                 |         |          |           | 2               |
..       +-----------------+---------+----------+-----------+-----------------+
..       | LEMO00: CH9     | 21      | W9       | Input     | Ndigo Extension |
..       |                 |         |          |           | digital channel |
..       |                 |         |          |           | 3               |
..       +-----------------+---------+----------+-----------+-----------------+
..       | SYNC1:          | 26      | F9       |           | not connected   |
..       | Sync-TDC8       |         |          |           |                 |
..       +-----------------+---------+----------+-----------+-----------------+
..       | SYNC1:          | 44      | AA7      | Output    | Sync for HPTDC  |
..       | Sync-HPTDC      |         |          |           |                 |
..       +-----------------+---------+----------+-----------+-----------------+



.. The four digital inputs are routed to the bus inputs of the trigger matrix
.. to be used for triggering. The routing can be configured to either *OR*\ ing
.. the sync bus and extension channels or use the extension channels
.. exclusively.

.. .. container:: small

..    +-------------+-----------------+--------------------------+----------------------+
..    | Connector   | Extension Card  | Trigger matrix input     | Trigger matrix input |
..    +-------------+-----------------+--------------------------+----------------------+
..    |             | Digital Channel | ignorecable = 0          | ignorecable = 1      |
..    +-------------+-----------------+--------------------------+----------------------+
..    | LEMO00: CH0 | 0               | BUS0 = EXT0 Sync Cable 0 | BUS0 = EXT0          |
..    +-------------+-----------------+--------------------------+----------------------+
..    | LEMO00: CH1 | 1               | BUS1 = EXT1 Sync Cable 1 | BUS1 = EXT1          |
..    +-------------+-----------------+--------------------------+----------------------+
..    | LEMO00: CH8 | 2               | BUS2 = EXT2 Sync Cable 2 | BUS2 = EXT2          |
..    +-------------+-----------------+--------------------------+----------------------+
..    | LEMO00: CH9 | 3               | BUS3 = EXT3 Sync Cable 3 | BUS3 = EXT3          |
..    +-------------+-----------------+--------------------------+----------------------+




.. Ndigo5G Functionality
.. ---------------------

.. Trigger Blocks
.. ~~~~~~~~~~~~~~




.. Auto Triggering Function Generator
.. ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. Some applications require periodic or random triggering. **Ndigo5G**’s
.. function generator provides this functionality.

.. The delay between two trigger pulses of this trigger generator is the
.. sum of two components: A fixed value :math:`M` and a pseudo-random value given
.. by the exponent :math:`N`.

.. The period is

..
   .. math::
      T = 1 + M + [1...2^N]

.. clock cycles with a duration of 3.2 |nbws| ns per cycle.

.. This allows to monitor input signals at times the current trigger
.. configuration does not trigger, e. g., to get base line information in
.. mass spectrometry applications. It can also be used to determine a
.. suitable threshold level for the trigger by first getting random
.. statistics on the input signal.

.. Timestamp Channel
.. ~~~~~~~~~~~~~~~~~

.. The timestamp channel produces a stream of small packets that denote the
.. time of the trigger event. An arbitrary set of trigger sources can be
.. selected in the trigger matrix to cause the creation of a packet.

.. The packets have a fixed length of 16 bytes. The format is described in
.. :numref:`Chapter %s<struct ndigopacket>`. The length field of the packet
.. contains a 32-bit pattern that contains the levels of all trigger sources at
.. the time of the trigger event except for the period monitor. Only one packet
.. is created, no matter how many trigger sources caused the timestamp channel to
.. trigger.

.. Data Lookup Table
.. ~~~~~~~~~~~~~~~~~

.. In some applications it might be useful to modify the ADC sample data by
.. a user defined function :math:`f(x)`. In this case the onboard FPGA is
.. able to perform this task such that the the data stream consists of data
.. words :math:`f(sample)` instead of :math:`sample`. The function :math:`f(x)` is
.. applied using a 1024 word lookup table (LUT) which needs to be provided
.. by the user. This is done by defining the corresponding function as a
.. custom_lut-member of the ndigo_configuration structure. Please feel free
.. to contact cronologic if you plan the use this feature. The onboard INL
.. correction is applied prior to mapping the LUT values.


.. Multiple Ndigo boards synchronization
.. -------------------------------------

.. Using several Ndigo devices in applications that use more channels than
.. a single board can provide requires synchronized operation. To ensure
.. exact synchronization, a delay parameter needs to be set for each board.
.. This parameter might change in case boards are swapped, added or removed
.. and in some cases might change after a firmware update.

.. The calibration tool “MultiboardCalibration.exe” is available after
.. installing the Ndigo device driver. It is used to find appropriate delay
.. values for each board in a given board setup. After starting, the
.. application lists all Ndigo boards found
.. \(:numref:`Figure %s<fig SyncCalibTool>`).

.. .. _fig synccalibtool:
.. .. figure:: figures/SyncCalibTool.*

..    Main window of the multiple boards sync calibration tool.

.. A board’s appropriate delay depends on whether it operates in master or
.. slave mode. The respective values can be set in the column “Delay M”
.. (for master boards) and “Delay S” (for slave boards). The designated
.. master board can be selected in the column “Master”. The calibration
.. procedure creates a histogram for each board displaying the current
.. delay between the boards. The histogram can be viewed by clicking on
.. “Show!”. When the appropriate delay values are found they can be stored
.. in the on-board flash PROM by clicking “Do it!” separately for each
.. board. Clicking “Flash All!” will write the values to all boards at
.. once. Please note: Flashing the values might take up to 10 seconds
.. during which the program might not respond.

.. .. note::

..    If the application reports a “PLL not locked” error
..    check the cable. If the recording of histograms does not make progress
..    check the cable. Make sure the cable is properly terminated at both ends
..    and firmly attached to each card.

.. Calibration Procedure
.. ~~~~~~~~~~~~~~~~~~~~~

.. #. Make sure “Automode” is selected.

.. #. Record the calibration histograms by pressing “Record histograms”.
..    The program will perform up to 200 measurements of the sync delay.
..    After accumulating some data, the delay values found are reported in
..    the column “AutoMmt”. The values can be verified by examining the
..    histogram that was recorded. A board’s histogram should look like the
..    one shown in :numref:`Figure %s <fig HistoUncalib>`.
..    During normal operation the delay will be adjusted such that the data
..    points accumulated roughly coincide with the vertical markers in the
..    upper panel. As the delay pattern is periodic valid delay values are
..    between 0 and 31. Thus, the delay value found by the auto measurement
..    should correspond to the distance between the vertical markers and
..    accumulated data points. Hint: When moving the mouse pointer across
..    the histogram the delay value of the current location is displayed.

.. #. After stopping the data acquisition, by pressing “Record Histograms”
..    again or waiting for 200 measurements to complete, the delay values
..    of the auto measurement need to be copied to the columns “Delay M” or
..    “Delay S” depending on the corresponding board being a master or a
..    slave. The correct field to copy the value to is highlighted in
..    green.

.. #. You may record a new dataset as a crosscheck that the delay is now
..    set to an appropriate value. By disabling “Automode” the new delay
..    values are used. Press “Record Histograms” in order to start the data
..    acquisition. After some time the histogram should look similar to the
..    one in :numref:`Figure %s<fig HistoCalib>`.

.. #. The delay values for all boards in a set needs to be found. For the
..    case a board acts as a master, the value “Delay M” needs to be
..    adjusted, in case it is a slave, the “Delay S” parameter needs to be
..    changed. In order to find the master-case delay values for all
..    boards, the calibration procedure needs to be performed with every
..    board acting as a master once. After changing the master board, the
..    slave values of the other boards don’t need to be readjusted. Only
..    Ndigo5G boards may be set as masters. Therefore, a Ndigo250M board
..    only needs to be calibrated as a slave.

.. #. After finding all delay values, write the values to the on-board
..    flash PROMs by pressing “Flash All!”.

.. .. _fig HistoUncalib:
.. .. figure:: figures/HistoUncalib.*

..    Histogram for the case that the delay value for the board is not set
..    correctly. Please note that the lower panel might differ from board to
..    board, with the |bdq| step |edq| being at a different position.

.. .. _fig HistoCalib:
.. .. figure:: figures/HistoCalib.*

..    Histogram for the case that the delay value of the board is set correctly.
      Please note that the lower panel might differ from board to board, with the
      |bdq| step |edq| being at a different position.

.. Synchronizing a Ndgio5G and an HPTDC8-PCI
.. ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. In order to operate a Ndigo5G in sync with one ore more HPTDC8-PCI
.. boards, a board to board interconnection using a Ndigo Extension Board
.. needs to be done. The Ndigo Extension Board has four clock outputs. One
.. of them needs to be connected to the external clock input of the HPTDC
.. using a standard Lemo 00 cable. The Ndigo5G is connected to the Ndigo
.. Extension Board using the Samtec ribbon cable provided with the Ndigo
.. Extension Board. The signals used for synchronization of the boards are
.. transmitted by a standard 10pin ribbon cable connecting the Ndigo
.. Extension Board and the HPTDC. A schematic of all necessary connections
.. is shown in :numref:`Figure %s<fig InterconNdigo>`.

.. In principle the user can use the standard device drivers of the Ndigo5G
.. and the HPTDC8-PCI to perform data acquisition. It is, however,
.. recommended to use the cronoSync-library, which is a part of the
.. cronoTools provided with with the Ndigo5G device driver. CronoSync
.. offers an easy group-based access to the data recorded and handles the
.. synchronization of all cronologic data ac-quisition devices used. A
.. detailed description of cronoTools and cronoSync can be found in the
.. cronoTools user guide.

.. .. _fig InterconNdigo:
.. .. figure:: figures/InterconNdigo.*

..    Interconnection scheme of a Ndigo5G (left) and a HPTDC8-PCI (right)
..    using a Ndigo Extension Board (middle).


.. Performing a firmware update
.. ----------------------------

.. After installing the Ndigo device driver, a firmware update tool is
.. available. By choosing “NdigoFirmwareGUI.exe” a firmware update can be
.. performed. After invoking the application a window as shown in
.. :numref:`Figure %s<fig Firmware>` will appear. The tool can be used for
.. updating the firmware and to create a backup of the on-board calibration
.. data of the Ndigo unit. If several boards are present, the one which is
.. going to be used can be selected in the upper left corner of the window.
.. Pressing the “Backup” buttons a backup of the firmware or the
.. calibration data will be created, respectively. In order to perform a
.. firmware update, chose the “.ndigorom”-file to used by pressing
.. “Browse”. The file contains the firmware PROMs for all boards of the
.. Ndigo product line. By pressing “Flash” the firmware is written to the
.. board. “Verify” can be used to compare the data stored inside the PROM
.. to the one inside a file.


.. .. _fig Firmware:
.. .. figure:: figures/Firmware.*

..    The firmware update and calibration data backup tool as provided with the
..    Ndigo device driver.

.. .. note::

..    The new firmware will only be used after a power
..    cycle, i.e., after switching the PC (or Ndigo crate) off and back on. A
..    simple reboot is not sufficient. Therefore the information shown in the
..    upper half of the application window does not change right after
..    flashing a new firmware.

.. After flashing and shutting the PC or the crate off and on again it is
.. recommended to perform a window calibration. The tool
.. “WindowCalibration” is provided for that purpose within the driver
.. installation. The omission of the calibration process leads to longer
.. execution times of applications using that firmware, since the
.. calibration is performed then instead.


.. Calibrating the TDC
.. -------------------

.. After each update of the Ndigo5G-10 firmware the TDC has to be
.. calibrated. The calibration is done with the tool “TDCCalibration.exe”
.. which is available after installing the Ndigo device driver. After
.. invoking the application a window as shown in
.. :numref:`Figure %s<fig Calib>` will appear.

.. .. _fig Calib:
.. .. figure:: figures/Calib.*

..    The TDC calibration tool as provided with the Ndigo device driver.

.. The calibration procedure is as follows:

.. #. Connect an external pulse signal to the Trigger input. The signal
..    should be low active with a frequency in the kHz range. It must not
..    be synchronized to the clock source of the Ndigo5G-10. The input
..    frequency must not exceed 10 MHz. The pulse low and high width has to
..    be at least 10ns each.

.. #. Set *Serial Number* according to the sticker on the card if the shown
..    value is not correct.

.. #. Start capturing pulse events by pressing the *Start* button.

.. #. Adjust the *Input Offset* so that *First Bin* is in the range of 4 to
..    16\. If *First Bin* is less than 4, increment *Input Offset* by one.
..    If *First Bin* is greater than 16 decrement *Input Offset* by one.
..    Repeat increment/decrement until *First Bin* is in the range of 4 to
..    16\. Depending on the firmware revision the *Input Offset* value for a
..    successful calibration may be in the range of 6–10 or 28–32.

.. #. When the *Write Calibration Data* button becomes enabled press it to
..    update the calibration data on the card.

.. #. Calibration done!

.. The card can only be successfully calibrated if:

.. -  *First Bin* is in the range of 4 to 16

.. -  *Empty Bins* is less than (First Bin + 4)

.. -  at least 10,000 events have been captured

.. -  a valid serial number is set.


..
   .. note::

      If the application reports an error check if the
      input pulse is within specification.