Driver Programming API
======================

The API is a DLL with C linkage. The functions provided by the DLL are
declared in **Ndigointerface.h.**

Constants
---------

**#define NDIGO_CHANNEL_COUNT 4**

The number of analog input channels.

**#define NDIGO_GATE_COUNT 4**

The number of gating blocks.

**#define NDIGO_TRIGGER_COUNT 16**

The number of triggers. Two per analog input, one per digital input
plus some specials.

**#define NDIGO_ADD_TRIGGER_COUNT 6**

Additional set of triggers for digital inputs.

Initialization
--------------

**int ndigo_count_devices (int**  * **error_code, char** ** **error message)**

Return the number of boards that are supported by this driver in the system.

**int ndigo_get_default_init_parameters(ndigo_init_parameters** * **init)**

Get a set of default parameters to feed into **ndigoinit().**

This must always be used to initialize the **ndigo_init_parameter** structure.

**ndigo_device**  * **ndigo_init(ndigo_init_parameters** * **params, int** * **error_code, char** ** **error_message)**

Open and initialize the Ndigo board with the given index. With **error_code** and **error_message**
the user must provide pointers where to buffers where error information should be written by the driver. The
buffer for the error message must by at least **80 chars** long.

Params is a structure of type **ndigo_init_parameters** that must be
completely initialized.

**int ndigo_close(ndigo_device**  * **device)**

Finalize the driver for this device.


Structure ndigo_init_parameters
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**int version**

Must be set to **NDIGO_API_VERSION**

**int card_index**

The index in the list of **Ndigo5G** boards that should be initialized.
There might be multiple boards in the system that are handled by this
driver as reported by **ndigo_count_devices**. This index selects one of
them. Boards are enumerated depending on the PCIe slot. The lower the
bus number and the lower the slot number the lower the card index.

int board_id
This 8 bit number is filled into each packet created by the board and
is useful if data streams of multiple boards will be merged. If only
**Ndigo5G** cards are used this number can be set to the card index. If
boards of different types that use a compatible data format are used
in a system each board should get a unique id.

Can be changed with int ndigosetboardid(ndigodevice*device, int boardid).

**ndigo_bool_t use_external_clock**

Use 10MHz clock supplied by IPC flat band cable. Must be set for all slaves.

**ndigo_bool_t drive_external_clock**

Drive internal 10MHz clock of this board to IPC flat band cable. Must be set for master.

**ndigo_bool_t is_slave**

Data acquisition of this board is controlled by the master board.

**int sync_period**

Period of the multicard sync pulse. Should be set to **4** (default) when
using several Ndigo boards in sync. Ignored for single board setups.
The **Ndigo5G** has 4 phases relative to the global 10MHz clock.

**int sync_delay**

Fine tap delay for incoming sync signals.

**ndigo_bool_t force_window_calibration**

If **true/1**, valid data window is detected at initialization. Default value is **false/0:**
values from flash memory are used in order to set data window to correct position.

**ndigo_bool_t hptdc_sync_enabled**

A **HPTDC** is connected to this board. Enables the clock and sync line
from the **Ndigo5G** to the **HPTDC**.

**__int64 buffer_size[8]**

The minimum size of the DMA buffer. If set to 0 the default size of
16MByte is used. **Ndigo5G** only uses **buffer_size[0]**.

**int buffer_type**

Must be set to **NDIGO_BUFFER_ALLOCATE**.

**__int64 buffer_address**

Ignored. Might be used for future buffer types.

**int variant**

Set to 0. Can be used to activate future device variants such as
different base frequencies.

**int device_type**

Initialized by ndigo_get_default_init_parameters(). Must be left unchanged.

    #define CRONO_DEVICE_HPTDC 0

    #define CRONO_DEVICE_NDIGO5G 1

    #define CRONO_DEVICE_NDIGO250M 2


**int_dma read_delay**

Initialized by **ndigo_get_default_init_parameters()**. The write pointer
update is delay by this number of **4 ns** clock periods to hide race
conditions between software and DMA.


Status Information
------------------

Functions for Information Retrieval
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


The driver provides functions to retrieve detailed information on the
type of board, its configuration, settings and state. The information is
split according to its scope and the computational requirements to query
the information from the board.

**int ndigo_get_driver_revision()**

