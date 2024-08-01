.. _adc data format:

Data encoding for ADC hits
--------------------------

:cpp:member:`data<crono_packet::data>`, that is, the packet-data payload, 
depends on :cpp:member:`ndigo6g12_configuration::output_mode`. The length of 
the :cpp:member:`data<crono_packet::data>` array is encoded in :cpp:member:`length<crono_packet::length>`. Be 
aware that :cpp:member:`length<crono_packet::length>` is in multiples of 64 bit, while the size of the fields 
of :cpp:member:`data<crono_packet::data>` depends on :cpp:member:`type<crono_packet::type>`.

Thus, reading packet data requires the following steps:

- Depending on :cpp:member:`type<crono_packet::type>`, multiply 
  :cpp:member:`length<crono_packet::length>` appropriately. E.g., if 
  :cpp:member:`type<crono_packet::type>` is 
  :c:macro:`CRONO_PACKET_TYPE_16_BIT_SIGNED`, 
  :cpp:member:`length<crono_packet::length>` has to be multiplied by 4 (since 4 
  :math:`\times` 16 bit = 64 bit).
- Cast :cpp:member:`data<crono_packet::data>` according to 
  :cpp:member:`type<crono_packet::type>`. E.g., if 
  :cpp:member:`type<crono_packet::type>` is 
  :c:macro:`CRONO_PACKET_TYPE_16_BIT_SIGNED`, cast
  :cpp:member:`data<crono_packet::data>` to ``int32_t``.


:c:macro:`NDIGO6G12_OUTPUT_MODE_SIGNED16`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Raw data of the ADC is mapped to the range of a signed16 integer (−32768 to 
32767). Packet data is of type :c:macro:`CRONO_PACKET_TYPE_16_BIT_SIGNED`.

:c:macro:`NDIGO6G12_OUTPUT_MODE_SIGNED32`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Only used if :cpp:member:`ndigo6g12_init_parameters::application_type` is
:c:macro:`NDIGO6G12_APP_TYPE_AVRG`.

Raw data of the ADC is mapped to the range of a signed32 integer (−2\ :sup:`31` 
to 2\ :sup:`31` −1). Packet data is of type 
:c:macro:`CRONO_PACKET_TYPE_32_BIT_SIGNED`.


:c:macro:`NDIGO6G12_OUTPUT_MODE_RAW`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Packet data is returned in the native range of the ADC (0 to 4095) and as
type :c:macro:`CRONO_PACKET_TYPE_16_BIT_SIGNED`. The two most significant
bits are control bits and have to be masked if one wishes to use the data.

.. note::

    :c:macro:`NDIGO6G12_OUTPUT_MODE_RAW` is useful for debugging purposes.
    For typical applications, we do not recommend using this mode over
    :c:macro:`NDIGO6G12_OUTPUT_MODE_SIGNED16`.
