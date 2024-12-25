加密货币
===============

加密货币界面显示的涨跌幅为 24 小时内的涨跌幅

id 号
-------------

.. _ids:

.. raw:: html

   <style>
      #assets{
         border-collapse: collapse;
         th,td{border:1px solid grey;text-align: center;}
         th{background-color: lightgrey}
      }
   </style>
   <table id='assets'><thead><tr><th>id</th><th>缩写</th><th>名称</th></tr></thead><tbody></tbody></table>
   <br><br><br><br>
   <script>
      fetch('https://api.coincap.io/v2/assets').then(r=>r.json()).then(
         assets=>document.querySelector('#assets tbody').innerHTML += assets.data.map(({id,name,symbol})=>`<tr><td>${id}</td><td>${symbol}</td><td>${name}</td></tr>`).join('')
      );
   </script>