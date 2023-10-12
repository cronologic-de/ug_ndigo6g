.. role:: cpp(code)
    :language: c++

Driver Programming API
======================

.. raw:: latex

    \begingroup
    %\RaggedRight

The API is a DLL with C linkage. The functions provided by the DLL are declared
in |br| :code:`Ndigointerface.h`.



Constants
---------

:cpp:`#define NDIGO_CHANNEL_COUNT 4`
    The number of analog input channels.

:cpp:`#define NDIGO_GATE_COUNT 4`
    The number of gating blocks.

:cpp:`#define NDIGO_TRIGGER_COUNT 16`
    The number of triggers. Two per analog input, one per digital input plus some specials.

:cpp:`#define NDIGO_ADD_TRIGGER_COUNT 6`
    Additional set of triggers for digital inputs.




Initialization
--------------

:cpp:`int ndigo_count_devices(int *error_code, char **error message)`
    Return the number of boards that are supported by this driver in the system. 

:cpp:`int ndigo_get_default_init_parameters(ndigo_init_parameters  *init)`
    Get a set of default parameters to feed into **ndigoinit().**
    This must always be used to initialize the **ndigo_init_parameter** structure.

:cpp:`ndigo_device *ndigo_init(ndigo_init_parameters *params, int *error_code, char **error_message)`
    Open and initialize the Ndigo board with the given index.
    With :cpp:`error_code` and :cpp:`error_message`
    the user must provide pointers where to buffers where error information
    should be written by the driver.
    The buffer for the error message must by at least **80 chars** long. 
    Params is a structure of type
    **ndigo_init_parameters** that must be completely initialized. 

:cpp:`int ndigo_close(ndigo_device *device)`
    Finalize the driver for this device. 




Structure :code:`ndigo_init_parameters`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:cpp:`int version`
    Must be set to :cpp:`NDIGO_API_VERSION`

:cpp:`int card_index`
    The index in the list of **Ndigo5G** boards that should be initialized. 
    There might be multiple boards in the system that are handled by this driver
    as reported by :cpp:`ndigo_count_devices`. This index selects one of them.
    Boards are enumerated depending on the PCIe slot. The lower the bus number
    and the lower the slot number the lower the card index.  int board_id This
    8-bit number is filled into each packet created by the board and is useful
    if data streams of multiple boards will be merged. If only **Ndigo5G**
    cards are used this number can be set to the card index. If boards of
    different types that use a compatible data format are used in a system
    each board should get a unique id.  Can be changed with |br|
    :cpp:`int ndigosetboardid(ndigodevice *device, int boardid)`. 

:cpp:`ndigo_bool_t use_external_clock`
    Use **10** |nbws| **MHz** clock supplied by IPC flat band cable. Must be
    set for all slaves. 

:cpp:`ndigo_bool_t drive_external_clock`
    Drive internal 10MHz clock of this board to IPC flat band cable.
    Must be set for master. 

:cpp:`ndigo_bool_t is_slave`
    Data acquisition of this board is controlled by the master board. 
    :cpp:`int sync_period` Period of the multicard sync pulse. Should be set to
    **4** (default) when using several Ndigo boards in sync. Ignored for single
    board setups.  The **Ndigo5G** has four phases relative to the global
    **10** |nbws| **MHz** clock. 

:cpp:`int sync_delay`
    Fine tap delay for incoming sync signals. 

:cpp:`ndigo_bool_t force_window_calibration`
    If :cpp:`true` / :cpp:`1`, valid data window is detected at initialization.
    Default value is :cpp:`false` / :cpp:`0`: values from flash memory are used
    in order to set data window to correct position.  
    
:cpp:`ndigo_bool_t hptdc_sync_enabled`
    A **HPTDC** is connected to this board. Enables the clock and sync line
    from the **Ndigo5G** to the **HPTDC**. 

:cpp:`__int64 buffer_size[8]`
    The minimum size of the DMA buffer.
    If set to :cpp:`0` the default size of **16** |nbws| **MByte** is used.
    **Ndigo5G** only uses :cpp:`buffer_size[0]`.

:cpp:`int buffer_type`
    Must be set to :cpp:`NDIGO_BUFFER_ALLOCATE`.

