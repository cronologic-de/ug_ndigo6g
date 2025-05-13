.. _avrg data format:

Data encoding for averaged ADC hits
-----------------------------------

When using :c:macro:`NDIGO6G12_APP_TYPE_AVRG`, the first two 64-bit words of
:cpp:member:`crono_packet::data` are the extended header
containing more information, as shown in the following bit table.

.. only:: html

    +-------------+----------+-----------------------------------------+----------+----------------------+
    | **Bits**    | 127 – 38 | 37 – 32                                 | 31 – 12  | 11 – 0               |
    +-------------+----------+-----------------------------------------+----------+----------------------+
    | **Data**    | reserved | flags                                   | reserved | iterations performed |
    +-------------+----------+-----------------------------------------+----------+----------------------+
    | **Details** |          | ``0x01``: stopped iterations prematurely|          |                      |
    |             |          | ``0x02``: overflow detected             |          |                      |
    |             |          | ``0x04``: stopped by timeout            |          |                      |
    |             |          | ``0x08``: stopped by software           |          |                      |
    |             |          | ``0x10``: stopped by overflow           |          |                      |
    +-------------+----------+-----------------------------------------+----------+----------------------+


.. raw:: latex

    \begingroup
    \renewcommand\tabularxcolumn[1]{>{\Centering}p{#1}}
    \begin{tabularx}{\textwidth}{|l||X|X|X|X|}
        \hline
        Bits & 127 $-$ 38 & 27 $-$ 32 & 31 $-$ 12 & 11 $-$ 0 \\
        \hline
        Data & reserved & flags & reserved & iterations performed \\
        \hline
    \end{tabularx}

    Flags:
    \begin{itemize}
        \item \texttt{0x01}: stopped iterations prematurely
        \item \texttt{0x02}: overflow detected
        \item \texttt{0x04}: stopped by timeout
        \item \texttt{0x08}: stopped by software
        \item \texttt{0x10}: stopped by overflow
    \end{itemize}

The following data words contain the raw ADC data mapped to the range of a signed32
integer (−2\ :sup:`31` to 2\ :sup:`31` −1). Thus, :cpp:member:`crono_packet::data`
must be cast to ``int32_t`` and :cpp:member:`crono_packet::length` must be multiplied
by 2 **taking into account the extended header**. That is,

.. code-block:: c

    uint32_t extended_header_length = 2;
    uint32_t sample_count = ((pkt->length - extended_header_length) * 2);
    int32_t* adc_data = (int32_t*)(pkt->data + offset);