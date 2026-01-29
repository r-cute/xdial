Weather
=========

Weather data can be fetched from :xref:`QWeather <https://www.qweather.com/en>` **for free** :

  #. :xref:`Sign up <https://dev.qweather.com/en>` for a QWeather account.
  #. **API Host** can be found in the :xref:`Setting <https://console.qweather.com/setting?lang=en>` page of Developer Console.
  #. In the :xref:`Project <https://console.qweather.com/project?lang=en>` page → click *Create Project* → fill in "Project Name" then *Save* → click *Add Credential* → select *API KEY* and fill in *Credential name* → click *Save* → copy the **API KEY** string.
  #. Go back to the settings web page, pasted the KEY
  #. type in the city you're at, the click 🔍search and select your location, click "Save" button.
  #. Now you shall see weather data appear in the "Weather" interface on device.

To disable the weather service, simply clear the location input field.

.. note::
   The number of weather data requests for each device is ((60 / update_interval + 5) * 24) per day, it's far less than the :xref:`free subscription limit <https://blog.qweather.com/announce/free-subscription-service-update>` . 

.. warning::
   Keep the API KEY private to yourself!

