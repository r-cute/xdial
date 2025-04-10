Cryptocurrencies
====================

Value to USD and 24-hour change rate are fetched from :xref:`coinlore.com <https://www.coinlore.com>`

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
   <br><button onclick="get_data(page_id++)">More</button>
   <br><br><br><br>
   <script>
      async function get_data(start, limit) { // limit max = 100
         await fetch(`https://api.coinlore.net/api/tickers/?start=${start}&limit=${limit}`).then(r=>r.json()).then(
            assets=>document.querySelector('#assets tbody').innerHTML += assets.data.map(({id,name,symbol})=>`<tr><td>${id}</td><td>${symbol}</td><td>${name}</td></tr>`).join('')
         );
      }
      page_id = 0;
      for(page_id=0;page_id<3;page_id++) {
         await get_data(page_id, 100);
      }
   </script>