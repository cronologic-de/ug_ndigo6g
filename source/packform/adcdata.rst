.. _adc data format:

Data encoding for ADC hits
--------------------------

:cpp:member:`data<crono_packet::data>`, that is, the packet-data payload, 
depends on :cpp:member:`ndigo6g12_configuration::output_mode`. The length of 
the :cpp:member:`data<crono_packet::data>` array is encoded in :cpp:member:`length<crono_packet::length>`. Be 
aware that :cpp:member:`length<crono_packet::length>` is in multiples of 64 bit, while
the size of the fields of :cpp:member:`data<crono_packet::data>` depends on
:cpp:member:`type<crono_packet::type>`.

Thus, reading packet data requires the following steps:

- Depending on :cpp:member:`crono_packet::type`, multiply 
  :cpp:member:`length<crono_packet::length>` appropriately. E.g., if 
  :cpp:member:`type<crono_packet::type>` is 
  :c:macro:`CRONO_PACKET_TYPE_16_BIT_SIGNED`, 
  :cpp:member:`length<crono_packet::length>` has to be multiplied by 4 (since 4 
  :math:`\times` 16 bit = 64 bit).
- Cast :cpp:member:`data<crono_packet::data>` according to 
  :cpp:member:`type<crono_packet::type>`. E.g., if 
  :cpp:member:`type<crono_packet::type>` is 
  :c:macro:`CRONO_PACKET_TYPE_16_BIT_SIGNED`, cast
  :cpp:member:`data<crono_packet::data>` to ``int16_t``.


:c:macro:`NDIGO6G12_OUTPUT_MODE_SIGNED16`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Raw data of the ADC is mapped to the range of a signed16 integer (−32768 to 
32767). Packet data must be cast to ``int16_t``.


:c:macro:`NDIGO6G12_OUTPUT_MODE_RAW`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Packet data is returned in the native range of the ADC (0 to 4095).
It must be cast to ``int16_t``.

Data layout:

.. only:: html

    +-------------+----+----+----+---------+----+----+-----+---+
    | **Bit**     | 15 | 14 | 13 | 12      | 11 | 10 | ... | 0 |
    +-------------+----+----+----+---------+----+----+-----+---+
    | **Data**    | 0  | 0  | control bits | sample data       |
    +-------------+----+----+--------------+-------------------+

.. raw:: latex

    \begingroup
    \renewcommand\tabularxcolumn[1]{>{\Centering}p{#1}}
    \begin{tabularx}{\textwidth}{|l||X|X|X|X|X|X|c|X|}
        \hline
        Bit & 15 & 14 & 13 & 12 & 11 & 10 & \dots & 0 \\
        \hline
        Data & 0 & 0 & \multicolumn{2}{c|}{control bits} & \multicolumn{4}{c|}{sample data} \\
        \hline
    \end{tabularx}
    \endgroup


:c:macro:`NDIGO6G12_OUTPUT_MODE_RAW_NO_CB`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Packet data is returned in the native range of the ADC (0 to 4095).
It must be cast to ``int16_t``. Unlike
:c:macro:`NDIGO6G12_OUTPUT_MODE_RAW`, it does not contain control bits.

.. attention::

    :c:macro:`NDIGO6G12_OUTPUT_MODE_RAW` and :c:macro:`NDIGO6G12_OUTPUT_MODE_RAW_NO_CB`
    are useful for debugging purposes.
    They are not supported for user applications. Use
    :c:macro:`NDIGO6G12_OUTPUT_MODE_SIGNED16` instead.


:c:macro:`NDIGO6G12_OUTPUT_MODE_SIGNED32`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Only used if :cpp:member:`ndigo6g12_init_parameters::application_type` is
:c:macro:`NDIGO6G12_APP_TYPE_AVRG`. See :numref:`Section %s<avrg data format>` for more
information.
