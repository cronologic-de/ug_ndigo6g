:hide-toc:

C++-Example
===========

The following source code is an example of an Ndigo6G-12 application written
in C++. The source code is also available on our
`GitHub <https://github.com/cronologic-de/ndigo6g_babel/tree/main/ug_example>`_.

=============================================== =======
Source file                                     Description
=============================================== =======
:doc:`ndigo6g12_example.cpp<example>`           Main source-code file of the
                                                example application.
:doc:`ndigo6g12_app.h<app>`                     Header file for classes for
                                                different Ndigo6G-12
                                                :cpp:member:`application types<ndigo6g12_init_parameters::application_type>`
                                                and TDC setup.
:doc:`ndigo6g12_adc_single.cpp<adc_single>`     Implementation of application
                                                type :c:macro:`NDIGO6G12_APP_TYPE_1CH`.
:doc:`ndigo6g12_adc_dual.cpp<adc_dual>`         Implementation of application
                                                type :c:macro:`NDIGO6G12_APP_TYPE_2CH`.
:doc:`ndigo6g12_adc_quad.cpp<adc_quad>`         Implementation of application
                                                type :c:macro:`NDIGO6G12_APP_TYPE_4CH`.
:doc:`ndigo6g12_adc_averager.cpp<adc_averager>` Implementation of application
                                                type :c:macro:`NDIGO6G12_APP_TYPE_AVRG`.
:doc:`ndigo6g12_tdc.cpp<tdc>`                   Implementation of the TDC-class.
:doc:`delay.h<delay>`                           Implementation for measuring
                                                delays.
=============================================== =======

.. toctree::
    :maxdepth: 2
    :hidden:

    example
    app
    adc_single
    adc_dual
    adc_quad
    adc_averager
    tdc
    delay

