addEventListener("load", ev =>{
	var url = location.href;
	var el = document.getElementsByTagName('h1')[0];
	var insert = document.createElement('p');
	insert.style['text-indent'] = 0;
	insert.innerHTML = url.indexOf('/en/')>=0 ?
		`<a href="${url.replace('/en/','/zh-cn/')}">[中文]</a>` :
		`<a href="${url.replace('/zh-cn/','/en/')}">[English]</a>`;
	el.parentNode.insertBefore(insert, el.nextSibling);
});