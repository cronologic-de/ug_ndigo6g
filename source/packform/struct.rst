Output Structure *crono_packet*
-------------------------------
.. .. doxygenstruct:: crono_packet
..    :members:

.. cpp:struct:: crono_packet

    .. cpp:member:: uint8_t channel

        Source channel of the data.

        Values correspond to the following:

        | ``0x0`` – ``0x3``: ADC A – D
        | ≥ ``0x4``: TDC channels. Which specific TDC channel is encoded in
          :cpp:member:`crono_packet::data`.

    .. cpp:member:: uint8_t card

        ID of the card.

    .. cpp:member:: uint8_t type

        Type of the packet.

        Different packet types correspond to different encodings of
        :cpp:member:`crono_packet::data`.

        Is one of the following:

        .. c:macro:: CRONO_PACKET_TYPE_16_BIT_SIGNED

            Used for :ref:`ADC data <adc data format>`.

            :cpp:member:`crono_packet::data` must be cast to ``int16_t`` and
            :cpp:member:`crono_packet::length` must be multiplied by 4.

        .. c:macro::  CRONO_PACKET_TYPE_TDC_DATA

            Used for :ref:`TDC data <tdcpacket bit table>`.

            :cpp:member:`crono_packet::data` must be cast to ``uint32_t`` and
            :cpp:member:`crono_packet::length` must be multiplied by 2.

        .. c:macro:: CRONO_PACKET_TYPE_AVRG_DATA

            Used for :ref:`averaged ADC data <avrg data format>`.

            :cpp:member:`crono_packet::data` must be cast to ``uint32_t`` and
            :cpp:member:`crono_packet::length` must be multiplied by 2.


    .. cpp:member:: uint8_t flags

        Bit field of the following flags:

        .. doxygengroup:: packetflags
            :content-only:

        For TDC data, can also be one of the following:

        .. doxygengroup:: tdcpacketflags
            :content-only:

    .. cpp:member:: uint32_t length

        Length of :cpp:member:`crono_packet::data` in multiples of 64 bits. The actual
        length of :cpp:member:`crono_packet::data` depends on 
        :cpp:member:`crono_packet::type`.

    .. cpp:member:: uint64_t timestamp

        Timestamp of the packet.

        For the Ndigo6G-12, this corresponds to the beginning of the packet data.

    .. cpp:member:: uint64_t data[1]

        Payload data of the packet.

        The length of ``data`` corresponds to :cpp:member:`crono_packet::length`.

        The data type must be cast according to :cpp:member:`crono_packet::type`, and
        the data encoding also depends on :cpp:member:`crono_packet::type`.

        See :numref:`Section %s<adc data format>` for the data encoding of ADC data.

        See :numref:`Section %s<tdcpacket bit table>` for the data encoding of TDC data.

        See :numref:`Section %s<avrg data format>` for the data encoding of averaged
        ADC data.



