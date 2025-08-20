const http = require('https');

const options = {
	method: 'GET',
	hostname: 'bhagavad-gita3.p.rapidapi.com',
	port: null,
	path: '/v2/chapters/?skip=0&limit=18',
	headers: {
		'x-rapidapi-key': '1dbc008694msh2c77544c94ab37ap1aeb3cjsne587ac3b8899',
		'x-rapidapi-host': 'bhagavad-gita3.p.rapidapi.com'
	}
};

const req = http.request(options, function (res) {
	const chunks = [];

	res.on('data', function (chunk) {
		chunks.push(chunk);
	});

	res.on('end', function () {
		const body = Buffer.concat(chunks);
		console.log(body.toString());
	});
});

req.end();