:cpp:`__int64 buffer_address`
    Ignored. Might be used for future buffer types. 

:cpp:`int variant`
    Set to :cpp:`0`. Can be used to activate future device variants such
    as different base frequencies. 

:cpp:`int device_type`
    Initialized by :cpp:`ndigo_get_default_init_parameters()`.
    Must be left unchanged. 

    * :cpp:`#define CRONO_DEVICE_HPTDC 0`
    * :cpp:`#define CRONO_DEVICE_NDIGO5G 1`
    * :cpp:`#define CRONO_DEVICE_NDIGO250M 2`

:cpp:`int_dma read_delay`
    Initialized by :cpp:`ndigo_get_default_init_parameters()`.
    The write pointer update is delay by this number of **4** |nbws| **ns**
    clock periods to hide race conditions between software and DMA. 


Status Information
------------------

Functions for Information Retrieval
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The driver provides functions to retrieve detailed information on the type
of board, its configuration, settings and state. The information is split
according to its scope and the computational requirements to query the
information from the board. 

:cpp:`int ndigo_get_driver_revision()`
    Returns the driver version, same format
    as ndigo_static_info::driver_revision.  This function does not require a
    present **Ndigo5G** device. 

:cpp:`const char* ndigo_get_driver_revision_str()`
    Returns the driver version including SVN build revision as a string. 
    This function does not require a present **Ndigo5G** device. 

:cpp:`int ndigo_get_static_info(ndigo_device *device, ndigo_static_info *info)`
    This structure contains information about the board that does not change
    during run time. 

:cpp:`int ndigo_get_param_info(ndigo device *device, ndigo_param_info *info)`
    The structure returned by this call contains information that changes
    indirectly due to configuration changes. 

:cpp:`int ndigo_get_fast_info(ndigo device *device, ndigo_fast_info *info)`
    This call returns a structure that contains dynamic information that can
    be obtained within a few microseconds. 

:cpp:`int ndigo_get_slow_info(ndigo device *device, ndigo_slow_info *info)`
    The data reported in this structure requires milliseconds to be obtained.
    The application should only call it in situation where the program flow can
    cope with an interruption of that magnitude. 

:cpp:`const char* ndigo_get_last_error_message(ndigo_device *device)`


Structure :cpp:`ndigo_static_info`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This structure contains information about the board that does not change
during run time. It is provided by the function 
:cpp:`ndigo_get_static_info`.

:cpp:`int size`
    The number of bytes occupied by the structure.

:cpp:`int version`
    A version number that is increased when
    the definition of the structure is changed. The increment can be larger
    than one to match driver version numbers or similar. Set to **0** for all
    versions up to first release.  

:cpp:`int board_id`
    Index of the board as passed to the constructor or set via

    :cpp:`int ndigosetboardid(ndigodevice *device, int boardid)`.

:cpp:`int driver_revision`
    The lower three bytes contain a triple level hierarchy of version
    numbers, e.g., :cpp:`0x010103` encodes version 1.1.3.

    A change in the first digit generally requires a recompilation of user
    applications. Change in the second digit denote significant improvements
    or changes that don’t break compatibility and the third digit changes
    with minor bugfixes and similar updates.

:cpp:`int firmware_revision`
    Firmware revision of the FPGA configuration. This increments only when
    there is a functional change.

:cpp:`int board_revision`
    Specify the board's revision.

    * :cpp:`0`: Experimental prototypes labeled |bdq| Rev. 1 |edq|
    * :cpp:`2`: The version produced until 2010 labeled |bdq| Rev. 2 |edq|
    * :cpp:`3`: The version produced starting in 2011
      labeled |bdq| Rev. 3 |edq|

