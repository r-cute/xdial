Stocks
=========

The values below the line are: opening price, highest and lowest price in the day.

Stock ids
--------------

.. _ids:

Stock ids consist of a 2-letter exchange market symbol and the stock code (ticker symbol). Note that stock ids are case sensitive!

* Exchange markets in **Chinese mainland** includes Shanghai "sh", Shenzhen "sz" and Beijing "bj" Exchange. e.g. 贵州茅台 `sh600519`, 平安银行 `sz000001`, 聚星科技 `bj920111`
* For **Hong Kong** exchange market, it's "hk" + 5 digits. e.g. XiaoMi Corporation is `hk01810`
* For stocks in the **U.S.**, it's "us" + ticker symbol. e.g. Tesla is `usTSLA`

.. raw:: html

   <script>
   	eid=x=>document.getElementById(x);
      market_translate={'200':'US','100':'HK','51':'深圳','1':'上海','62':'北京'};
   	tx_stock=s=>fetch('https://qt.gtimg.cn/q='+s).then(t=>t.arrayBuffer()).then(r=>new TextDecoder('GBK').decode(r));
      parse_stock=s=>tx_stock(s).then(r=>r.split('"')[1].split('~')).then(r=>{var o=Object.fromEntries(Object.entries({'Market':0,'Name':1,'Price':3,'Value':3,'Change':32,'Open':5,'High':33,'Low':34,'Name_EN':46}).map(([k,v])=>[k,r[v]]));o.currency='USD,CNY,HKD'.split(',').filter(x=>r.includes(x))[0];o.idx=r.includes('ZS');return o;});
   	query_stock=async(s)=>{
   		var ret = await parse_stock(s);
         if(ret.idx) {
            delete(ret.Price);
         } else {
            ret.Price += ' ' + ret.currency;
            delete(ret.Value);
         }
   		ret.Change += '%';
         if(['100','200'].includes(ret.Market)) {
            ret.Name=ret.Name_EN;
         }
         delete(ret.Name_EN);delete(ret.Market);
         delete(ret.idx);delete(ret.currency);
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
   <div style="display:flex;justify-content:space-between;gap:0.15em"><input id='stock_id' type='text' placeholder='usTSLA' style="flex:1"/><button onclick='var st_id=eid("stock_id");if(st_id.value.length==0)st_id.value=st_id.placeholder;query_stock(st_id.value.split(",")[0].trim())'>Test</button></div>
   <br><table id='tb'></table>
   <br><br><br><br>