Returns the driver version, same format as ndigo_static_info::driver_revision.
This function does not require a present **Ndigo5G** device.

**const char* ndigo_get_driver_revision_str()**

Returns the driver version including SVN build revision as a string.
This function does not require a present **Ndigo5G** device.

**int ndigo_get_static_info(ndigo_device *device, ndigo_static_info *info)**

This structure contains information about the board that does not
change during run time.

**int ndigo_get_param_info(ndigo device *device, ndigo_param_info *info)**

The structure returned by this call contains information that changes
indirectly due to configuration changes.

**int ndigo_get_fast_info(ndigo device *device, ndigo_fast_info *info)**

This call returns a structure that contains dynamic information that
can be obtained within a few microseconds.

**int ndigo_get_slow_info(ndigo device *device, ndigo_slow_info *info)**

The data reported in this structure requires milliseconds to be
obtained. The application should only call it in situation where the
program flow can cope with an interruption of that magnitude.

**const char* ndigo_get_last_error_message(ndigo_device *device)**

Structure ndigo_static_info
---------------------------

This structure contains information about the board that does not change
during run time. It is provided by the function  **ndigo_get_static_info**.

**int size**

The number of bytes occupied by the structure

**int version**

A version number that is increased when the definition of the
structure is changed. The increment can be larger than one to match
driver version numbers or similar. Set to **0** for all versions up to
first release.

**int board_id**

Index of the board as passed to the constructor or set via int
ndigosetboardid(ndigodevice *device, int boardid).

**int driver_revision**

The lower three bytes contain a triple level hierarchy of version
numbers, e.g. **0x010103** encodes **version 1.1.3.**

A change in the first digit generally requires a recompilation of user
applications. Change in the second digit denote significant improvements
or changes that don’t break compatibility and the third digit changes
with minor bugfixes and similar updates.

**int firmware_revision**

Firmware revision of the FPGA configuration. This increments only when
there is a functional change.

**int board_revision**

**0** for experimental prototypes labeled **Rev. 1**

**2** for the version produced until 2010 labeled **Rev. 2**

**3** for the version produced starting in 2011 labeled **Rev. 3**

**int board_configuration**

Describes the schematic configuration of the board.

For **board revision 0** this always reads **0**.

For **board revision 2** the following assignments are valid:

If **Bit 3 = 0** this following is valid:

**Bit 0** determines the ADC resolution. (**0 = 8 - bit or 1 = 10 - bit**).

**Bit 1** determines whether the TDC-oscillator is present
  (**0** = oscillator present, **1** = simple trigger).
**Bit 2** determines the input connectors (**0** = single ended, **1** = differential).

**Bit 3 = 1** signifies a special version of the board

**0xA** is **Ndigo1250M-12** single ended with digital trigger

**0x8** is **Ndigo5G-8** single ended with digital trigger

**For Board revision 3 the following assignments are valid:**

**Bit 2** determines the input connectors (**0** = single ended, **1** = differential).

The other bits have one of the following patterns [Bits 3...0]

    **0010** Ndigo5G-10 2.5u 10

    **0011** Ndigo5G-8-AQ 2.5u 8

    **0110** Ndigo5G-10-Diff 560pF 10 DIFF

    **1000** Ndigo5G-8 560pF 8+

    **1010** Ndigo1250M-12 2.2uF 12 Sciex DC

    **1011** Ndigo5G-10 560pF 10

    **1110** Ndigo5G-Sciex 2.2uF 10 Sciex Infiniband, DIFF

    **1111** Ndigo5G-Roent = fADC4/10 560pF 10


**int adc_resolution**

Number of bits of the ADC, set to **0** if unknown.

**double nominal_sample_rate**

Sample rate in once channel mode. Usually **5.0e9 = 5Gsps**.

**double analog_bandwidth**

**3e9** for **3Ghz**.

**int chip_id**

16 bit factory ID of the ADC chip

**int board_serial**
Serial number with the year minus 2000 in the highest 8 bits of the
integer and a running number in the lower 24 bits. This number is
identical with the one on the label on the board.

**int flash_serial_low**

**int flash_serial_high**

64 bit manufacturer serial number of the flash chip.

**int flash_valid**

If not 0 the driver found valid calibration data in the flash on the
board and is using it.

