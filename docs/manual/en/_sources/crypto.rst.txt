Cryptocurrencies
====================

Value to USD and 24-hour change rate are fetched from :xref:`coincap.io <https://coincap.io>`

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
   <br><br><br><br>
   <script>
      fetch('https://api.coincap.io/v2/assets').then(r=>r.json()).then(
         assets=>document.querySelector('#assets tbody').innerHTML += assets.data.map(({id,name,symbol})=>`<tr><td>${id}</td><td>${symbol}</td><td>${name}</td></tr>`).join('')
      );
   </script>