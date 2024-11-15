天气
========

天气数据是通过 **免费订阅** :xref:`和风天气 <https://www.qweather.com>` 获取的，步骤如下：

	#. :xref:`注册 <https://dev.qweather.com>` 和风天气的开发账号。
	#. 登录和风天气 :xref:`项目管理 <https://console.qweather.com/#/apps>` 页面 → 点击 *创建项目* → 任意填写名称，选择 *免费订阅* → 点击 *创建* → *创建凭据* → 选择 *API KEY* → 任意填写名称，点击 *创建* → 复制生成的 API KEY。
	#. 返回网页版设置页面，在 “天气” 栏里填入 KEY，查找并选择您所在城市，然后点击 “保存” 按钮 。
	#. 此时您便可以在设备的天气界面看到气象数据，设备会根据设置定期更新数据。

.. note::
   | 设备每天的天气数据请求次数约为 ((60 / 刷新间隔 + 3) * 24) 次，而目前免费订阅账号的数据请求 :xref:`限制 <https://dev.qweather.com/docs/finance/subscription/#comparison>` 是 1000 次/天。
   | 因此，如果刷新间隔都设为 5 分钟，则两个设备可以共享一个 KEY; 如果都设为 10 分钟，则 4 个设备可以共用一个 KEY。

\

.. raw:: html

   <div class="ver">
   <b>视频演示</b>
   <iframe src="https://www.bilibili.com/blackboard/html5mobileplayer.html?isOutside=true&aid=113382824870887&bvid=BV1HT1GYdEGS&cid=26498107811&p=1&high_quality=1&danmaku=0" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true"></iframe>
   </div>