const msg = document.getElementById('msg');
const h = document.getElementById('h');

function E() {
	var txt = msg.value;
	var enc = window.btoa(txt);
	document.getElementById("h").innerHTML = enc;
}

function D() {
	var txt = msg.value;
	var enc = window.atob(txt);
	document.getElementById("h").innerHTML = enc;
}
