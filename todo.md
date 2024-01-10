# TODO

 - NDIGO6G12_MAX_MULTISHOT define missing
 - NDIGO6G12_MAX_PRECURSOR define missing
 - what are the return values of ndigo6g12_get_default_init_parameters
   (defdefinpar)
 - what are the return values of ndigo6g12_get_last_error_message
   (defclose)
    * error codes as defined in crono_interface.h
 - what are the return values of ndigo6g12_start/stop_capture
   (defstartcap/defstopcap)
    * error codes as defined in crono_interface.h
 - what is crono_pcie_info?
    * define in crono_interface.h
 - Figure out how to use automatic documentaion for doxygen groups.
   Right now, they are ugly, since the automatic output includes the doxygen
   group name, which is not nice.
 - What does "Trigger signal active each clock cycle" mean?
    * it is basically the opposite of TRIGGER_NONE
 - What is the default for ndigo6g12_gating_block?
 - Update comments of adcdefs, so different modes don't have the same
   description.