:cpp:`int board_configuration`
    Describes the schematic configuration of the board.

    * For board **revision 0**, this always reads :cpp:`0`

    * For board **revision 2**, the following assignments are valid:

      If Bit 3 is :cpp:`0`, the following is valid:

        - Bit 0 determines the ADC resolution.
          \(:cpp:`0`: 8 |nbws| bit, :cpp:`1`: 10 |nbws| bit).
        - Bit 1 determines whether the TDC-oscillator is present
          |br| (:cpp:`0`: oscillator present, :cpp:`1`: simple trigger).
        - Bit 2 determines the input connectors |br| (:cpp:`0`: single ended,
          :cpp:`1`: differential).

      If Bit 3 is :cpp:`1`, it signifies a special version of the board

        - :cpp:`0xA`: **Ndigo1250M-12**, single ended with a digital trigger
        - :cpp:`0x8`: **Ndigo5G-8**, single ended with a digital trigger

    * For board **revision 3**, the following assignments are valid:

        - Bit 2 determines the input connectors
          (:cpp:`0` = single ended, :cpp:`1` = differential).

      The other bits have one of the following patterns [Bits 3...0]:

        - :cpp:`0010`:  Ndigo5G-10 2.5u 10
        - :cpp:`0011`:  Ndigo5G-8-AQ 2.5u 8
        - :cpp:`0110`:  Ndigo5G-10-Diff 560pF 10 DIFF
        - :cpp:`1000`:  Ndigo5G-8 560pF 8+
        - :cpp:`1010`:  Ndigo1250M-12 2.2uF 12 Sciex DC
        - :cpp:`1011`:  Ndigo5G-10 560pF 10
        - :cpp:`1110`:  Ndigo5G-Sciex 2.2uF 10 Sciex Infiniband, DIFF
        - :cpp:`1111`:  Ndigo5G-Roent = fADC4/10 560pF 10


:cpp:`int adc_resolution`
    Number of bits of the ADC, set to :cpp:`0` if unknown.

:cpp:`double nominal_sample_rate`
    Sample rate in once channel mode. Usually :cpp:`5.0e9` (5 |nbws| Gsps).

:cpp:`double analog_bandwidth`
    :cpp:`3.0e9` (3 |nbws| Ghz).

:cpp:`int chip_id`
    16 |nbws| bit factory ID of the ADC chip

:cpp:`int board_serial`
    Serial number with the year minus 2000 in the highest 8 |nbws| bits of the
    integer and a running number in the lower 24 |nbws| bits. This number is
    identical with the one on the label on the board.

.. raw:: latex

    \begingroup
    \bfseries

:cpp:`int flash_serial_low`

.. raw:: latex

    \endgroup

:cpp:`int flash_serial_high`
    64 |nbws| bit manufacturer serial number of the flash chip.

:cpp:`int flash_valid`
    If not :cpp:`0` the driver found valid calibration data in the flash on the
    board and is using it.

:cpp:`ndigo_bool_t dc_coupled`
    Returns :cpp:`false` for the standard AC coupled **Ndigo5G**.

:cpp:`int subversion_revision`
    A number to track builds of the firmware in more detail than the
    firmware revision. It changes with every change in the firmware, even
    if there is no visible effect for the user.

:cpp:`char calibration_date[20]`
    DIN EN ISO 8601 string (YYYY-MM-DD HH:DD) describing the time when the
    card was calibrated.



Structure :cpp:`ndigo_param_info`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:cpp:`int size`
    The number of bytes occupied by the structure.

:cpp:`int version`
    A version number that is increased when the definition of the
    structure is changed. The increment can be larger than one to match
    driver version numbers or similar. Set to :cpp:`0` for all versions up to
    first release.

:cpp:`double bandwidth`
    Analog Bandwidth setting of the ADC. Either :cpp:`3.0e9` (3 |nbws| GHz)
    or :cpp:`1.0e9` (1 |nbws| GHz) for the 10 bit version.

:cpp:`double sample_rate`
    Sample rate. Either :cpp:`1.25e9`, :cpp:`2.5e9`, or :cpp:`5.0e9` depending
    on the current ADC mode.

    :cpp:`sample_rate * channels = 5.0e9`.

:cpp:`double sample_period`
    The period one sample in the data represents in ps.

:cpp:`int board_id`
    The number the board uses to identify the data source in the output
    data stream.

:cpp:`int channels`
    Number of channels. 1, 2 or 4 depending on the ADC mode chosen;

    :cpp:`sample_rate * channels = 5.0e9`.

:cpp:`int channel_mask`
    Mask with a set bit for each enabled input channel.

:cpp:`int64 total_buffer`
    The total amount of the DMA buffer in bytes.


Structure :cpp:`ndigo_fast_info`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:cpp:`int size`
    The number of bytes occupied by the structure

