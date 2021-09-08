window.onload = function() {
	const copy_button = document.createElement("button");
	copy_button.style.position = "absolute";
	copy_button.style.top = "-6px";
	copy_button.style.left = "-12px";
	copy_button.style.padding = "0px";
	copy_button.style.width = "13px";
	copy_button.style.height = "13px";
	copy_button.style.cursor = "pointer";
	copy_button.innerHTML = "+";
	for (const cb of document.querySelectorAll("code")) {
		const local_button = copy_button.cloneNode(true);
		local_button.addEventListener("click", function() {
			navigator.clipboard.writeText(this.parentElement.innerText.slice(0, -3));
		});
		cb.style.position = "relative";
		cb.appendChild(local_button);
	}
	console.info("Extension: Added copy buttons.");
};