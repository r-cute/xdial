Time zone
========================

The time zone text field accepts POSIX timezone string format.

.. raw:: html

   <style>
      #tz{
         border-collapse: collapse;
         th,td{border:1px solid grey;text-align: center;}
         th{background-color: lightgrey}
      }
   </style>
   <table id='tz'><thead><tr><th>Region</th><th>Time zone</th></tr></thead><tbody></tbody></table>
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