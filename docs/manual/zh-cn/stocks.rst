股票
=======

股票界面的大数字为当前价格，其下方显示当天或最后一个交易日的开盘价、最高价和最低价。在收盘时，当前价即为收盘价。

id 号
-----------

.. _ids:

股票 id 号以交易所两位字母开头，加上数字或英文代码。注意大小写不能写错！

* *A股* 分为上交所 "sh"、深交所 "sz" 和北交所 "bj"，加上 6 位数字。如贵州茅台 `sh600519`, 平安银行 `sz000001`, 聚星科技 `bj920111`
* *港股* 一般是 "hk" + 5 位数字, 如小米集团 `hk01810`；指数则是 "hk" + 大写字母，如恒生指数 `hkHSI`
* *美股* 是 "us" + 大写的英文，如特斯拉 `usTSLA`

.. raw:: html

   <script>
   	eid=x=>document.getElementById(x);
   	currency_translate={USD:'美元',CNY:'元',HKD:'港币'};
      market_translate={'200':'美股','100':'港股','51':'深圳','1':'上海','62':'北京'};
   	tx_stock=s=>fetch('https://qt.gtimg.cn/q='+s).then(t=>t.arrayBuffer()).then(r=>new TextDecoder('GBK').decode(r));
      parse_stock=s=>tx_stock(s).then(r=>r.split('"')[1].split('~')).then(r=>{var o=Object.fromEntries(Object.entries({'交易所':0,'名称':1,'当前价':3,'当前点位':3,'涨跌幅':32,'开盘':5,'最高':33,'最低':34}).map(([k,v])=>[k,r[v]]));o.currency='USD,CNY,HKD'.split(',').filter(x=>r.includes(x))[0];o.idx=r.includes('ZS');return o;});
   	query_stock=async(s)=>{
   		var ret = await parse_stock(s);
         if(ret.idx) {
            delete(ret['当前价']);
         } else {
            ret['当前价'] += ' '+currency_translate[ret.currency];
            delete(ret['当前点位']);
         }
   		ret['涨跌幅'] += '%';
         delete(ret.idx);delete(ret.currency);delete(ret['交易所']);
   		eid('tb').innerHTML = Object.entries(ret).map(([k,v])=>`<tr><td>${k}</td><td>${v}</td></tr>`).join('');
   	};
   </script>
   <style>
      #tb{
         border-collapse: collapse;
         td{border:1px solid grey;padding-left:1em;padding-right: 1em}
         td:first-child{background-color: lightgrey}
      }
   </style>
   <div style="display:flex;justify-content:space-between;gap:0.15em"><input id='stock_id' placeholder="sh600519" type='text' style="flex:1"/><button onclick='var st_id=eid("stock_id");if(st_id.value.length==0)st_id.value=st_id.placeholder;query_stock(st_id.value.split(",")[0].trim())'>测试</button></div>
   <br><table id='tb'></table>
   <br><br><br><br>