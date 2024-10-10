Readout
-------

After an Ndigo6G-12 board is initialized and capturing, the captured events
can be read from the board with :cpp:func:`ndigo6g12_read`. The read-out
data is packaged in *packets* (see :numref:`Chapter %s<packet format>`).


.. raw:: latex

    \phantomsection
    \addcontentsline{toc}{subsubsection}{\textit{ndigo6g12\_read}}

.. doxygenfunction:: ndigo6g12_read

.. raw:: latex

    \phantomsection
    \addcontentsline{toc}{subsubsection}{\textit{ndigo6g12\_get\_last\_error\_message}}

.. doxygenfunction:: ndigo6g12_get_last_error_message

.. raw:: latex

    \phantomsection
    \addcontentsline{toc}{subsubsection}{\textit{ndigo6g12\_device\_state\_to\_str}}

.. doxygenfunction:: ndigo6g12_device_state_to_str



.. raw:: latex

    \phantomsection
    \addcontentsline{toc}{subsubsection}{\textit{ndigo6g12\_read\_in}}

.. doxygenstruct:: ndigo6g12_read_in
    :members:

.. raw:: latex

    \phantomsection
    \addcontentsline{toc}{subsubsection}{\textit{ndigo6g12\_read\_out}}

.. doxygenstruct:: ndigo6g12_read_out
    :members: