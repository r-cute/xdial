Time zone
========================

The time zone input box accepts POSIX timezone string format.

.. raw:: html

   <style>
      #assets{
         border-collapse: collapse;
         th,td{border:1px solid grey;text-align: center;}
         th{background-color: lightgrey}
      }
   </style>
   <table id='tz'><thead><tr><th>Region</th><th>Time zone</th></tr></thead><tbody></tbody></table>
   <script>
   	fetch('../../timezone.js').then(r=>r.json()).then(tz=>
      	document.querySelector('#tz tbody').innerHTML += Object.entries(tz).map(([key, val])=>`<tr><td>${key}</td><td>${val}</td></tr>`).join('')
      );
   </script>