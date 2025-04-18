天气
========

天气数据是从 :xref:`和风天气 <https://www.qweather.com>` **免费** 获取的，步骤如下：

	#. :xref:`注册 <https://dev.qweather.com>` 和风天气的开发账号。
	#. **API Host** 可在开发者控制台的 :xref:`设置 <https://console.qweather.com/setting>` 页面里找到。
	#. 在 :xref:`项目管理 <https://console.qweather.com/project>` 页面 → 点击 *创建项目* → 任意填写名称，*保存* → 点击 *创建凭据* → 选择 *API KEY* → 任意填写凭据名称，点击 *保存* → 复制生成的 **API KEY** .
	#. 返回设备的设置页面，在 “天气” 栏里填入 API Host 和 API KEY.
	#. 填写您所在城市，然后点击🔍搜索，在弹出的县、区里点选，最后点击 “保存” 按钮 。
	#. 此时您便可以在设备的天气界面看到气象数据。

如果要设备停止获取天气服务，只要清除城市一栏的设置。

.. note::
   一台设备的天气数据请求次数约为 ((60 / 刷新间隔 + 5) * 24) 次/天，:xref:`和风天气提供的免费额度 <https://blog.qweather.com/announce/free-subscription-service-update>` 完全足够个人使用。

.. warning::
	请勿与他人分享 API KEY!