:cpp:`int version`
    A version number that is increased when the definition of the structure is
    changed.  The increment can be larger than one to match driver version
    numbers or similar. Set to :cpp:`0` for all versions up to first release.

:cpp:`int adc_rpm`
    Speed of the ADC fan. Reports :cpp:`0` if no fan is present.

:cpp:`int fpga_rpm`
    Speed of the FPGA fan. Reports :cpp:`0` if no fan is present.

:cpp:`int alerts`
    Alert bits from the system monitor.

    * Bit 0: FPGA temperature alert (:math:`>` 85°C)
    * Bit 1: Internal FPGA voltage out-of-range (:math:`<` 1.01 |nbws| V
      or :math:`>` 1.08 |nbws| V)
    * Bit 2: FPGA auxiliary voltage out-of-range. (:math:`<` 2.375 |nbws| V
      or :math:`>` 2.625 |nbws| V)
    * Bit 3: FPGA temperature critical (:math:`>` 125°C)
    * Bit 4: ADC temperature alert (:math:`>` 90°C)
    * Bit 5: ADC temperature critical (:math:`>` 100°C). ADC will automatically
      be turned off.

:cpp:`double voltage_aux`
    Auxiliary FPGA voltage, nominal 2.5 |nbws| V

:cpp:`double voltage_int`
    Internal FPGA voltage, nominal 1.0 |nbws| V

:cpp:`double fpga_temperature`
    In degree Celsius as measured on die.

:cpp:`int pcie_link_width`
    Number of PCIe lanes that the card uses. Should be :cpp:`4` for
    **Ndigo5G**.

:cpp:`int pcie_max_payload`
    Maximum size in bytes for one PCIe transaction, depends on system
    configuration.

.. _struct ndigoslowinfo:

Structure :cpp:`ndigo_slow_info`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:cpp:`int size`
    The number of bytes occupied by the structure.

:cpp:`int version`
    A version number that is increased when the definition of the structure is
    changed.  The increment can be larger than one to match driver version
    numbers or similar. Set to :cpp:`0` for all versions up to first release.

:cpp:`double adc_temperature`
    ADC temperature in degree Celsius as measured on die.

:cpp:`double board_temperature`
    Board temperature in degree celsius. 


Configuration
-------------

The device is congfiured with a configuration structure. The user should first
obtain a structure that contains the default settings of the device read from
an on board ROM, than modify the structure as needed for the user application
and use the result to configure the device.

.. raw:: latex

    \begingroup
    \RaggedRight
    \bfseries

:cpp:`int ndigo_get_default_configuration(ndigo_device *device, ndigo_configuration *config)`

:cpp:`int ndigo_get_current_configuration(ndigo_device *device, ndigo_configuration *config)`

:cpp:`int ndigo_configure(ndigo_device *device, ndigo_configuration *config)`

.. raw:: latex

    \endgroup

:cpp:`int ndigo_set_board_id(ndigo_device *device, int board_id)`
    The :cpp:`board_id` can be changed after initialization of the card. If
    *cronotools* are used, the :cpp:`board_id` changes have to be done before
    *cronotools* initialization.


Structure :cpp:`ndigo_configuration`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This is the structure containing the configuration information. It is used in
conjunction with :cpp:`ndigo_get_default_configuration`,
:cpp:`ndigo_get_current_configuration` and :cpp:`ndigo_configure`.

It uses internally the structures :cpp:`ndigo_trigger_block` and 
:cpp:`ndigo_trigger`.

:cpp:`int size`
    The number of bytes occupied by the structure.

:cpp:`int version`
    A version number that is increased when the definition of the structure
    is changed.  The increment can be larger than one to match driver version
    numbers or similar.  Set to :cpp:`0` for all versions up to first release.

:cpp:`int reserved1`
    Reserved for internal usage. Do not change.