**ndigo bool_t_dc_coupled**

Returns false for the standard AC coupled **Ndigo5G**.


**int subversion_revision**

A number to track builds of the firmware in more detail than the
firmware revision. It changes with every change in the firmware, even
if there is no visible effect for the user.

**char calibration_date[20]**

DIN EN ISO 8601 string YYYY-MM-DD HH:DD describing the time when the
card was calibrated.


Structure ndigo_param_info
~~~~~~~~~~~~~~~~~~~~~~~~~~

**int size**

The number of bytes occupied by the structure.

**int version**

A version number that is increased when the definition of the
structure is changed. The increment can be larger than one to match
driver version numbers or similar. Set to **0** for all versions up to
first release.

**double bandwidth**

Analog Bandwidth setting of the ADC. Either **3e9 = 3GHz or 1e9 = 1GHz** for 10 bit version

**double sample_rate**

Sample rate. This **is 1.25e9, 2.5e9** or **5.0e9** depending on the current
ADC mode.
sample_rate · channels = **5.0e9**.

**double sample_period**

The period one sample in the data represents in picoseconds

**int board_id**

The number the board uses to identify the data source in the output
data stream.

**int channels**

Number of channels. 1, 2 or 4 depending on the ADC mode chosen.
                **sample_rate · channels = 5.0e9.**

**int channel_mask**

Mask with a set bit for each enabled input channel.

**int64 total_buffer**

The total amount of the DMA buffer in bytes.

Structure ndigo fast info
~~~~~~~~~~~~~~~~~~~~~~~~~

**int size**

The number of bytes occupied by the structure

**int version**

A version number that is increased when the definition of the structure is changed.
The increment can be larger than one to match driver version numbers or similar.
Set to **0** for all versions up to first release.

**int adc_rpm**

Speed of the ADC fan. Reports **0** if no fan is present.

**int fpga_rpm**

Speed of the FPGA fan. Reports **0** if no fan is present.

**int alerts**

Alert bits from the system monitor.

**Bit 0 :** FPGA temperature alert (**> 85°C**)

**Bit 1 :** Internal FPGA voltage out of range (**< 1:01V or > 1:08V** )

**Bit 2 :** FPGA auxiliary voltage out of range. (**< 2,375V or > 2,625V** )

**Bit 3 :** FPGA temperature critical (**> 125°C**)

**Bit 4 :** ADC temperature alert (**> 90°C**)

**Bit 5 :** ADC temperature critical (**> 100°C**): will automatically be turned off.

**double voltage_aux**

Auxiliary FPGA voltage, nominal 2.5V

**double voltage_int**

Internal FPGA voltage, nominal 1.0V

**double fpga_temperature**

In °C measured on die.

**int pcie_link_width**

Number of PCIe lanes that the card uses. Should be 4 for **Ndigo5G**.

**int pcie_max_payload**

Maximum size in bytes for one PCIe transaction, depends on system configuration.


Structure ndigo slow info
~~~~~~~~~~~~~~~~~~~~~~~~~

**int size**

The number of bytes occupied by the structure.

**int version**

A version number that is increased when the definition of the structure is changed.
The increment can be larger than one to match driver version numbers or similar.
Set to **0** for all versions up to first release.

**double adc_temperature**

ADC temperature in °C measured on die.

**double board_temperature**

In °C


Configuration
-------------

The device is congfiured with a configuration structure. The user should first obtain a structure
that contains the default settings of the device read from an on board ROM, than modify the
structure as needed for the user application and use the result to configure the device.

**int ndigo_get_default_configuration(ndigo_device *device, ndigo_configuration *config)**

**int ndigo_get_current_configuration(ndigo_device *device, ndigo_configuration *config)**

**int ndigo configure(ndigo_device *device, ndigo_configuration *config)**

**int ndigo_set_board_id(ndigo_device *device, int board_id)**

The **board_id** can be changed after initialization of the card. If cronotools are
used, the **board_id** changes have to be done before cronotools initialization.



Structure ndigo configuration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This is the structure containing the configuration information. It is used in conjunction with
**ndigo_get_default_configuration, ndigo_get_current_configuration** and **ndigo_configure**.

It uses internally the structures **ndigo_trigger_block** and **ndigo_trigger**.

**int size**

