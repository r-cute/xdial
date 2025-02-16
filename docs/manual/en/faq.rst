FAQ
============

`update firmware <ota.html>`_ to latest version.

When pluged, nothing shows on screen.
---------------------------------------------

It doesn't fit with Apple's double-ended type-C cable, try using a with a normal type-C cable (with type-A on the other end).

How to re-configure WiFi settings?
---------------------------------------

When the device failed to access WiFi network on startup, it will enter WiFi provision mode.

It can also be manually set it to WiFi provision mode, by:

	#. Hold down **left button**, then power on device, until a beep.
	#. Follow instructions on device's screen, connect to its WiFi hotspot, then re-configure WiFi settings.

Settings web page can't be accessed
----------------------------------------
			
	#. Make sure your phone is in the same WLAN as the device, and the WiFi is 2.4GHz, not 5GHz.
	#. Check that the device's `settings server is turned on <settings.html>`_
						
Weather interface shows no data
------------------------------------

	#. Follow instructions on how to `setup weather data <weather.html>`_
	#. In the device's weather interface, click right button to force a manual update, see if any :xref:`error code <https://dev.qweather.com/en/docs/resource/status-code/>` shows up.
		

Cryptocurrency prices not showing
-----------------------------------

	#. Check that :xref:`https://coincap.io <https://coincap.io>` is accessible via your router.
	#. In the settings web page, make sure you input correct `ids <coincap_assets.html>`_ in the "Others" textbox, if any. 

Device fails to reboot after after firmware update
------------------------------------------------------

This happens occasionally when newly updated firmware cannot read previous settings, please try delete previous settings by :ref:`factory reset <How to factory reset?>`

Device repeatedly reboots after downloading new clock face
---------------------------------------------------------------

If errors occur when downloading optional clock faces, or the downloaded resource is malformed, the device may have problem loading the resources on startup, then it reboots, and then fail again...

You can force device to skip loading clock face resources on startup, then delete them:

	#. Hold down **right button**, then power on device, until a beep.
	#. After device starts, go to the settings web page → *Clock Faces* → select *(Optional N)* from dropdown menu → click *delete* button.
	#. Check for `firmware updates <ota.html>`_.
	#. If the problem remains, try :ref:`factory reset <How to factory reset?>`
			
		
	
How to factory reset?
-------------------------

* Click the *reset* button in settings web page.

* Or, you can hard reset device on startup by:
	
	#. Hold down **both buttons**, then power on device, until you hear 2 beeps.
	#. Now the device will delete all custom settings, including QWeather KEY and any optional clock faces, but WiFi settings will be kept.

		
		
Can I design my own clock face (and share it)?
---------------------------------------------------

It's currently impractical for users to design custom clock faces, due to lack of a user-friendly software with graphical interface to facilitate this.


Can I flash 3rd party firmware?
------------------------------------

No, the serial port is disabled.