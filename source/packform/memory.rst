Memory management
=================

The host buffer is memory on the host’s system in which the data recorded by the
Ndigo6G-12 is stored until it is acknowledged by the user.

The host buffer is managed by the DMA (direct memory access) driver.
The DMA driver can only ever write to the host buffer if enough memory is free.
That means, new packets will never overwrite old packets, unless they have been
acknowledged.

If the host buffer is full, data may be lost.
Then, the :c:macro:`CRONO_PACKET_FLAG_HOST_BUFFER_FULL` bit of
:cpp:member:`crono_packet::flags` is set.
To ensure that this does not happen, the user must acknowledge packets
fast enough by the analysis software.
Note that data only has been lost due to a full host buffer if the
:c:macro:`CRONO_PACKET_FLAG_TRIGGER_MISSED` bit of :cpp:member:`crono_packet::flags`
is set.

Acknowledge Packets
-------------------
A packet in the host buffer will only be overwritten if it has been acknowledged.
This can be done manually by the user by calling
:cpp:func:`ndigo6g12_acknowledge` or automatically by the driver if in the call of
:cpp:func:`ndigo6g12_read`, :cpp:member:`in.ackwnoledge_last_read<ndigo6g12_read_in::acknowledge_last_read>` of
was set to true.

Acknowledging a packet acknowledges all previous packets as well.

Be aware that acknowledging a packet immediately invalidates it, and it is unsafe to
attempt accessing its content.

Internal Memory Layout
----------------------
The Ndigo6G-12 uses internal FIFO (first-in, first-out) memories.
In one of these FIFOs, referred to as the DMA
FIFO, packets that are ready to be sent to the host system are buffered.
If the DMA FIFO is full at any point, the affected packets
:c:macro:`CRONO_PACKET_FLAG_DMA_FIFO_FULL` bit of :cpp:member:`crono_packet::flags`
is set. This does not mean that data has been necessarily lost. Only if the
:c:macro:`CRONO_PACKET_FLAG_TRIGGER_MISSED` bit is set has data been lost.