The number of bytes occupied by the structure.

**int version**

A version number that is increased when the definition of the structure is changed.
The increment can be larger than one to match driver version numbers or similar.
Set to **0** for all versions up to first release.

**int reserved1**

Reserved for internal usage. Do not change.

**int adc mode**

Constant describing the ADC mode

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

**double bandwidth**

Set to the minimum bandwidth required for the application.
Lower bandwidth results in reduced noise. The driver will set the ADC to the minimum
setting that has at least the desired bandwidth and report the selected bandwidth in the
**ndigo_param_info** structure. The -8, -10 and -12 versions currently supports **1GHz** and
**3GHz** bandwidth, the -8AQ version supports **2GHz, 1.5GHz, 600MHz** and **500 MHz**.

**ndigo_bool_t reserved**

**ndigo_bool_t tdc_enabled**

Enable capturing of TDC measurements on external digital input channel.

**ndigo_bool_t tdc_fb_enabled**

Enable enhanced TDC resolution. Currently not implemented.

**double analog offset[NDIGO CHANNEL COUNT]**

Sets the input DC offset-values to **+- this value in volts**. Defaults to **0**.

**double dc offset[2]**

Sets the DC offset in volts for the TDC trigger input (index 1) and the GATE input (index 0).
The trigger threshold is zero. For **negative 0.8V NIM** pulses a value of **0.4** should be set here.

**ndigo trigger trigger[NDIGO TRIGGER COUNT + NDIGO ADD TRIGGER COUNT]**

Configuration of the external trigger sources. Threshold is ignored for entries **8 and above**.


The trigger indexes refer to the entry in the trigger array and are defined like this:

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



    #define NDIGO_TRIGGER_TDC PE 16

    #define NDIGO_TRIGGER_GATE PE 17

    #define NDIGO_TRIGGER_BUS0 PE 18

    #define NDIGO_TRIGGER_BUS1 PE 19

    #define NDIGO_TRIGGER_BUS2 PE 20

    #define NDIGO_TRIGGER_BUS3 PE 21



**ndigo_trigger_block trigger_block[NDIGO_CHANNEL_COUNT + 1]**

A structure describing the trigger settings of the four channels plus
the timestamp channel. In some modes not all channels are used.

**ndigo_gating_block gating_block[4]**

A structure describing the gating blocks that can be used by the trigger blocks to filter triggers.

**ndigo_extension_block extension_block[NDIGO EXTENSION_COUNT]**

A structure describing the routing of the 4 digital channels
of the **Ndigo extension board** to the trigger matrix.

**int drive_bus[4]**

Enable output drive for each of the four external sync lines.
Each integer represents a bitmask selecting the trigger sources for that line.
The bit mapping is described in section`Structure_ndigo_trigger_block`_ on page 22.

**int auto_trigger_period**

**int auto_trigger_random_exponent**

Create a trigger either periodically or randomly. There are two parameters
**M =** trigger_period and **N =** random_exponent that result in a distance between triggers of


.. math::
        T = 1 + M + [1...2^N]


clock cycles.


:math:`0 \leq M < 2^{32}`


:math:`0 \leq N < 32`


There is no enable or reset as the usage of this trigger can be configured in the trigger block
channel source field.


**int output_mode**

Defines the data representation in the output. **Signed16** scales and INL-corrects the input.
**RAW** directly presents the ADC values.

    #define NDIGO_OUTPUT_MODE_SIGNED16 0

    #define NDIGO_OUTPUT_MODE_RAW 1

    #define NDIGO_OUTPUT_MODE_CUSTOM 2

    #define NDIGO_OUTPUT_MODE_CUSTOM_INL 3


**lut_func custom _lut**

Lookup table. If the output_mode is set to **NDIGO_OUTPUT_MODE_CUSTOM** or
to **NDIGO_OUTPUT_MODE_CUSTOM_INL**, this function is used for mapping
from ADC value to output value. The driver will call this function with a value
from **-1** to **+1** and the function must return the corresponding signed 16 bit value
that the board should return for an input voltage relative to the full scale range.

**typedef short (*lut func)(int channel, float x)**

This can be used e.g. for custom INL, offset and gain correction that covers user front end
electronics. It can also invert the signal or correct the effect of logarithmic input amplifiers etc.

