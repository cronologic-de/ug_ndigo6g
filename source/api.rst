Driver Programming API
======================

.. raw:: latex

    \begingroup
    %\RaggedRight

The API is a DLL with C linkage. The functions provided by the DLL are declared
in :code:`ndigo6g12_interface.h`.



Constants
---------

:cpp:`#define NDIGO6G12_CHANNEL_COUNT 4`
    The number of analog input channels.

:cpp:`#define NDIGO6G12_GATE_COUNT 4`
    The number of gating blocks.

:cpp:`#define NDIGO6G12_TRIGGER_COUNT 16`
    The number of triggers. Two per analog input, one per digital input plus
    some specials. :red:`TODO check`

:cpp:`#define NDIGO6G12_ADD_TRIGGER_COUNT 6`
    Additional set of triggers for digital inputs.


Initialization
--------------

:cpp:`int ndigo6g12_count_devices(int *error_code, const char **error message)`
    Return the number of boards that are supported by this driver in the system. 

:cpp:`int ndigo6g12_get_default_init_parameters(ndigo6g12_init_parameters  *init)`
    Get a set of default parameters to feed into :cpp:`ndigo6g12_init()`.
    This must always be used to initialize the :cpp:`ndigo6g12_init_parameter` structure.

:cpp:`ndigo6g12_device *ndigo6g12_init(ndigo6g12_init_parameters *params, int *error_code, char **error_message)`
    Open and initialize the Ndigo6G12 board with the given index.
    With :cpp:`error_code` and :cpp:`error_message`
    the user must provide pointers where to buffers where error information
    should be written by the driver.
    The buffer for the error message must by at least **80 chars** long. 
    :cpp:`params` is a structure of type
    :cpp:`ndigo6g12_init_parameters` that must be completely initialized. 

:cpp:`int ndigo6g12_close(ndigo6g12_device *device)`
    Finalize the driver for this device. 




Structure :code:`ndigo6g12_init_parameters`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:cpp:`int version`
    Must be set to :cpp:`NDIGO6G12_API_VERSION`

:cpp:`int card_index`
    The index in the list of **Ndigo6G** boards that should be initialized. 
    There might be multiple boards in the system that are handled by this
    driver as reported by :cpp:`ndigo6g12_count_devices()`. This index selects
    one of them.  Boards are enumerated depending on the PCIe slot. The lower
    the bus number and the lower the slot number, the lower the card index. 

:cpp:`int board_id`
    This 8-bit number is filled into each packet created by the board and is
    useful if data streams of multiple boards will be merged. If only
    **Ndigo6G12** cards are used this number can be set to the card index. If
    boards of different types that use a compatible data format are used in a
    system each board should get a unique id.

:cpp:`int64_t buffer_size[8]`
    The minimum size of the DMA buffer. If set to :cpp:`0`, the default size of
    64 |nbws| MiBytes is used. For the Ndigo6G12, only the first entry is used.

:cpp:`int dma_read_delay`
    The update delay of the writing pointer after a packet has been send over
    PCIe. Default value is :cpp:`8192`. Do not change.

:cpp:`int perf_derating`
    Default :cpp:`0`: 1.6/3.2/6.4 |nbws| Gsps. Do not change.

:cpp:`int led_flashing_mode`
    Controls the LED flashing mode.
    - :cpp:`0`: off
    - :cpp:`1`: light all colors once
    - :cpp:`2`: 
    - :cpp:`3`: 

:cpp:`int adc_channel_mask`
    Mask with a bit set for each enabled ADC channel. By default, all channels
    are enabled. Do not change.

:cpp:`crono_bool_t no_reference_clock`
    Default is :cpp:`false`. Do not change.

:cpp:`crono_bool_t use_external_clock`
    Use **10** |nbws| **MHz** clock as a reference. Input is either the
    internal SMA or external LEMO connector depending on 
    :cpp:`use_aux2_clock`. Default is :cpp:`false`.

:cpp:`crono_bool_t use_aux2_clock`
    If enabled, use slot bracket LEMO as external reference clock input.
    Otherwise, the internal SMA connector is used. Has no effect if 
    :cpp:`use_external_clock` is :cpp:`false`. Default is :cpp:`false`.