:cpp:`int adc mode`
    Constant describing the ADC mode

    .. code:: c++

        #define NDIGO_ADC_MODE_ABCD 0
        #define NDIGO_ADC_MODE_AC 4
        #define NDIGO_ADC_MODE_BC 5
        #define NDIGO_ADC_MODE_AD 6
        #define NDIGO_ADC_MODE_BD 7
        #define NDIGO_ADC_MODE_A 8
        #define NDIGO_ADC_MODE_B 9
        #define NDIGO_ADC_MODE_C 10
        #define NDIGO_ADC_MODE_D 11
        #define NDIGO_ADC_MODE_AAAA 12
        #define NDIGO_ADC_MODE_BBBB 13
        #define NDIGO_ADC_MODE_CCCC 14
        #define NDIGO_ADC_MODE_DDDD 15
        #define NDIGO_ADC_MODE_A12 28 // not available on all boards
        #define NDIGO_ADC_MODE_B12 29 // not available on all boards
        #define NDIGO_ADC_MODE_C12 30 // not available on all boards
        #define NDIGO_ADC_MODE_D12 31 // not available on all boards

:cpp:`double bandwidth`
    Set to the minimum bandwidth required for the application.
    Lower bandwidth results in reduced noise. The driver will set the ADC
    to the minimum setting that has at least the desired bandwidth and report
    the selected bandwidth in the :cpp:`ndigo_param_info` structure.
    Versions -8, -10 and -12 currently support 1 |nbws| GHz and 3 |nbws| GHz
    bandwidth, version -8AQ supports 2 |nbws| GHz, 1.5 |nbws| GHz,
    600 |nbws| MHz and 500 |nbws| MHz.

:cpp:`ndigo_bool_t reserved`
    Reserved for internal use, do not change.

:cpp:`ndigo_bool_t tdc_enabled`
    Enable capturing of TDC measurements on external digital input channel.

:cpp:`ndigo_bool_t tdc_fb_enabled`
    Enable enhanced TDC resolution. Currently not implemented.

:cpp:`double analog_offset[NDIGO_CHANNEL_COUNT]`
    Sets the input DC offset-values to :math:`\pm` this value in V.
    Defaults to :cpp:`0`.

:cpp:`double dc_offset[2]`
    Sets the DC offset in volts for the TDC trigger input (index :cpp:`1`) and
    the GATE input (index :cpp:`0`). The trigger threshold is zero. For
    **negative 0.8** |nbws| **V NIM** pulses, this value should be set to
    :cpp:`0.4`.

:cpp:`ndigo_trigger trigger[NDIGO_TRIGGER_COUNT + NDIGO_ADD_TRIGGER_COUNT]`
    Configuration of the external trigger sources. Threshold is ignored for
    entries **8 and above**.

    The trigger indexes refer to the entry in the trigger array and are
    defined like this:

    .. code:: c++

        #define NDIGO_TRIGGER_A0 0
        #define NDIGO_TRIGGER_A1 1
        #define NDIGO_TRIGGER_B0 2
        #define NDIGO_TRIGGER_B1 3
        #define NDIGO_TRIGGER_C0 4
        #define NDIGO_TRIGGER_C1 5
        #define NDIGO_TRIGGER_D0 6
        #define NDIGO_TRIGGER_1 7
        #define NDIGO_TRIGGER_TDC 8
        #define NDIGO_TRIGGER_GATE 9
        #define NDIGO_TRIGGER_BUS0 10
        #define NDIGO_TRIGGER_BUS1 11
        #define NDIGO_TRIGGER_BUS2 12
        #define NDIGO_TRIGGER_BUS3 13
        #define NDIGO_TRIGGER_UTO 14
        #define NDIGO_TRIGGER_ONE 15

    Always positive edge-sensitive sources:

    .. code:: c++

        #define NDIGO_TRIGGER_TDC PE 16
        #define NDIGO_TRIGGER_GATE PE 17
        #define NDIGO_TRIGGER_BUS0 PE 18
        #define NDIGO_TRIGGER_BUS1 PE 19
        #define NDIGO_TRIGGER_BUS2 PE 20
        #define NDIGO_TRIGGER_BUS3 PE 21

:cpp:`ndigo_trigger_block trigger_block[NDIGO_CHANNEL_COUNT + 1]`
    A structure describing the trigger settings of the four channels plus
    the timestamp channel. In some modes not all channels are used.

:cpp:`ndigo_gating_block gating_block[4]`
    A structure describing the gating blocks that can be used by the trigger
    blocks to filter triggers.

:cpp:`ndigo_extension_block extension_block[NDIGO EXTENSION_COUNT]`
    A structure describing the routing of the 4 digital channels
    of the **Ndigo extension board** to the trigger matrix.

