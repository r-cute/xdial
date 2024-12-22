Stocks
=========

Stock ticker symbols consist of

* *A股* 代码为 6 位数字，如平安银行是 `000001`
* *港股* 是 5 位数字，如小米集团 `01801`
* *美股* 代码一般是大写的英文，比如特斯拉是 `TSLA`

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