:cpp:`crono_bool_t ignore_lane_errors`
    Default is :cpp:`false`. Do not change.

:cpp:`crono_bool_t ignore_clock_erros`
    Default is :cpp:`false`. Do not change.

:cpp:`crono_bool_t adc_full_swing`
    Default is :cpp:`false`. Do not change.

:cpp:`int application_type`
    Select four, two, or one channel, or averaging mode.
    - :cpp:`0` use currently isntalled type
    - :cpp:`1` one ADC channel at 6.4 Gsps
    - :cpp:`2` two ADC channels at 3.2 Gsps
    - :cpp:`4` four ADC channels at 1.6 Gsps
    - :cpp:`5` averaging mode

:cpp:`crono_bool_t force_bitstream_update`
    Update partial bitstream even if the application type matches.

:cpp:`int partial_bitstream_size`
    Size of the partial bitstream.

:cpp:`uint32_t *partial_bitstream`
    Pointer to the buffer with the partial bitstream data.
    Can be :cpp:`nullptr` if :cpp:`application_type` matches 
    :cpp:`application_type` of the currently installed firmware.

:cpp:`const char *firmware_locations`
    Pointer to a list of paths (separated by :cpp:`;`).
    Can be :cpp:`nullptr` if :cpp:`application_type` matches 
    :cpp:`application_type` of the currently installed firmware.



Status Information
------------------

Functions for Information Retrieval
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The driver provides functions to retrieve detailed information on the type
of board, its configuration, settings and state. The information is split
according to its scope and the computational requirements to query the
information from the board. 

:cpp:`int ndigo6g12_get_driver_revision()`
    Returns the driver version, same format as
    :cpp:`ndigo_static_info::driver_revision`.

:cpp:`const char* ndigo_get_driver_revision_str()`
    Returns the driver version including SVN build revision as a string. 
    with format x.y.z.svn

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


Structure :cpp:`ndigo6g12_static_info`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This structure contains information about the board that does not change
during run time. It is provided by the function 
:cpp:`ndigo_get_static_info()`.

:cpp:`int size`
    The number of bytes occupied by the structure.

:cpp:`int version`
    A version number that is increased when the definition of the structure is
    changed. The increment can be larger than one to match driver version
    numbers or similar. Set to :cpp:`0` for all versions up to first release.  

:cpp:`int board_id`
    Index of the board as passed to the constructor or set via

    :cpp:`int ndigosetboardid(ndigodevice *device, int boardid)`.

:cpp:`char bitstream_date[NDIGO6G_BITSTREAM_DATE_LEN]`
    Bitstream creation date
    
    DIN EN ISO 8601 string YYYY-MM-DD HH:DD:SS describing the time when the
    bitstream was created.

:cpp:`int board_revision`
    Board revision number.
    
    The board revision number can be read from a register. It is a four
    bit number that changes when the schematic of the board is changed.
    - :cpp:`0`: Experimental first board Version. Labeled "Rev. 1"
    - :cpp:`2`: First commercial Version. Labeled "Rev. 2"

:cpp:`int board_serial`
    Serial number
    
    With year and running number in 8.24 format. The number is identical
    to the one printed on the silvery sticker on the board.

:cpp:`char calibration_date[NDIGO6G_CALIBRATION_DATE_LEN]`
    Calibration date
    
    DIN EN ISO 8601 string YYYY-MM-DD HH:DD describing the time when the
    card was calibrated.
    
:cpp:`int chip_id`;
    16bit factory ID of the ADC chip.
    
    This is the chipID as read from the 16 bit ADC chip ID register.

:cpp:`crono_bool_t dc_coupled`
    Shows if the inputs are DC-coupled.
    Default is :cpp:`false`, i.e., AC-coupled.

:cpp:`int driver_build_revision`
    The build number of the driver according to cronologic's internal
    versioning system.

:cpp:`crono_bool_t flash_valid`
    Calibration data read from flash is valid.
    
    If not :cpp:`false`, the driver found valid calibration data in the flash
    on the board and is using it.

:cpp:`int fw_revision`
    Revision number of the FPGA configuration

:cpp:`int fw_type`
    Type of firmware, always :cpp:`5`, i.e., Ndigo6G-12.