:cpp:`int drive_bus[4]`
    Enable output drive for each of the four external sync lines.
    Each integer represents a bitmask selecting the trigger sources for that line.
    The bit mapping is described in
    :numref:`Section %s<struct ndigotriggerblock>`

.. raw:: latex

    \begingroup
    \bfseries

:cpp:`int auto_trigger_period` 

.. raw:: latex

    \endgroup

:cpp:`int auto_trigger_random_exponent`
    Create a trigger either periodically or randomly.
    With :math:`M` = :cpp:`auto_trigger_period` and
    :math:`N` = :cpp:`auto_trigger_random_exponent`, the number of clock cycles
    :math:`T` between triggers will be

    .. math::

        T = 1 + M + [1...2^N]

    where :math:`0 \leq M < 2^{32}` and :math:`0 \leq N < 32`.

    There is no enable or reset as the usage of this trigger can be configured
    in the trigger block channel source field.


:cpp:`int output_mode`

    Defines the data representation in the output. :cpp:`Signed16` scales and
    :cpp:`CUTSOM_INL` corrects the input. :cpp:`RAW` directly presents the
    ADC values.

    .. code:: c++

        #define NDIGO_OUTPUT_MODE_SIGNED16 0
        #define NDIGO_OUTPUT_MODE_RAW 1
        #define NDIGO_OUTPUT_MODE_CUSTOM 2
        #define NDIGO_OUTPUT_MODE_CUSTOM_INL 3


:cpp:`lut_func custom_lut`
    Look-up table. If the output_mode is set to :cpp:`NDIGO_OUTPUT_MODE_CUSTOM`
    or to :cpp:`NDIGO_OUTPUT_MODE_CUSTOM_INL`, this function is used for
    mapping from ADC value to output value. The driver will call this function
    with a value from :math:`-1` to :math:`+1` and the function must return the
    corresponding signed 16-bit value that the board should return for an
    input voltage relative to the full scale range.

:cpp:`typedef short (*lut_func)(int channel, float x)`
    This can be used, e.g., for custom INL, offset and gain correction that
    covers user front end electronics. It can also invert the signal or
    correct the effect of logarithmic input amplifiers etc.

    The look-up table is applied on the board, thus using it does not cause
    any additional CPU load.  In the mode
    :cpp:`NDIGO_OUTPUT_MODE_CUSTOM_INL` the on-board INL correction table is
    applied before the user function, while :cpp:`NDIGO_OUTPUT_MODE_CUSTOM`
    does not perform INL correction. In order to use the user LUT 
    functionality, :cpp:`lut_func` must be set to a pointer to the
    LUT-function



Structure :cpp:`ndigo_trigger`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:cpp:`short threshold`
    Sets the threshold for the trigger block within the range of the ADC data
    of :math:`-32768` and :math:`+32768`.

    For trigger indices :cpp:`NDIGO_TRIGGER_TDC` to 
    :cpp:`NDIGO_TRIGGER_BUS3_PE`, the threshold is ignored.

:cpp:`ndigo_bool_t edge`
    If set, this trigger implements edge trigger functionality. Else, this is a
    level trigger.

    For trigger indices :cpp:`NDIGO_TRIGGER_AUTO` and :cpp:`NDIGO_TRIGGER_ONE`,
    this is ignored.

    For trigger indices :cpp:`NDIGO_TRIGGER_TDC_PE` to
    :cpp:`NDIGO_TRIGGER_BUS3_PE`, this must be set.

:cpp:`ndigo_bool_t rising`
    If set, trigger on rising edges or when above threshold.

    For trigger indices :cpp:`NDIGO_TRIGGER_AUTO` and :cpp:`NDIGO_TRIGGER_ONE`
    this is ignored.

    For trigger indices :cpp:`NDIGO_TRIGGER_TDC_PE` to
    :cpp:`NDIGO_TRIGGER_BUS3_PE` this must be set.


.. _struct ndigotriggerblock:

Structure :cpp:`ndigo_trigger_block`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:cpp:`ndigo_bool_t enabled`
    Activate triggers on this channel.

