天气
========

天气数据是通过 **免费订阅** :xref:`和风天气 <https://www.qweather.com>` 获取的，步骤如下：

	#. :xref:`注册 <https://dev.qweather.com>` 和风天气的开发账号。
	#. 登录和风天气 :xref:`项目管理 <https://console.qweather.com/#/apps>` 页面 → 点击 *创建项目* → 任意填写名称，选择 *免费订阅* → 点击 *创建* → *创建凭据* → 选择 *API KEY* → 任意填写名称，点击 *创建* → 复制生成的 API KEY。
	#. 返回网页版设置页面，在 “天气” 栏里填入 KEY，查找并选择您所在城市，然后点击 “保存” 按钮 。
	#. 此时您便可以在设备的天气界面看到气象数据，设备会根据设置定期更新数据。

.. note::
   一台设备的天气数据请求次数约为 ((60 / 刷新间隔 + 5) * 24) 次/天，远低于 :xref:`和风天气提供的免费额度 <https://blog.qweather.com/announce/free-subscription-service-update>`。

\

.. raw:: html

   <div class="ver">
   <b>视频演示</b>
   <iframe src="https://www.bilibili.com/blackboard/html5mobileplayer.html?isOutside=true&aid=113382824870887&bvid=BV1HT1GYdEGS&cid=26498107811&p=1&high_quality=1&danmaku=0" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true"></iframe>
   </div>