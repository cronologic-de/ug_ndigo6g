Introduction
============

The Ndigo6G-12 offers 6400 Msps sample rate, 12 bit resolution and a greatly
improved readout rate of 6000 MB/s.  

The unit is a combined ADC/TDC board for the acquisition of pulses in 
time-of-flight applications. It builds on the established Platform of the 
`Ndigo5G-10 <https://www.cronologic.de/product/ndigo5g-10>`_ but takes it to 
the next level both in performance and flexibility.

The Ndigo6G-12 was specifically designed for time-of-flight applications like
`LIDAR <https://www.cronologic.de/applications/lidar>`_ or 
`TOF mass spectrometry <https://www.cronologic.de/applications/tof-mass-spectrometry>`_. 
Pulse arrival times can be measured with an accuracy down to 5 ps together with
information on pulse shape such as area or amplitude. 

Four channels with 1600 Msps at 12 bit resolution can be acquired
independently. Alternatively, the four channels can be combined into two
channels or decreased to a single channel. This way, either a higher temporal
resolution up to 6400 Msps or a larger dynamic range can be achieved.

Features
--------

- **12 bit** dynamic range

- Up to **6400 Msps** sample rate (in 1 channel mode) for increased resolution
  in time domain.

- Up to **four ADC channels** for your individual measurement setups.

- **Four TDC channels** with a resolution of **12** |nbws| **ns**.

- Digital TDC inputs can also be used for **gating and triggering**.

- PCIe3 x8 1.1 with **TODO** |nbws| **MB/s throughput** for simple and fast
  data transfer to most PCs.

.. - **Synchronization of up to eight boards** via reference clock if more than
  four ADC or TDC channels are required.

- **Unlimited multihit** capabilities.

- Continuous ADC readout rate of approx. **6000** |nbws| **MB/s**.

- **Zero suppression** reducing PCIe load.

- **Internal 10 MHz** clock with a time base of **50** |nbws| **ppb** or the
  **ability to use an external** 10 |nbws| MHz clock.


Board overview
--------------

+------------------------------------+---------------------------------------------+
| Optimized for                      | TOF applications                            |
+------------------------------------+---------------------------------------------+
| ADC channels                       | 4                                           |
+------------------------------------+---------------------------------------------+
| TDC channels                       | 4                                           |
+------------------------------------+---------------------------------------------+
| Gating channels                    | 4                                           |
+------------------------------------+---------------------------------------------+
| Connectors                         | 10 :math:`\times` LEMO 00                   |
+-------------+----------------------+---------------------------------------------+
| Sample rate | | Single Channel     | | 6400 Msps                                 |
|             | | Dual Channel       | | 3200 Msps                                 |
|             | | Quad Channel       | | 1600 Msps                                 |
+-------------+----------------------+---------------------------------------------+
| Resolution                         | 12 bit                                      |
+------------------------------------+---------------------------------------------+
| Double pulse resolution            | TBD                                         |
+------------------------------------+---------------------------------------------+
| Maximum bandwidth                  | TBD                                         |
+------------------------------------+---------------------------------------------+
| TDC bin size                       | 12 ps                                       |
+------------------------------------+---------------------------------------------+
| Multihit                           | unlimited                                   |
+------------------------------------+---------------------------------------------+
| Dead time between groups           | none                                        |
+--------------+---------------------+---------------------------------------------+
| Readout rate | | ADC               | | TBD                                       |
|              | | TDC               | | approx. 6000 MByte/s                      |
+--------------+---------------------+---------------------------------------------+
| Range                              | TBD                                         |
+------------------------------------+---------------------------------------------+
| Synchronization                    | up to 8 boards                              |
+------------------------------------+---------------------------------------------+
| Readout interface                  | PCIe3 :math:`\times` 8                      |
+------------------------------------+---------------------------------------------+
| Time base                          | 50 ppb (internal) or external 10 MHz clock  |
+------------------------------------+---------------------------------------------+
| On-board calibration data storage  | yes                                         |
+------------------------------------+---------------------------------------------+
| Adjustable trigger windows         | yes                                         |
+------------------------------------+---------------------------------------------+
| Possibility for overlapping events | yes                                         |
+------------------------------------+---------------------------------------------+
| Easy-to-use Windows C-API          | yes                                         |
+------------------------------------+---------------------------------------------+
| In-system firmware updates         | yes                                         |
+------------------------------------+---------------------------------------------+

