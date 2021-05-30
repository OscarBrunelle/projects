let offers = [];

function download(data = JSON.stringify(offers), filename = "Offres", type = "csv") {
	const file = new Blob([data], {
		type: type
	});
	if (window.navigator.msSaveOrOpenBlob) // IE10+
		window.navigator.msSaveOrOpenBlob(file, filename);
	else { // Others
		const a = document.createElement("a"),
			url = URL.createObjectURL(file);
		a.href = url;
		a.download = filename;
		document.body.appendChild(a);
		a.click();
		setTimeout(function () {
			document.body.removeChild(a);
			window.URL.revokeObjectURL(url);
		}, 0);
	}
}

function add_offers() {
	const offer_elements = document.querySelectorAll(".AdCard__AdCardLink-sc-1h74x40-0.cHZrAn");

	for (const offer of offer_elements) {
		const link = "https://www.leboncoin.fr/" + offer.getAttribute("href");

		let title_element = offer.querySelector(".AdCardTitle-e546g7-0");
		const title = title_element.innerHTML;

		const price_element = offer.querySelector(".AdCardPrice__Amount-bz31y2-1");
		const price = parseInt(price_element.innerHTML.split(" €")[0]);

		let postal_element = offer.querySelectorAll("._2k43C._137P-.P4PEa._3j0OU")[1];
		const postal = postal_element.innerHTML.split(" ")[1];

		offers.push({
			title: title,
			price: price,
			postal: postal,
			link: link
		});
	}

	let total = 0;
	let min = Infinity,
		min_link,
		max = 0,
		max_link;
	for (const offer of offers) {
		total += offer.price;
		if (offer.price < min) {
			min = offer.price;
			min_link = offer.link;
		}
		if (offer.price > max) {
			max = offer.price;
			max_link = offer.link;
		}
	}
	let average = total / offers.length;

	console.log(offers);
	console.log(`Average: ${average} €`);
	console.log(`Min: ${min} €; ${min_link}`);
	console.log(`Max: ${max} €; ${max_link}`);

	//const data_url = "https://www.oscarbrunelle.com/projects/tables/index.html?data=" + encodeURIComponent(JSON.stringify(offers));
	const data_url = "https://127.0.0.1:5500/projects/tables/index.html?data=" + encodeURIComponent(JSON.stringify(offers));
	console.log(encodeURIComponent(JSON.stringify(offers)));
	console.log("See data at: " + data_url);
	window.open(data_url);
}

add_offers();