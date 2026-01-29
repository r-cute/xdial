时区
========================

时区一栏接受 "POSIX timezone string" 格式，如北京时间（东八区）可填入 "UTC-8"

以下是一些其他地区对应的时区

.. raw:: html

   <style>
      #tz{
         border-collapse: collapse;
         th,td{border:1px solid grey;text-align: center;}
         th{background-color: lightgrey}
      }
   </style>
   <table id='tz'><thead><tr><th>地区</th><th>时区</th></tr></thead><tbody></tbody></table>
   <script>
      tb = document.querySelector('#tz');
      fetch('../timezone.json').then(r=>r.json()).then(
         tz=>Object.entries(tz).forEach(([key, val])=>{
            var row = tb.insertRow(-1);
            row.insertCell(0).innerText = key;
            row.insertCell(1).innerText = val;
         })
      );
   </script>