:cpp:`int pcb_serial`
    Trenz serial number

    
:cpp:`int svn_revision`
    Subversion revision ID of the FPGA configuration.
    
    A number to track builds of the firmware in more detail than the
    firmware revision. It changes with every change in the firmware, even
    if there is no visible effect for the user. The subversion revision
    number can be read from a register.
    
:cpp:`int application_type`
    Shows the initialized mode
    :cpp:`0`: keep currently used application type
    :cpp:`1`: one ADC channel @6.4 Gsps
    :cpp:`2`: two ADC channels @3.2 Gsps
    :cpp:`4`: four ADC channels @1.6 Gsps
    :cpp:`5`: averaging mode
    See :cpp:`NDIGO6G_APP_TYPE_*` constants

:cpp:`char config_flash_signature_primary[NDIGO6G_FLASH_SIG_LEN]`
    Shows the signature of the primary flash

:cpp:`char config_flash_signature_secondary[NDIGO6G_FLASH_SIG_LEN]`
    Shows the signature of the secondary flash

     
    



Structure :cpp:`ndigo6g12_param_info`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:cpp:`int size`
    The number of bytes occupied by the structure.

:cpp:`int version`
    A version number that is increased when the definition of the
    structure is changed. The increment can be larger than one to match
    driver version numbers or similar. Set to :cpp:`0` for all versions up to
    first release.

:cpp:`double bandwidth`
    Bandwidth setting of the ADC. :cpp:`4.5` or :cpp:`6.5` (GHz) depending on
    the configuration.

:cpp:`double resolution`
    ADC sample resolution. Always :cpp:`12.0` (bit).

:cpp:`double sample_rate`
    Actual ADC sample rate of currently sampled data.
    Depends on ADC mode: *sample_rate = 6.4 / #channels*

:cpp:`double sample_period`
    The period one sample in the data represents in ps.

:cpp:`double tdc_period`
    The period one TDC bin in the data represents in ps.

:cpp:`double packet_ts_period`
    The period one tick of the packet timestamp represents in ps.

:cpp:`uint64_t tdc_packet_timestamp_offset`
    TDC packets carry the timestamp of the end of packet. To calculate the
    start, substract the offset.

:cpp:`uint32_t tdc_rollover_period`
    The time span in TDC bins of one TDC timestamp rolloever period.

:cpp:`adc_sample_delay`
    The ID the board uses to identify itself in the output data stream. Takes
    values :cpp:`0` to :cpp:`255`.

:cpp:`int board_id`
    The number the board uses to identify the data source in the output
    data stream.

:cpp:`int channels`
    Number of channels in the current mode.

:cpp:`int channel_mask`
    Mask with a set bit for each enabled input channel.

:cpp:`int tdc_channels`
    Number of TDC channels in the current mode.

:cpp:`int64_t total_buffer`
    The total amount of the DMA buffer in bytes.


Structure :cpp:`ndigo6g12_fast_info`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:cpp:`int size`
    The number of bytes occupied by the structure.

:cpp:`int version`
    A version number that is increased when the definition of the structure is
    changed.  The increment can be larger than one to match driver version
    numbers or similar. Set to :cpp:`0` for all versions up to first release.

:cpp:`int state`
    The current state of the device.
    Should be one of the values :cpp:`NDIGO6G12_DEVICE_STATE_*`

:cpp:`int fan_speed`
    Speed of the FPGA fan in rounds per minute.
    Reports :cpp:`0`, if no fan is present.

:cpp:`double fpga_temperature`
    Temperature of the FPGA in °C.

:cpp:`double fpga_vccint`
    Internal Voltage of the FPGA :red:`in V? TODO`.

:cpp:`double fpga_vccaux`
    Auxillary Voltage of the FPGA

:cpp:`double fpga_vccbram`
    BRAM Voltage of the FPGA :red:`in V? TODO`.

:cpp:`double mgt_0v9`
    Shows measured Voltage for the mgt_0v9 supply :red:`in V? TODO`.

:cpp:`double mgt_1v2`
    Shows measured Voltage for the mgt_1v2 supply :red:`in V? TODO`.

