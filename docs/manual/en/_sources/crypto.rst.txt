Cryptocurrencies
====================

Value to USD and 24-hour change rate are fetched from :xref:`coinlore.com <https://www.coinlore.com/all_coins>`

Crypto ids
----------------

.. _ids:

.. raw:: html

   <style>
      #assets{
         border-collapse: collapse;
         th,td{border:1px solid grey;text-align: center;}
         th{background-color: lightgrey}
      }
   </style>
   <table id='assets'><thead><tr><th>id</th><th>symbol</th><th>name</th></tr></thead><tbody></tbody></table>
   <br><button onclick="more()">More</button>
   <br><br><br><br>
   <script>
      function get_data(start, limit) { // limit max = 100
         return fetch(`https://api.coinlore.net/api/tickers/?start=${start??0}&limit=${limit??100}`).then(r=>r.json()).then(
            assets=>document.querySelector('#assets tbody').innerHTML += assets.data.map(({id,name,symbol})=>`<tr><td>${id}</td><td>${symbol}</td><td>${name}</td></tr>`).join('')
         );
      }
      start_num = 0;
      function more() {var p=get_data(start_num);start_num+=100;return p;}
      more().then(more).then(more);
   </script>