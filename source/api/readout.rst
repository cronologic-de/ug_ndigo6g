:tocdepth: 3

Readout
-------

After an Ndigo6G-12 board is initialized and capturing, the captured events
can be read from the board with :cpp:func:`ndigo6g12_read`. The read-out
data is packaged in *packets* (see :doc:`../packform/index`).


.. latex-toc-doxygenfunction:: ndigo6g12_read

.. latex-toc-doxygenfunction:: ndigo6g12_get_last_error_message

.. latex-toc-doxygenfunction:: ndigo6g12_device_state_to_str

.. latex-toc-doxygenfunction:: ndigo6g12_acknowledge

.. latex-toc-doxygenstruct:: ndigo6g12_read_in

.. latex-toc-doxygenstruct:: ndigo6g12_read_out