:cpp:`ndigo_bool_t retrigger`
    If a new trigger condition occurs while the postcursor is acquired, the
    packet is extended by starting a new postcursor. Otherwise the new trigger
    is ignored and the packet ends after the precursor of the first trigger.

    The retrigger setting is ignored for the timestamp channel.

:cpp:`ndigo_bool_t reserved1`
    Defaults to :cpp:`false`. Do not change.

:cpp:`ndigo_bool_t reserved2`
    Defaults to :cpp:`false`. Do not change.

:cpp:`int precursor`
    Precursor in multiples of 3.2ns. The amount of data preceding a trigger
    that is captured.  The precursor setting is ignored for the timestamp
    channel.

:cpp:`int length`
    In multiples of 3.2 |nbws| ns.

    The total amount of data that is recorded in addition to the trigger
    window. Precursor determines how many of these are ahead of the trigger
    and how many are appended after the trigger. In **edge trigger mode**
    the trigger window always is **3.2** |nbws| **ns** wide. In
    **level trigger mode** it is as long as the trigger condition is fulfilled.

    The length setting is ignored for the timestamp channel.

:cpp:`int sources`
    A bit mask with a bit set for all trigger sources that can trigger this
    channel.

    .. code:: c++

        #define NDIGO_TRIGGER_SOURCE_A0 0x00000001
        #define NDIGO_TRIGGER_SOURCE_A1 0x00000002
        #define NDIGO_TRIGGER_SOURCE_B0 0x00000004
        #define NDIGO_TRIGGER_SOURCE_B1 0x00000008
        #define NDIGO_TRIGGER_SOURCE_C0 0x00000010
        #define NDIGO_TRIGGER_SOURCE_C1 0x00000020
        #define NDIGO_TRIGGER_SOURCE_D0 0x00000040
        #define NDIGO_TRIGGER_SOURCE_D1 0x00000080
        #define NDIGO_TRIGGER_SOURCE_TDC 0x00000100
        #define NDIGO_TRIGGER_SOURCE_GATE 0x00000200
        #define NDIGO_TRIGGER_SOURCE_BUS0 0x00000400
        #define NDIGO_TRIGGER_SOURCE_BUS1 0x00000800
        #define NDIGO_TRIGGER_SOURCE_BUS2 0x00001000
        #define NDIGO_TRIGGER_SOURCE_BUS3 0x00002000
        #define NDIGO_TRIGGER_SOURCE_AUTO 0x00004000
        #define NDIGO_TRIGGER_SOURCE_ONE 0x00008000
        #define NDIGO_TRIGGER_SOURCE_TDC PE 0x01000000
        #define NDIGO_TRIGGER_SOURCE_GATE PE 0x02000000
        #define NDIGO_TRIGGER_SOURCE_BUS0 PE 0x04000000
        #define NDIGO_TRIGGER_SOURCE_BUS1 PE 0x08000000
        #define NDIGO_TRIGGER_SOURCE_BUS2 PE 0x10000000
        #define NDIGO_TRIGGER_SOURCE_BUS3 PE 0x20000000

:cpp:`int gates`
    .. code:: c++

        #define_NDIGO_TRIGGER_GATE_NONE 0x0000
        #define_NDIGO_TRIGGER_GATE_0 0x0001
        #define_NDIGO_TRIGGER_GATE_1 0x0002
        #define_NDIGO_TRIGGER_GATE_2 0x0004
        #define_NDIGO_TRIGGER_GATE_3 0x0008

:cpp:`double minimum_free_packets`
    This parameter sets how many packets are supposed to t into the on-board
    FIFO before a new packet is recorded after the FIFO was full, i.e., a
    certain amount of free space in the FIFO is demanded before a new packet
    is written after the FIFO was full.

    As a measure for the packet length the gate length set by the user is used.
    The on-board algorithm checks the free FIFO space only in case the FIFO is
    full.  Therefore, if this number is :cpp:`1.0` or more, at least every second
    packet in the DMA buffer is guaranteed to have the full length set by the
    gate length parameters. In many cases smaller values will also result in
    full length packets. But below a certain value multiple packets that are
    cut off at the end will show up.

.. _struct ndigoextblock:

Structure :cpp:`ndigo_extension_block`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This structure configures how the inputs from the optional extension board
and signals from the synchronization bus are merged.

:cpp:`ndigo_bool_t enable`
    Enable routing of digital signal from Ndigo extension board to the
    according BUSx trigger unit.


:cpp:`ndigo_bool_t ignore_cable`
    If :cpp:`false` input signal and BUS signal are *OR*ed before routing to
    the according BUSx trigger unit. Otherwise only the signal from
    **Ndigo extension board** is used.



Run Time Control
~~~~~~~~~~~~~~~~

.. raw:: latex

    \begingroup
    \bfseries

:cpp:`int ndigo_start_capture(ndigo_device *device)`

:cpp:`int ndigo_pause_capture(ndigo_device *device)`

.. raw:: latex

    \endgroup

:cpp:`int ndigo_continue_capture(ndigo_device *device)`
    Call this to resume data acquisition after a call to
    :cpp:`ndigo_pause_capture`.

.. raw:: latex

    \begingroup
    \bfseries

:cpp:`int ndigo_stop_capture(ndigo_device *device)`

.. raw:: latex

    \endgroup


Readout
-------

:cpp:`int ndigo_read(ndigo_device *device, ndigo_read in *in, ndigo_read_out *out)`
    Return a pointer to an array of captured data in :cpp:`read_out`. The
    result can contain any number of packets of type
    :cpp:`ndigo_packet`. :cpp:`read_in` provides parameters to the driver.
    A call to this method automatically allows the driver to reuse the
    memory returned in the previous call.

    Returns an error code as defined in the structure :cpp:`ndigo_read_out`.


:cpp:`int ndigo_acknowledge(ndigo_device *device, ndigo_packet *packet)`
    Acknowledge all data up to the packet provided as parameter. This is
    mandatory if :cpp:`acknowledge_last_read` in the :cpp:`ndigo_read_in`
    structure is set to :cpp:`false` for calls to :cpp:`ndigo_read`.

    This feature allows to either free up partial DMA space early if there
    will be no call to :cpp:`ndigo_read` anytime soon. It also allows to keep
    data over multiple calls to :cpp:`ndigo_read` to avoid unnecessary copying
    of data.

:cpp:`int ndigo_process_tdc_packet(ndigo_device *device, ndigo_packet *packet)`
    Call on a TDC packet to update the timestamp of the packet with a more
    accurate value.  If called more than once on a packet the timestamp will
    be invalid.


Input Structure :cpp:`ndigo_read_in`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:cpp:`ndigo_bool_t acknowledge_last_read`
    If set :cpp:`ndigo_read` automatically acknowledges packets from the last
    read.


Output Structure :cpp:`ndigo_read_out`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:cpp:`ndigo_packet *first_packet`
    Pointer to the first packet that was capture by the call of ndigo_read.

:cpp:`ndigo_packet *last_packet`
    Address of header of the last packet in the buffer.

:cpp:`int error_code`
    .. code:: c++

        #define NDIGO_READ_OK 0
        #define NDIGO_READ_NO_DATA 1
        #define NDIGO_READ_INTERNAL_ERROR 2

.. raw:: latex

    \begingroup
    \bfseries

:cpp:`const char *error_message`

.. raw:: latex

    \endgroup



Other Functions
---------------

LED control
~~~~~~~~~~~

There are six LEDs on the front panel. The intensity of the red and green part
can be set from :cpp:`0` to :cpp:`255`. There is no blue component in the current
version. Per default all LEDs are set to auto mode. This means that used
channels are lit **green**, activity is shown as **yellow** on overflow is
shown as **red**.

:cpp:`int ndigo_set_led_color(ndigo device *device, int led, unsigned short r, unsigned short g, unsigned short b)`
    Set the LED to the selected color. No automatic updates are performed.


:cpp:`int ndigo set led automode(ndigo device *device, int led)`
    Let the selected LED be controlled by hardware.








.. raw:: latex

    % RaggedRight ends here
    \endgroup



.. |nbws| unicode:: 0xA0
    :trim:

.. |hyphen| unicode:: U+2012

.. |endash| unicode:: U+2013

.. |emdash| unicode:: U+2014

.. |bdq| unicode:: U+201C
    :rtrim:

.. |edq| unicode:: U+201D
    :ltrim:

.. |br| raw:: latex

    \linebreak
