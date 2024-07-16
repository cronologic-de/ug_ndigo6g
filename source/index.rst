###########################
Ndigo6G |hyphen| User Guide
###########################


.. raw:: latex

    \RaggedRight

.. only:: html

    .. note::

        This User Guide is under active development.

.. only:: latex

    .. raw:: latex

        \newpage

    .. note::

        This User Guide is still under active development.
        For the latest version, please visit
        `docs.cronologic.de/ndigo6g <https://docs.cronologic.de/ndigo6g>`_

.. raw:: latex

    \phantomsection
    \addcontentsline{toc}{chapter}{Introduction}
    \chapter*{Introduction}

The `Ndigo6G-12 <https://www.cronologic.de/product/ndigo6g-12>`_ offers
6400 Msps sample rate, 12 bit resolution and a greatly
improved readout rate of 5200 MB/s.

The unit is a combined ADC/TDC board for the acquisition of pulses in
time-of-flight applications. It builds on the established platform of the
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

This User Guide documents the hardware and functionality of the
Ndigo6G-12 board, as well as the driver programming API provided by the
Ndigo6G-12 driver.

.. only:: latex

    This User Guide is also available online at 
    `docs.cronologic.de/ndigo6g <https://docs.cronologic.de/ndigo6g>`_.

.. only:: html

    Features
    --------

.. raw:: latex

    \phantomsection
    \addcontentsline{toc}{section}{Features}
    \section*{Features}

- **12 bit** dynamic range

- Up to **6400 Msps** sample rate (in 1-channel mode) for increased resolution
  in time domain.

- Up to **four ADC channels** for your individual measurement setups.

- **Four TDC channels** with a resolution of **13 ps**.

- **Two digital control inputs** for effective
  **gating and triggering**.

- PCIe3 x8 with **6000 MB/s throughput** for simple and fast
  data transfer to most PCs.

- **Unlimited multihit** capabilities.

- **Common start** and **common stop** capabilities.

- Continuous ADC readout rate of approx. **5200 MB/s**.

- **Zero suppression**, significantly reducing PCIe load.

- **Internal 10 MHz** clock with a time base of **10 ppb** or the
  **ability to use an external** 10 MHz clock.


.. only:: html

    Board overview
    --------------

.. raw:: latex

    \phantomsection
    \addcontentsline{toc}{section}{Board overview}
    \section*{Board overview}

+------------------------------------+---------------------------------------------+
| Optimized for                      | TOF applications                            |
+------------------------------------+---------------------------------------------+
| ADC channels                       | 4                                           |
+------------------------------------+---------------------------------------------+
| TDC channels                       | 4                                           |
+------------------------------------+---------------------------------------------+
| Digital control channels           | 2                                           |
+------------------------------------+---------------------------------------------+
| Connectors                         | 10 :math:`\times` LEMO 00                   |
+------------------------------------+---------------------------------------------+
| Sample rate                        | | 6400 Msps (1-Channel Mode)                | 
|                                    | | 3200 Msps (2-Channel Mode)                |
|                                    | | 1600 Msps (4-Channel Mode)                |
+------------------------------------+---------------------------------------------+
| Resolution                         | 12 bit                                      |
+------------------------------------+---------------------------------------------+
| Maximum bandwidth                  | TBD                                         |
+------------------------------------+---------------------------------------------+
| TDC bin size                       | 13 ps                                       |
+------------------------------------+---------------------------------------------+
| TDC double pulse resolution        | typically 4 ns                              |
+------------------------------------+---------------------------------------------+
| Multihit                           | unlimited                                   |
+------------------------------------+---------------------------------------------+
| Dead time between groups           | none                                        |
+------------------------------------+---------------------------------------------+
| Readout rate                       | | 5200 MByte/s (ADC)                        |
|                                    | | 30 MHits/s (all TDC channels)             |
|                                    | | 11.6 MHits/s (single TDC channel)         |
+------------------------------------+---------------------------------------------+
| Timestamp range                    | 106 d                                       |
+------------------------------------+---------------------------------------------+
| Readout interface                  | PCIe3 x8                                    |
+------------------------------------+---------------------------------------------+
| Time base                          | 10 ppb (internal) or external 10 MHz clock  |
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


.. only:: html

    Contents
    --------

.. toctree::
    :maxdepth: 2
    :numbered: 3

    hardware/index
    functionality/index
    api/index
    packform/index
    example/index
    techdata
    revhistory

.. only:: html

    .. toctree::

        genindex