The LUT is applied on the board, thus using it does not cause any additional CPU load.
In the mode **NDIGO_OUTPUT_MODE_CUSTOM_INL** the on-board INL correction table is
applied before the user function, while **NDIGO_OUTPUT_MODE_CUSTOM** does not perform
INL correction. In order to use the user lookup table functionality, **lut_func** must be set to a
pointer to the LUT-function


Structure ndigo trigger
~~~~~~~~~~~~~~~~~~~~~~~


**short threshold**

Sets the threshold for the trigger block within the range of the ADC data of -32768 and +32768.

For trigger indices **NDIGO_TRIGGER_TDC** to **NDIGO_TRIGGER_BUS3_PE** the threshold is ignored.

**ndigo_bool_t edge**

If set this trigger implements edge trigger functionality else this is a level trigger.

For trigger indices **NDIGO_TRIGGER_AUTO** and **NDIGO_TRIGGER_ONE** this is ignored.

For trigger indices **NDIGO_TRIGGER_TDC_PE** to **NDIGO_TRIGGER_BUS3_PE** this must be set.

**ndigo_bool_t rising**

If set trigger on rising edges or when above threshold.

For trigger indices **NDIGO_TRIGGER_AUTO** and **NDIGO_TRIGGER_ONE** this is ignored.

For trigger indices **NDIGO_TRIGGER_TDC_PE** to **NDIGO_TRIGGER_BUS3_PE** this must be set.


**ndigo_bool_t rising**

If set trigger on rising edges or when above threshold.

For trigger indices **NDIGO_TRIGGER_AUTO** and **NDIGO_TRIGGER_ONE** this is ignored.

For trigger indices **NDIGO_TRIGGER_TDC_PE** to **NDIGO_TRIGGER_BUS3_PE** this must be set.


.. _Structure_ndigo_trigger_block:
Structure_ndigo_trigger_block
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


**ndigo_bool_t enabled**

Activate triggers on this channel.

**ndigo_bool_t retrigger**

If a new trigger condition occurs while the postcursor is acquired, the packet is extended by
starting a new postcursor. Otherwise the new trigger is ignored and the packet ends after the
precursor of the first trigger.

The retrigger setting is ignored for the timestamp channel.

**ndigo_bool_t reserved1**

Defaults to false. Do not change.

**ndigo_bool_t reserved2**

Defaults to false. Do not change.

**int precursor**

Precursor in multiples of 3.2ns. The amount of data preceding a trigger that is captured.
The precursor setting is ignored for the timestamp channel.

**int length**

In multiples of 3.2ns.

The total amount of data that is recorded in addition to the trigger window. Precursor
determines how many of these are ahead of the trigger and how many are appended
after the trigger. In **edge trigger mode** the trigger window always is **3.2ns** wide, in
**level trigger mode** it is as long as the trigger condition is fulfilled.

The length setting is ignored for the timestamp channel.



**int sources**

A bit mask with a bit set for all trigger sources that can trigger this channel.

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


**int gates**


    #define_NDIGO_TRIGGER_GATE_NONE 0x0000

    #define_NDIGO_TRIGGER_GATE_0 0x0001

    #define_NDIGO_TRIGGER_GATE_1 0x0002

    #define_NDIGO_TRIGGER_GATE_2 0x0004

    #define_NDIGO_TRIGGER_GATE_3 0x0008


**double minimum_free_packets;**

This parameter sets how many packets are supposed to t into the on-board FIFO
before a new packet is recorded after the FIFO was full, i.e. a certain amount of free
space in the FIFO is demanded before a new packet is written after the FIFO was full.

As a measure for the packet length the gate length set by the user is used.
The on-board algorithm checks the free FIFO space only in case the FIFO is full.
Therefore, if this number is **1.0** or more, at least every second packet in the DMA
buffer is guaranteed to have the full length set by the gate length parameters.
In many cases smaller values will also result in full length packets. But below
a certain value multiple packets that are cut off at the end will show up.


Structure ndigo gating block
~~~~~~~~~~~~~~~~~~~~~~~~~~~~


**ndigo_bool_t negate**

Invert output polarity. Defaults to false.

**ndigo_bool_t retrigger**