:cpp:`double adc_2v5`
    Shows measured Voltage for the 2v5 supply :red:`in V? TODO`.

:cpp:`double clk_3v3`
    Shows measured Voltage for the clk_3v3 supply :red:`in V? TODO`.

:cpp:`double adc_3v3`
    Shows measured Voltage for the adc_3v3 supply :red:`in V? TODO`.

:cpp:`double pcie_3v3`
    Shows measured Voltage for the pcie_3v3 supply :red:`in V? TODO`.

:cpp:`double opamp_5v2`
    Shows measured Voltage for the opamp_5v2 supply :red:`in V? TODO`.

:cpp:`double temp4633_1`
    Shows temperature of temp4633_1 in °C

:cpp:`double temp4633_2`
    Shows temperature of temp4633_2 in °C

:cpp:`double temp4644`
    Shows temperature of temp4644 in °C

:cpp:`double tdc1_temp`
    Temperature of the TDC in °C.

:cpp:`double ev12_cmiref`
    Shows voltage for ev12_cmiref supply. Measured or calibration target
    depending on board revision and assembly variant.

:cpp:`double ev12_temp`
    Temperature of the ADC in °C.

:cpp:`int alerts`
    Alert bits from temperature sensor and the system monitor.
    
    Bit 0 is set if the TDC temperature exceeds 140 °C. In this case the
    TDC did shut down and the device needs to be reinitialized.

:cpp:`int pcie_link_width`
    Number of PCIe lanes the card uses.
    Should always be :cpp:`8` for the Ndigo6G12.

:cpp:`int pcie_link_speed`
    Data rate of the PCIe card.
    Should always be x :red:`TODO` for the Ndigo6G12.

:cpp:`int pcie_max_payload`
    Maximum size for a single PCIe transaction in bytes. Depends on
    system configuration.

:cpp:`crono_bool_t adc_data_pll_locked`
    ADC data clock is PLL locked

:cpp:`crono_bool_t adc_data_pll_lost_lock`
    ADC data clock PLL lost lock (Sticky Bit)

:cpp:`int adc_lanes_synced;`
    Shows the synced ADC lanes
    each bit corresponds to one lane

:cpp:`int adc_lanes_lost_sync`
    Shows the ADC lanes that lost sync
    each bit corresponds to one lane

:cpp:`int adc_lanes_fifo_empty`
    Shows which ADC lanes have an empty FIFO
    each bit corresponds to one lane

:cpp:`int adc_lanes_fifo_full`
    Shows which ADC lanes have a full FIFO
    each bit corresponds to one lane

:cpp:`int adc_lanes_running`
    Shows which ADC lanes are running
    each bit corresponds to one lane

:cpp:`int adc_lanes_sync_timeout`
    Shows which ADC lanes were unable to sync before a timeout
    each bit corresponds to one lane

:cpp:`int adc_sync_retry_count`
    The number of ADC lane synchronization retries
    Default is set to :cpp:`0`

:cpp:`int adc_sync_strobe_retry_count`
    The number of ADC strobe synchronization retries
    Default is set to :cpp:`0`

:cpp:`int adc_sync_delay_count`
    16 Bit number showing when the last ADC lane synchronization was achieved
   
:cpp:`crono_bool_t adc_mgt_power_good`
    Shows if the supplied mgt power is sufficient

:cpp:`crono_bool_t lmk_pll1_locked`
    Shows if lmk_pll1 is locked

:cpp:`crono_bool_t lmk_pll2_locked`
    Shows if lmk_pll2 is locked

:cpp:`crono_bool_t lmk_lost_lock`
    Shows if lmk lost lock

:cpp:`int lmk_lock_wait_count`
    Wait count of the lmk

:cpp:`int lmk_ctrl_vcxo`
    :red:`TODO`

:cpp:`crono_bool_t lmx_locked`
    lmx locked

:cpp:`crono_bool_t lmx_lost_lock`
    lmx lost lock

:cpp:`int lmx_lock_wait_count`
    :red:`TODO`

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


:cpp:`int ndigo_set_led_automode(ndigo device *device, int led)`
    Let the selected LED be controlled by hardware.

.. raw:: latex

    % RaggedRight ends here
    \endgroup



