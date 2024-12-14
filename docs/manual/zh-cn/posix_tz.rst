时区
========================

时区一栏接受 "POSIX timezone string" 格式. 北京时间可填入 "UTC-8"，以下是一些其他地区对应的时区

.. raw:: html

   <style>
      #assets{
         border-collapse: collapse;
         th,td{border:1px solid grey;text-align: center;}
         th{background-color: lightgrey}
      }
   </style>
   <table id='tz'><thead><tr><th>地区</th><th>时区</th></tr></thead><tbody></tbody></table>
   <script>
   	fetch('../../timezone.js').then(r=>r.json()).then(tz=>
      	document.querySelector('#tz tbody').innerHTML += Object.entries(tz).map(([key, val])=>`<tr><td>${key}</td><td>${val}</td></tr>`).join('')
      );
   </script>