Defaults to false. If retriggering is enabled, the timer is reset to the value of the start parameter
whenever the input signal is set while waiting to reach the stop time.

**ndigo_bool_t extend**

Defaults to true. If set, a gate is created with the set timing from the first occurrence of the
input trigger even for short gates. If not set, the input signal must persist for the gate to be
created. This feature is **NOT YET IMPLEMENTED.**


**ndigo_bool_t reserved1**

Defaults to false. Do not change.

**int start**

In multiples of **3.2ns**. The time from the first input signal seen in the idle state until the gating
output is set. The value of start needs to be less or equal to the stop value. Maximum value for
start and stop is :math:`2^{16}-1`.

**int stop**

In multiples of **3.2ns**. Maximum allowed value is :math:`2^{16}-1`.


The time from leaving the idle state until the gating output is reset. If retriggering is enabled,
the timer is reset to the value of the start parameter whenever the input signal is set while
waiting to reach the stop time.


**int sources**


A bit mask with a bit set for all trigger sources that can trigger this channel. The gates cannot
use the additional digital trigger sources **NDIGO_TRIGGER_SOURCE_TDC_PE** to
**NDIGO_TRIGGER_SOURCE_BUS3_PE**.


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



Structure ndigo extension block
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


This structure configures how the inputs from the optional extension board and signals from
the synchronization bus are merged.


**ndigo_bool_t enable**

Enable routing of digital signal from Ndigo extension board to the according **BUSx** trigger unit.


**ndigo_bool_t ignore_cable**

If **false** input signal and BUS signal are **OR** ed before routing to the according

**BUSx** trigger unit. Otherwise only the signal from **Ndigo extension board** is used.



Run Time Control
~~~~~~~~~~~~~~~~


**int ndigo_start_capture(ndigo_device *device)**

**int ndigo_pause_capture(ndigo_device *device)**

**int ndigo_continue_capture(ndigo_device *device)**

Call this to resume data acquisition after a call to ndigo_pause_capture.

**int ndigo_stop_capture(ndigo_device *device)**

.. _Section 3.6:

Readout
-------


**int ndigo_read(ndigo_device *device, ndigo_read in *in, ndigo_read_out *out)**

Return a pointer to an array of captured data in **read_out**. The result can contain any number
of packets of type **ndigo_packet. read_in** provides parameters to the driver. A call to this
method automatically allows the driver to reuse the memory returned in the previous call.


Returns an error code as defined in the structure **ndigo_read_out**.


**int ndigo_acknowledge(ndigo_device *device, ndigo_packet *packet)**


Acknowledge all data up to the packet provided as parameter. This is mandatory if
**acknowledge_last_read** in the **ndigo_read_in** structure is set to **false** for calls to **ndigo_read**.


This feature allows to either free up partial DMA space early if there will be no call to
**ndigo_read** anytime soon. It also allows to keep data over multiple calls to **ndigo_read** to avoid
unnecessary copying of data.

**int ndigo_process_tdc_packet(ndigo_device *device, ndigo_packet *packet)**

Call on a TDC packet to update the timestamp of the packet with a more accurate value.
If called more than once on a packet the timestamp will be invalid.


Input Structure ndigo read in
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


**ndigo_bool_t acknowledge_last_read**

If set **ndigo_read** automatically acknowledges packets from the last read.


Input Structure ndigo read out
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


**ndigo_packet *first_packet**

Pointer to the first packet that was capture by the call of ndigo_read.

**ndigo_packet *last_packet**

Address of header of the last packet in the buffer.

**int error_code**

#define NDIGO_READ_OK 0

#define NDIGO_READ_NO_DATA 1

#define NDIGO_READ_INTERNAL_ERROR 2


**const char *error_message**


Other Functions
---------------

LED control
~~~~~~~~~~~


There are six LEDs on the front panel. The intensity of the red and green part can be set from
**0** to **255**. There is no blue component in the current version. Per default all LEDs are set to
**auto mode**. This means that used channels are lit **green**, activity is shown as **yellow** on
overflow is shown as **red**.


**int ndigo_set_led_color(ndigo device *device, int led, unsigned short r, unsigned short g,
unsigned short b)**


Set the LED to the selected color. No automatic updates are performed.


**int ndigo set led automode(ndigo device *device, int led)**

Let the selected LED be controlled by hardware.

