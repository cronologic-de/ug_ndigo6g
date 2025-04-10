===================
Calibrating the TDC
===================

You can backup or restore the calibration from a previous backup using
*FirmwareGUI_64.exe* (see  :doc:`firmware` and
:numref:`Figure %s<flash tool>`).

In the “Calibration” section, click “Backup” and choose a location for the
:code:`.ndigo6gcal` calibration file.

You can compare the currently used calibration with the calibration from a
backup file by clicking “Verify” button after browsing to your calibration file.

You can flash the calibration from a :code:`*.ndigo6gcal` file onto the Ndigo6G-12
by clicking “Flash” after browsing to your calibration file.

.. attention::

    After performing a :doc:`firmware update<firmware>`, it is always necessary to
    re-calibrate your Ndigo6G-12. Restoring a previous calibration from a backup
    is not sufficient.

Re-calibrating the Ndigo6G-12
-----------------------------

Calibration is performed with the command-line tool *ndigo6g12_tdc_alignment.exe*.
It is located in the installation directory of the Ndigo6G-12 driver under
:code:`apps\\x64`
(by default :code:`C:\\Program Files\\cronologic\\Ndigo6G-12\\apps\\x64`).

Navigate to the folder and open it in a terminal, then start the tool from that
terminal.

The tool takes command line arguments. Run :code:`.\\ndigo6g12_tdc_alignment.exe -help`
for an overview.

Calibration is performed by simply starting the tool:
:code:`.\\ndigo6g12_tdc_alignment.exe`.

If multiple Ndigo6G-12 are installed in your system, you can perform calibration for
each one of them by calling
:code:`.\\ndigo6g12_tdc_alignment.exe -index \<device_index\>`, where the
:code:`\<device_index\>` starts at 0 and increments for each Ndigo6G-12.


