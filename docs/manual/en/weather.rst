Weather
=========

Weather data can be fetched from :xref:`QWeather <https://www.qweather.com/en>` **for free** :

  #. :xref:`Sign up <https://dev.qweather.com/en>` for a QWeather account.
  #. Login to QWeather's :xref:`Project <https://console.qweather.com/#/apps?lang=en>` page → click *Create Project* → fill in "Project Name" and choose *Free Subscription* → *Create* → *Create Credential* → select *API KEY* and fill in *Credential name* → click *Create* → copy the *API KEY* string.
  #. Go back to the settings web page, pasted the KEY, search and select your location, then click "Save".
  #. Now you shall see weather data appear in the "Weather" interface on device, data will be sync-ed periodically.

.. note::
   | Currently the :xref:`limit <https://dev.qweather.com/en/docs/finance/subscription/#comparison>` on the number of weather data request per day for free subscription account is 1000. And the number of data requests for each device is ((60 / update_interval + 3) * 24) per day.
   | That makes it possible to share the same key between 2 devices if both set update interval to 5 min, or 4 devices if update interval set to 10 min.

\

.. raw:: html

   <div class="ver">
   <b>Video guide</b>
   <iframe src="https://www.bilibili.com/blackboard/html5mobileplayer.html?isOutside=true&aid=113382824870887&bvid=BV1HT1GYdEGS&cid=26498107811&p=1&high_quality=1&danmaku=0" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true"></iframe>
   </div>