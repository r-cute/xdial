addEventListener("load", ev =>{
	// var url = location.href;
	// var el = document.getElementsByTagName('h1')[0];
	// var insert = document.createElement('p');
	// insert.style['text-align'] = 'right';
	// insert.innerHTML = url.indexOf('/en/')>=0 ?
	// 	`<a href="${url.replace('/en/','/zh/')}">[中文]</a>` :
	// 	`<a href="${url.replace('/zh/','/en/')}">[English]</a>`;
	// el.parentNode.insertBefore(insert, el);
	var url = location.href;
	var li=document.querySelector('div[role="navigation"] ul li[class="wy-breadcrumbs-aside"]');
	li.style.display='inline-block';
	li.innerHTML=
		url.indexOf('/en/')>=0 ?
		`<a href="${url.replace('/en/','/zh/')}">[中文]</a>` :
		`<a href="${url.replace('/zh/','/en/')}">[English]</a>`;
});