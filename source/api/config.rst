:tocdepth: 3

Configuration
=============

The Ndigo6G-12 board is configured with a configuration structure
(:cpp:struct:`ndigo6g12_configuration`).

The user should first obtain a standard set of configuration parameters
using :cpp:func:`ndigo6g12_get_default_configuration`, then modify only the
necessary parameters to their specific needs.

The configuration itself is done by calling :cpp:func:`ndigo6g12_configure`.

.. latex-toc-doxygenfunction:: ndigo6g12_get_default_configuration

.. latex-toc-doxygenfunction:: ndigo6g12_configure


.. latex-toc-doxygenstruct:: ndigo6g12_configuration

.. latex-toc-doxygenstruct:: ndigo6g12_trigger

.. latex-toc-doxygenstruct:: ndigo6g12_trigger_block

.. latex-toc-doxygenstruct:: ndigo6g12_gating_block

.. latex-toc-doxygenstruct:: ndigo6g12_tdc_configuration

.. latex-toc-doxygenstruct:: ndigo6g12_averager_configuration

.. latex-toc-doxygenstruct:: ndigo6g12_tdc_channel

.. latex-toc-doxygenstruct:: ndigo6g12_tdc_gating_block

.. latex-toc-doxygenstruct:: ndigo6g12_tdc_tiger_block
