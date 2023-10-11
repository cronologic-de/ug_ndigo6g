.. role:: cpp(code)
    :language: c++

Driver Programming API
======================

The API is a DLL with C linkage. The functions provided by the DLL are declared
in :code:`Ndigointerface.h`.




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
    8 bit number is filled into each packet created by the board and is useful if
    data streams of multiple boards will be merged. If only **Ndigo5G** cards are
    used this number can be set to the card index. If boards of different types that
    use a compatible data format are used in a system each board should get a
    unique id.  Can be changed with
    :cpp:`int ndigosetboardid(ndigodevice *device, int boardid)`. 

:cpp:`ndigo_bool_t use_external_clock`
    Use 10MHz clock supplied by IPC flat band cable. Must be set for all slaves. 

:cpp:`ndigo_bool_t drive_external_clock`
    Drive internal 10MHz clock of this board to IPC flat band cable.
    Must be set for master. 

:cpp:`ndigo_bool_t is_slave`
    Data acquisition of this board is controlled by the master board. 
    :cpp:`int sync_period` Period of the multicard sync pulse. Should be set to
    **4** (default) when using several Ndigo boards in sync. Ignored for single
    board setups.  The **Ndigo5G** has 4 phases relative to the global 10MHz clock. 

:cpp:`int sync_delay`
    Fine tap delay for incoming sync signals. 

:cpp:`ndigo_bool_t force_window_calibration`
    If :cpp:`true` / :cpp:`1`, valid data window is detected at initialization. Default
    value is :cpp:`false` / :cpp:`0`: values from flash memory are used in order to set
    data window to correct position.  :cpp:`ndigo_bool_t hptdc_sync_enabled` A
    **HPTDC** is connected to this board. Enables the clock and sync line from
    the **Ndigo5G** to the **HPTDC**. 

:cpp:`__int64 buffer_size[8]`
    The minimum size of the DMA buffer.
    If set to :cpp:`0` the default size of 16MByte is used. **Ndigo5G** only uses
    :cpp:`buffer_size[0]`.

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

    :cpp:`#define CRONO_DEVICE_HPTDC 0`
    :cpp:`#define CRONO_DEVICE_NDIGO5G 1`
    :cpp:`#define CRONO_DEVICE_NDIGO250M 2`

:cpp:`int_dma read_delay`
    Initialized by :cpp:`ndigo_get_default_init_parameters()`.
    The write pointer update is delay by this number of **4 ns** clock periods
    to hide race conditions between software and DMA. 