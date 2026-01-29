WiFi Provision
======================

The device needs access to the Internet to sync clock and request for weather data.

When WiFi is not accessable at startup, the device will enter WiFi provision mode with screen showing below interface.


.. figure:: _static/wifi_prov.dev.png
   :class: dev

   Now the device acts as a WiFi hotspot "xDial-xxxx", last four digits being device ID.

Follow the instructions, connect to device's WiFi hotspot with your phone, then you shall see a WiFi provision page pop up (if not, you'll have to visit the IP address with your browser), in which you can type in the WiFi name and password in your home or office.

.. warning::
   The device doesn't support 5GHz WiFi, make sure 2.4GHz WiFi is enabled on your router. 

Then the device will reboot and WiFi configuration will be saved.

.. tip::
   It's recommended to bind the device's MAC address to a static IP address. Usually this can be done in the configurtion page of your WiFi router.

