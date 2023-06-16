Packet Format
=============

Output Structure ndigopacket
----------------------------

**unsigned char channel**

**0** to **3** for the ADC input channels, **4** for the TDC, **5** for the timestamp channel.

**unsigned char card**

Identifies the source card in case there are multiple boards present.
Defaults to **0** if no value is assigned to the parameter boardid in Structure
ndigoinitparameters or set via
 **int ndigosetboardid(ndigodevice \*device, int boardid).**

**unsigned char type**

For the ADC channels this is set to **1** to signify **16 bit signed** data.

For the TDC channel it is set to **8** to signify **64 bit unsigned** data.

If the type field is 128 or greater then there is no data present, even
if length is not **0**. In this cases the length field may contain other
data.


.. container:: small

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

**unsigned char flags**

 #define NDIGO_PACKET_FLAG_SHORTENED 1

If the bit with **weight 1** is set, the packet was truncated because the internal
FIFO was full. Less than the requested number of samples have
been written due to the full FIFO.

 #define NDIGO_PACKET_FLAG_PACKETS LOST 2
If the bit with **weight 2** is set, there are lost triggers immediatel
preceding this packet due to insufficient DMA buffers. The DMA
controller has discarded packets due to full host buffer.

 #define NDIGO_PACKET_FLAG_OVERFLOW 4
If the bit with **weight 4** is set, the packet contains ADC sample overflows.

 #define NDIGO_PACKET_FLAG_TRIGGER MISSED 8
If the bit with **weight 8** is set, there are lost triggers immediately
preceding this packet due to insufficient buffers. The trigger unit
has discarded packets due to full FIFO.

 #define NDIGO_PACKET_FLAG_DMA FIFO FULL 16
If the bit with **weight 16** is set, the internal DMA FIFO was full.
Triggers only got lost if a subsequent package has the bit with **weight
8** set.

 #define NDIGO_PACKET_FLAG_HOST_BUFFER_FULL 32
If the bit with **weight 32** is set, the host buffer was full. Triggers
only got lost if a subsequent package has the bit with **weight 8** set.

 #define NDIGO_PACKET_FLAG_TDC_NO_EDGE 64
If the bit with **weight 64** is set, the packet from the TDC does not
contain valid data and the timestamp is not corrected. No valid edge
was found in TDC packet.

**unsigned int length**

Number of **64-bit** elements (each containing 4 samples) in the data
array if type :math:`< 128`.

If **type = 128** this is the pattern of trigger sources that where active
in the clock cycle given by the timestamp. Bits are set according to the
trigger sources, i.e. **bit 0** is set if **trigger A0** was active, **bit 29** is
set if **trigger BUS3 PE** was active. Use the **NDIGO_TRIGGER_SOURCE_*** to
check for the bits set.

**unsigned __int64 timestamp**

ADC channels **A** to **D**: Timestamp of the last word in the packet in ps.

TDC: Timestamp of the trigger event (falling edge) on the TDC channel in
ps. When **ndigo_process_tdc_packet()** is called once on the packet the
timestamp is replaced with the precise timestamp for the edge.

Timestamp channel: Timestamp of the trigger event in ps.

**unsigned __int64 data[]**

Sample data. For the **Ndigo5G** each **64 bit** word contains four **16 bit**
signed words from the ADC. The user can cast the array to short\* to
directly operate on the sample data.
