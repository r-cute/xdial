FAQ
============

How to re-configure WiFi settings?
---------------------------------------

When the device failed to access WiFi network on startup, it will enter WiFi provision mode.

It can also be manually set it to WiFi provision mode, by:

	#. Hold down **left button**, then power on device, until a "beep" sound.
	#. Follow instructions on device's screen, connect to its WiFi hotspot, then re-configure WiFi settings.

Unable to visit device's settings web page
---------------------------------------------
			
	#. Make sure your phone is on the same LAN as the device.
	#. Check that the device's `settings server is turned on <settings.html>`_
						
Weather interface shows no data
------------------------------------

	#. Follow instructions on how to `setup weather data <weather.html>`_
	#. In the device's weather interface, click right button to force a manual update, see if any :xref:`error code <https://dev.qweather.com/en/docs/resource/status-code/>` shows up.
		

Device reboots infinitely after downloading new clock face
---------------------------------------------------------------

If errors occur when downloading optional clock faces, or the downloaded resource is malformed, the device may have problem loading the resources on startup, then it reboots, and then fail again...

You can force device to skip loading clock face resources on startup, then delete them:

	#. Hold down **right button**, then power on device, until a "beep" sound.
	#. After device starts, go to the settings web page → *Clock Faces* → select *(Optional N)* from dropdown menu → click *delete* button.
	#. Check for `firmware updates <ota.html>`_.
	#. If the problem remains, try :ref:`factory reset <How to factory reset?>`
			
		
	
How to factory reset?
-------------------------

* Click the *reset* button in settings web page.

* Or, you can hard reset device on startup by:
	
	#. Hold down **both buttons**, then power on device, until you hear 2 "beep" sound.
	#. Now the device will delete all custom settings, including QWeather KEY and any optional clock faces, but WiFi settings will be kept.

		
		
Can I design my own clock face (and share it)?
---------------------------------------------------

It's still impractical for users to design custom clock faces, because currently we don't have a user-friendly software with graphical interface to facilitate this.
