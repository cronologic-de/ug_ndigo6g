.. role:: cpp(code)
    :language: c++

Packet Format
=============

.. _struct ndigopacket:

Output Structure :cpp:`ndigo_packet`
------------------------------------

:cpp:`unsigned char channel`
   :cpp:`0` to :cpp:`3` for the ADC input channels, :cpp:`4` for the TDC,
   :cpp:`5` for the timestamp channel.

:cpp:`unsigned char card`
   Identifies the source card in case there are multiple boards present.
   Defaults to :cpp:`0` if no value is assigned to the parameter boardid in
   Structure ndigoinitparameters or set via
   :cpp:`int ndigosetboardid(ndigodevice \*device, int boardid)`.

:cpp:`unsigned char type`
   For the ADC channels this is set to :cpp:`1` to signify 16-bit signed data.

   For the TDC channel it is set to :cpp:`8` to signify 64-bit unsigned data.

   If the type field is 128 or greater then there is no data present, even
   if length is not :cpp:`0`. In this cases the length field may contain other
   data.

   .. raw:: latex

      \begingroup
      \RaggedRight

   +------+------------------------------+------------------------------+
   | Type | Length Field                 | Description                  |
   +======+==============================+==============================+
   | 1    | Number of payload words      | 16 bit signed samples from   |
   |      |                              | one of the ADCs              |
   +------+------------------------------+------------------------------+
   | 8    | Number of payload words      | 64 Bit unsigned TDC Data,    |
   |      |                              | only for internal processing |
   +------+------------------------------+------------------------------+
   | 128  | Bit pattern of trigger       | Whenever at least one of the |
   |      | sources                      | sources that is enabled for  |
   |      |                              | the timestamp channel        |
   |      |                              | triggers, one of these       |
   |      |                              | packets is generated. The    |
   |      |                              | length field contains the    |
   |      |                              | triggers active when this    |
   |      |                              | packet was created.          |
   +------+------------------------------+------------------------------+

   .. raw:: latex

      \endgroup

:cpp:`unsigned char flags`
   .. code:: c++

      #define NDIGO_PACKET_FLAG_SHORTENED 1

   If the bit with **weight 1** is set, the packet was truncated because the
   internal FIFO was full. Less than the requested number of samples have
   been written due to the full FIFO.

   .. code:: c++

      #define NDIGO_PACKET_FLAG_PACKETS_LOST 2

   If the bit with **weight 2** is set, there are lost triggers immediatel
   preceding this packet due to insufficient DMA buffers. The DMA
   controller has discarded packets due to full host buffer.

   .. code:: c++

      #define NDIGO_PACKET_FLAG_OVERFLOW 4

   If the bit with **weight 4** is set, the packet contains ADC sample
   overflows.

   .. code:: c++

      #define NDIGO_PACKET_FLAG_TRIGGER_MISSED 8

   If the bit with **weight 8** is set, there are lost triggers immediately
   preceding this packet due to insufficient buffers. The trigger unit
   has discarded packets due to full FIFO.

   .. code:: c++

      #define NDIGO_PACKET_FLAG_DMA_FIFO_FULL 16

   If the bit with **weight 16** is set, the internal DMA FIFO was full.
   Triggers only got lost if a subsequent package has the bit with **weight
   8** set.

   .. code:: c++

      #define NDIGO_PACKET_FLAG_HOST_BUFFER_FULL 32

   If the bit with **weight 32** is set, the host buffer was full. Triggers
   only got lost if a subsequent package has the bit with **weight 8** set.

   .. code:: c++

      #define NDIGO_PACKET_FLAG_TDC_NO_EDGE 64

   If the bit with **weight 64** is set, the packet from the TDC does not
   contain valid data and the timestamp is not corrected. No valid edge
   was found in TDC packet.

:cpp:`unsigned int length`
   Number of **64-bit** elements (each containing four samples) in the data
   array if :cpp:`type` :math:`<` :cpp:`128`.

   If :cpp:`type == 128` this is the pattern of trigger sources that where
   active in the clock cycle given by the timestamp. Bits are set according to
   the trigger sources, i.e., **bit 0** is set if **trigger A0** was active,
   **bit 29** is set if **trigger BUS3 PE** was active. Use the
   :cpp:`NDIGO_TRIGGER_SOURCE_*`-defines to check for the bits set.

:cpp:`unsigned __int64 timestamp`
   ADC channels **A** to **D**: Timestamp of the last word in the packet in ps.

   TDC: Timestamp of the trigger event (falling edge) on the TDC channel in
   ps. When :cpp:`ndigo_process_tdc_packet()` is called once on the packet, the
   timestamp is replaced with the precise timestamp for the edge.

   Timestamp channel: Timestamp of the trigger event in ps.

:cpp:`unsigned __int64 data[]`
   Sample data. For the **Ndigo5G** each **64-bit** word contains four
   **16-bit** signed words from the ADC. The user can cast the array to
   :cpp:`short` to directly operate on the sample data.
